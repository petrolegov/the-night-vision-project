# Do everything based on OpenCV, not PiCamera:
#    (1) OpenCV is platform-independent (Windows/Linux, PC/Laptop/RaspberryPi), PiCamera only works on RaspberryPi or with major hackarounds
#    (2) OpenCV has a much lower latency (faster reaction!), because PiCamera will sniff the HDMI output, which is slow
# This script is (more or less) optimized for low latency. For this reason no IF-ELSE branching is performed IN the endless loops ("while True"), but 4 methods have been defined.
# By this, the IF-ELSE decision is moved out of the inner loop, which avoids slowing down the inner loop and reduces latency.
import cv2


  
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
    


# definition of main routine
def __main__():
    print("\n\nDIY Night Vision (Windows 64-Bit)\n")
    print("Exit camera view & program with <ESC> key!\n")
    print("-------------------------------------------------------\n\n")

    # stream only camera 0 (first camera plugged in) & in full screen mode. You are welcome to add changes if you like!
    stream_night_vision_fullscreen(cam_sel=0)
        
        

# perform main routine
__main__()


