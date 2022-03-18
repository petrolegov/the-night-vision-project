# Do everything based on OpenCV, not PiCamera:
#    (1) OpenCV is platform-independent (Windows/Linux, PC/Laptop/RaspberryPi), PiCamera only works on RaspberryPi or with major hackarounds
#    (2) OpenCV has a much lower latency (faster reaction!), because PiCamera will sniff the HDMI output, which is slow
# This script is (more or less) optimized for low latency. For this reason no IF-ELSE branching is performed IN the endless loops ("while True"), but 4 methods have been defined.
# By this, the IF-ELSE decision is moved out of the inner loop, which avoids slowing down the inner loop and reduces latency.
import cv2



# definition of night vision camera streaming:   fullscreen: NO,   resize: NO
def stream_night_vision_fast(cam_sel=0, cam_window_name="Night Vision (EXIT with <ESC> key)"):
    cap = cv2.VideoCapture(cam_sel)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open (night vision) camera. Check if camera is properly connected!")

    # endless loop until <ESC> is pressed
    while True:
        # read individual camera frame
        ret, frame = cap.read()

        # update display
        try:
            cv2.imshow(cam_window_name, frame)
            cv2.setWindowProperty(cam_window_name, cv2.WND_PROP_TOPMOST, 1)     # always set video to foreground of each program
        except:
            print("ERROR:   Showing the video stream failed")
            pass

        #  exit on <ESC> key
        if cv2.waitKey(1) ==  27:
            break

    cap.release()
    cv2.destroyAllWindows()  

  
# definition of night vision camera streaming:   fullscreen: YES,   resize: NO
def stream_night_vision_fullscreen(cam_sel=0, cam_window_name="Night Vision (EXIT with <ESC> key)"):
    cap = cv2.VideoCapture(cam_sel)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open (night vision) camera. Check if camera is properly connected!")

    # endless loop until <ESC> is pressed
    while True:
        # read individual camera frame
        ret, frame = cap.read()
        
        # configure fullscreen...fullscreen makes only sense on small displays (5", 7"), otherwise latency will be large & video will lag extremely!
        cv2.namedWindow(cam_window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(cam_window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        # update display
        try:
            cv2.imshow(cam_window_name, frame)
            cv2.setWindowProperty(cam_window_name, cv2.WND_PROP_TOPMOST, 1)     # always set video to foreground of each program
        except:
            print("ERROR:   Showing the video stream failed")
            pass
        
        #  exit on <ESC> key
        if cv2.waitKey(1) ==  27:
            break

    cap.release()
    cv2.destroyAllWindows()
    
    
# definition of night vision camera streaming:   fullscreen: NO,   resize: YES
def stream_night_vision_resize(resize_format=(1, 1), cam_sel=0, cam_window_name="Night Vision (EXIT with <ESC> key)"):
    cap = cv2.VideoCapture(cam_sel)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open (night vision) camera. Check if camera is properly connected!")

    # endless loop until <ESC> is pressed
    while True:
        # read individual camera frame
        ret, frame = cap.read()
        
        # resizing format will be given by a tuple with reshape factors for   x (index 0)   and   y (index 1)
        try:
            frame = cv2.resize(frame, None, fx=int(resize_format[0]), fy=int(resize_format[1]), interpolation=cv2.INTER_AREA)
        except:
            print("ERROR:   Resizing the video failed. Might be because of broken data coming in.")
        
        # update display
        try:
            cv2.imshow(cam_window_name, frame)
            cv2.setWindowProperty(cam_window_name, cv2.WND_PROP_TOPMOST, 1)     # always set video to foreground of each program
        except:
            print("ERROR:   Showing the video stream failed")
            pass
        
        #  exit on <ESC> key
        if cv2.waitKey(1) ==  27:
            break

    cap.release()
    cv2.destroyAllWindows()



# definition of main routine
def __main__():
    fullscreen = True         # not fullscreen  ->  lower latency  ->  immediate camera data!
    resize_format = (1, 1)     # not resizing    ->  lower latency  ->  immediate camera data!

    print("\n\nDIY Night Vision (Windows 64-Bit)\n")
    print("Exit camera view & program with <ESC> key!\n")
    print("-------------------------------------------------------\n\n")

    print("Select camera (maybe restart and try other camera if showing wrong camera data):\n")
    print("\t(0)  -  system camera (or only camera)   -->   press   0   then   <ENTER>\n")
    print("\t(1)  -  external camera (if it is not the only camera)   -->   press   1   then   <ENTER>\n")
    try:
        cam_sel = int(input())
    except:
        cam_sel = 0
        pass

    print("Enter full-screen mode (will be slightly slower)?\n")
    print("\t(y)  -  Yes   -->   press   y   then   <ENTER>\n")
    print("\t(n)  -  No   -->   press   n   then   <ENTER>\n")
    input_key = input()
    if input_key == 'y':
        fullscreen = True
    else:
        fullscreen = False
        print("Resize with factors   (x,y)?   Enter   (1,1)   if no resize desired.\nFinish each scaling factor with   <ENTER>\n")
        x_scale = input("Integer scaling factor for x:   ")
        y_scale = input("Integer scaling factor for y:   ")
        resize_format = (x_scale, y_scale)

    if ((fullscreen == True)  and  not(resize_format == (1, 1))):
        """ SAME AS CASE BELOW BECAUSE LOGIC ! """
        print("It does not make sense to have full-screen mode AND resize. Switching to fullscreen instead!")
        stream_night_vision_fullscreen(cam_sel=cam_sel)
        
    elif ((fullscreen == True)  and  (resize_format == (1, 1))):
        """ fullscreen: YES,   resize: NO """
        stream_night_vision_fullscreen(cam_sel=cam_sel)
        
    elif ((fullscreen == False)  and  not(resize_format == (1, 1))):
        """ fullscreen: NO,   resize: YES """
        stream_night_vision_resize(cam_sel=cam_sel, resize_format=resize_format)
        
    elif ((fullscreen == False)  and  (resize_format == (1, 1))):
        """ fullscreen: NO,   resize: NO     (MINIMUM LATENCY -> FASTEST CAMERA UPDATES!!!) """
        stream_night_vision_fast(cam_sel=cam_sel)
        
        

# perform main routine
__main__()


