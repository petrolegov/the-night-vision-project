# Welcome to the Night Vision Project!

This is a DIY project about the topic "night vision", which can be used to observe animals or other sceneries.

It is more a collection of tutorials how to build such a system. Necessary code will be provided, but is just seen as a component to build the night vision system. Everything will be explained in detail, so any person with some IT knowledge can implement the solution (even if the person has never worked with RaspberryPi, night vision cameras, Linux operating systems or Python before).

Different tutorials targeting a variety of night vision systems will be uploaded continuously to serve as a starting point for development and adaptation of own night vision systems.

<p align="center">
    <img width="400" height="200" src="https://user-images.githubusercontent.com/101147656/158529013-6f5bc1c1-0b35-4f34-a17e-666b50693e66.png">
</p>


## Contents

1. [Technical Basics of Night Vision](#technical-basics-of-night-vision)
2. [A Stationary Night Vision System Based on PC or Laptop](#a-stationary-night-vision-system-based-on-pc-or-laptop)
3. [A More Flexible Night Vision System Based on RaspberryPi](#a-more-flexible-night-vision-system-based-on-raspberrypi)
4. [An Autonomously Usable Night Vision System for Mobile Usage](#an-autonomously-usable-night-vision-system-for-mobile-usage)
5. [Multiple Night Vision Nodes Accessible Via Website](#multiple-night-vision-nodes-accessible-via-website)
6. [Safety Instructions](#safety-instructions)
7. [Ordering and Delivery Hints](#ordering-and-delivery-hints)
8. [Useful RaspberryPi Links](#useful-raspberrypi-links)



## 1 - Technical Basics of Night Vision

<p align="center">
    <img width="400" height="400" src="https://user-images.githubusercontent.com/101147656/158277081-7132d559-cd76-4878-a340-4fadb5897f2c.jpeg">
</p>

Most cheap night vision cameras are simple optical cameras with a switchable IR cut filter. The IR cut filter typically filters out infrared (IR) light during daytime, leaving only (humanly) visible light for observation, which preserves "natural" colors for the human eye.

At night (or low illumination), this IR cut filter is switched off. The infrared light then is visible, resulting in more visible features during the night.

When the IR cut filter is switched on or off, you usually hear a clicking noise. You hear the clicking noise because the IR cut filter is a mechanical shutter that blocks or passes infrared light. This might be a valuable information if you are in environments with varying light conditions and do not want to be heard, e.g. by a shy animal in the forest or inside a abandoned house.

**To avoid the clicking noise** and be noiseless in varying light conditions, you need to understand the circuit behind a little better:

The decision "IR cut filter on/off" is usually depending on a comparator circuit using a photoresistor (see image above, red circles). Photoresistors are more conductive when illuminated, so they have a high resistance in darkness and a low resistance in light. The comparator circuit detects when the resistance of the photoresistor rises above the (fixed) value of another (standard) resistor, resulting in a signal to turn the IR cut filter off in darkness or low light. Vice versa, the IR cut filter is switched on when the resistance of the photoresistor drops below the other resistor value again in a bright surrounding.

<p align="center">
    <img width="150" height="100" src="https://user-images.githubusercontent.com/101147656/158277406-b5c0aac5-0a20-4165-96b5-584a56d373bb.jpeg">
</p>

If you now replace the photoresistor with a high resistor value (R=1MΩ for example, see image above), it will seem to the comparator circuit like the photoresistor is always in the dark. Then the IR cut filter will always be off, and you will always have a "night vision" display. You can look at it when you need it and ignore it when you are in the light, but **you will hear no clicking, so you are less noisy**...also works with putting a tape over the photoresistor ;)

If you want, you can also make the IR cut filter switchable via software. You need to use the GPIOs of a RaspberryPi in this case (when you use a RaspberryPi as computing gadget).


<br/>

**PLEASE ALWAYS CONSIDER THE [SAFETY INSTRUCTIONS](#safety-instructions) FOR INFRARED LIGTH, VISIBILITY BY OTHERS, SIGNIFICANT HEAT DEVELOPMENT AND ORDERING ISSUES!**

<br/>



## 2 - A Stationary Night Vision System Based on PC or Laptop

**Budget:   $35**


The simplest and cheapest (but also least flexible) way to build a night vision system is based on a PC (workstation) or laptop. Because you already have a power supply and a computing gadget, you will only need a camera that supports night vision (for example a cheap camera with switchable IR cut filter, see image below).

<p align="center">
    <img width="300" height="300" src="https://user-images.githubusercontent.com/101147656/158514531-b2ebbc28-085f-40c5-bb1c-c21e659364b9.png">
</p>



### 2.1 - Required Components
Assuming you have a laptop or PC workstation, you only need to buy a small and cheap camera that supports night vision via USB. One good option for a fair price is Arducam.

Two online shops where you can buy the Arducam are:
  * [UCTronics](https://www.uctronics.com/arducam-1080p-day-night-vision-usb-camera-module-for-computer-2mp-automatic-ir-cut-switching-all-day-image-usb2-0-webcam-board-with-ir-leds-for-windows-linux-android-and-mac-os.html)
  * [Amazon](https://www.amazon.com/Arducam-Computer-Automatic-Switching-All-Day/dp/B0829HZ3Q7)

Low Light WDR cameras with USB interface can be an alternative if ArduCam modules are sold out. But it is not really night-vision, just more sensitive to light than standard daylight camera modules. They are also more expensive. For example available from:
  * [Amazon](https://www.amazon.com/Arducam-Computer-Fisheye-Microphone-Windows/dp/B07ZS75KZR/ref=sr_1_6?keywords=Arducam+1080P+Day+%26+Night+Vision+USB+Camera&qid=1646702909&sr=8-6)

Instead of using a PC+monitor or a laptop, also a RaspberryPi (default type or RaspberryPi Zero, not RaspberryPi Pico) can be used as mini computer if available. They are more light-weight, the larger ones offer USB-A interfaces, they also allow an additional camera interface (MIPI CSI via ribbon cable).  
Solutions based on RaspberryPi will be presented in [section 3](#a-more-flexible-night-vision-system-based-on-raspberrypi) and [section 4](#an-autonomously-usable-night-vision-system-for-mobile-usage).



### 2.2 - Installation of the Stationary DIY Night Vision System

The assembly of the DIY night vision system is very straightforward. Just plug in the USB cable of the Arducam Day&Night camera into a PC or laptop. Done!

Then you can either download the Python code from this Github repository and run it in your IDE or from command line. Or, depending on your operating system, download the correct executable file. This will be specified in section 3.2, “Software”.



#### 2.2.1 - Mounting Location
An optimal mounting position of the night vision camera module is at a window, but you should place yourself with some distance to the night vision camera. The infrared LEDs of the night vision camera will emit red light, which might be seen and serve as a target for a potential enemy.


Either you already have a window close to your desk (see image above), then you might rearrange your desk position or just your monitor position.  
Or you can put the camera at the window connected to a laptop, where you can place the laptop with some distance to the window.  
You can also hang the camera outside of the window (some centimeters) and put the cable through the window.

The camera can also be helpful to look around the corner!

You can also use multiple infrared cameras at the same device, just call the script or program several times and increase the number entered at the beginning (see under TODO TODO TODO!!!).

**CAUTION:** Watch out that the infrared diodes and the complete camera module are not so close to textiles, curtains or similar. Infrared diodes send out warmth, they (and their environment) can get very hot!


### 2.3 - Software Setup
There are two options, either run the software via executable (works out of the box, requires less technical knowledge) OR run the Python scripts directly (recommended). Both options will be explained below.

#### 2.3.1 - Running Software from Executables
If you are not familiar with executing Python scripts and would like to have executable files for Windows 10 (64-Bit) or Ubuntu 20.04 (64-Bit), you can find them in following mega.nz file archive (complete link posted to check for correct link forwarding):
  * Windows 10 (64-Bit):   [https://mega.nz/folder/28VEhLaY#UC1vjnSJnoVBJkIUPk07HQ](https://mega.nz/folder/28VEhLaY#UC1vjnSJnoVBJkIUPk07HQ)
  * Ubuntu 20.04 (64-Bit): [https://mega.nz/folder/6xdgHT6C#PZ2-c4jJ__XEabcIsCxjUw](https://mega.nz/folder/6xdgHT6C#PZ2-c4jJ__XEabcIsCxjUw)
    
MEGA has end-to-end encryption, it should be quite safe. But this option is just for easy access. If you do not trust downloading this content, it is recommended to clone the Github repositories and execute the Python code via interpreter (in IDE or via command line).

If you prefer running the Pytrhon scripts directly or have a restricted / unstable internet connection / only very limited traffic, download the Python scripts (<10kB) instead of the executables (approx. 50MB), given that you have Python3 and all required Python packages installed. If packages need to be installed, they could also consume a lot of traffic.

#### 2.3.2 - Running Software as Python Scripts Directly
**Prerequisites:**
  * Python 3 (best: Python 3.7) is installed on your PC / laptop
  * pip package manager for Python is installed (conda is also okay, whatever you are familiar with)
  * Python script and package requirements, can be downloaded from: [https://github.com/petrolegov/the-night-vision-project](https://github.com/petrolegov/the-night-vision-project)

First install all the required Python modules. If you already installed the modules, they will be skipped or updated.
``` shell
python3 -m pip install --upgrade pip
python3 -m pip install requirements.txt
python3 night_vision_stationary.py
```

You can of coursae also run the script from an IDE.

### 2.4 - Software Control

<p align="center">
    <img width="700" height="400" src="https://user-images.githubusercontent.com/101147656/158526558-bcce0705-d184-4e47-b26c-b401f9dd73c8.png">
</p>

Different options can be selected during the start of the program, before any camera images are visible:
  * Camera Index   (0: system camera or only available camera,   1: external USB camera when other camera is present)
    * when using without any other camera, always use index 0
    * when another camera is installed at the system (especially a laptop webcam), enter index 1 to select the external USB Arducam
  * Full-screen Mode:
    * full-screen mode requires more resources, but on a workstation or laptop it should not play a role. Full-screen allows to see more details.
  * Scaling factors:
    * if no full-screen mode is selected, the camera display can be scaled manually. If not desired, simply set x-scaling & y-scaling to 1 each. Need to be integers!

If some option is selected by mistake (camera index for example), simply start the program again and enter another value. Some error handling will be added later to the program, the idea was to make the tutorial available ASAP, so fixes & improvements will be done continuously.

Once the display starts showing, the program can be closed with the escape key `ESC`. From terminal, the script can also be killed using `CTRL`+`C`.


### 2.5 - Additional Stuff
Some minor modifications can be made at the Arducam to enhance functionality and robustness.
    
**CAUTION: It seems like the focus can not be configured at Arducam (possibly AutoFocus). So do not destroy your objective by trying to wrench it hard!**
    
    
#### 2.5.1 - Making the Night Vision Camera More Robust
Although this is a minor concern for indoor usage, the weak points of the Arducam are the cable connectors. If you put some strong tape for additional security, the cables (and plug) should stay robust. The small wires can carefully be fixated to the objective (without breaking the cables!).

<p align="center">
   <img width="400" height="300" src="https://user-images.githubusercontent.com/101147656/158527816-23681885-fdb7-455e-bd00-9ded040a207d.png">
</p>


#### 2.5.2 - Multiple Camera Configuration
Becausea it is a USB connection, you can connect multiple cameras at once (looking at different directions when hanging outside the window, or one backwards and one towards front, or one around the corner, ...). Simply start the program twice (or more often) and change the camera ID (the limit is not 1 in this case, you can go up to “N-1”, where N is the number of cameras in the system).
    

## 3 - A More Flexible Night Vision System Based on RaspberryPi

**Budget:   $50...$60**


A big advantage of using a RaspberryPi instead of a workstation PC or laptop is that you have more options for the night vision camera. Additional to USB cameras that can be used with PC or laptop, RaspberryPi allows you to use MIPI CSI cameras as the ones shown below (left: ribbon cable for standard RaspberryPi, right: ribbon cable for smaller interface of RaspberryPi Zero):

<p align="center">
   <img width="300" height="300" src="https://user-images.githubusercontent.com/101147656/158514647-66dade3b-909b-49e4-8694-f2e5add9bd35.png">   
</p>

You are also more flexible when you want to mount your night vision system, because it does not have to be close to your workstation. You can also install the RaspberryPi night vision system close to your surrounding and observe the data via video stream by use of the WiFi function (look under [Useful RaspberryPi Links](#useful-raspberrypi-links) for a how-to).


### 3.1 - Required Components
The components you need depend on which device you use. It is different between RaspberryPi 1/2/3/4 and RaspberryPi Zero.

### 3.1.1 - Basic Equipment
You need following things:

**Power supply with USB connector:**
This can be a USB power plug (left) if you have a power supply around. It can also be a powerbank (middle) or a solar battery pack (right) with USB plug for mobile use or if you do not have a power supply around.

<p align="center">
    <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158885813-4d351a6c-24a8-4353-b639-5a9d38306729.png">
    <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158885667-bfd83447-93cf-430d-8ff5-89281a7ec00f.png">
    <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158885935-c4d09568-bee6-452c-b3a6-ef390d2ed99a.png">
</p>


**RaspberryPi 1/2/3/4 (left) or RaspberryPi Zero (right):**
RaspberryPi are sold out anywhere, so either you already have one or you can also use a BananaPi, OrangePi or other RaspberryPi derivatives. As long as they have USB ports or MIPI CSI ports for your night vision camera and a (Micro)HDMI or another MIPI CSI port for your large HDMI monitor or your small TFT monitor. For this reason, you **cannot use a RaspberryPi Pico**, it has no connector for screen.
<p align="center">
   <img width="300" height="200" src="https://user-images.githubusercontent.com/101147656/158883627-363ebe46-b3e6-4ce0-872e-158d4fc3445f.png">
   <img width="300" height="200" src="https://user-images.githubusercontent.com/101147656/158886124-78176f1c-0465-49cd-885c-21412ef1ddcd.png">
</p>

Currently compatible & available RaspberryPi or alternatives with MIPI CSI & HDMI (as of March 17th 2022, will be updated regularly):
  * **OrangePi**: https://orangepi.com/index.php?route=product/product&product_id=864
  * **OrangePi Lite**: https://orangepi.com/index.php?route=product/product&product_id=867
  * **OrangePi PC Plus**: https://orangepi.com/index.php?route=product/product&product_id=866
  * **OrangePi One OP0100**: https://orangepi.com/index.php?route=product/product&product_id=852


**USB night vision camera (left) or MIPI CSI night vision camera (right):**
<p align="center">
    <img width="300" height="300" src="https://user-images.githubusercontent.com/101147656/158514531-b2ebbc28-085f-40c5-bb1c-c21e659364b9.png">
    <img width="300" height="300" src="https://user-images.githubusercontent.com/101147656/158514647-66dade3b-909b-49e4-8694-f2e5add9bd35.png">
</p>


**MicroUSB cable:**
<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158884964-e998b5a5-2105-4a25-9dfb-e5ec3042e121.png">
</p>


**MicroSD card + SD card adapter:**
<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158883405-b925e241-46d4-47e7-b1c6-bf7b07baf2e1.png">
</p>


**SD card reader (if your laptop/PC workstation can not already do this):**
<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158882860-4fc98781-0622-4c70-9b11-31e602b9b749.png">
</p>


### 3.1.2 - Additional Equipment for RaspberryPi4
If using a HDMI monitor (large or small), you will also need a MicroHDMI to HDMI adapter. RaspberryPi4 has no large HDMI connectors, it has only MicroHDMI connectors. If you use a small TFT monitor with ribbon cable and MIPI CSI connector you do not need this.

**MicroHDMI to HDMI adapter:**
<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158884164-add6b11b-5aa0-4107-a479-eb93ab91aee1.png">
</p>



### 3.1.3 - Additional Equipment for RaspberryPi Zero
For the RaspberryPi Zero two more things are needed:

**FFC Flex Cable Adapter for RaspberryPi Zero (from large connector at camera to small connector at RaspberryPi Zero):**
The camera connector of the RaspberryPi Zero is smaller than the one on the standard RaspberryPi. So you need an adapter (not so nice) or one of these adapter cables (smallest & best option!). Choose the orange adapter cable such that it is not too short (>=8cm), you want to have some freedom to adjust the camera.

<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158893551-ca2fff00-51a5-4a46-abc7-ce69f9eb9134.png">
</p>


**OTG adapter (USB-A female to MicroUSB male, just for setup):**
<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158908917-78f4a900-773e-4415-9db5-b3a911c34a21.png">
</p>


**USB hub (just for setup):**
The USB hub will be needed to use both mouse and keyboard via a single MicroUSB port, because the other MicroUSB port of the RaspberryPi Zero will be needed for power. The USB hub can be removed once everything is installed and the Python script for the night vision camera has been set to autostart.
<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158908715-fad497fb-25d9-4579-901d-0b716980db1a.png">
</p>


**MicroHDMI to HDMI adapter:**
If using a HDMI monitor (large or small), you will also need a MicroHDMI to HDMI adapter. RaspberryPi Zero has no large HDMI connectors, it has only MicroHDMI connectors. The RaspberryPi Zero does not have a second MIPI CSI connector, so you really have to have an HDMI adaptor.

<p align="center">
   <img width="200" height="200" src="https://user-images.githubusercontent.com/101147656/158884164-add6b11b-5aa0-4107-a479-eb93ab91aee1.png">
</p>



### 3.2 - Setting up your RaspberryPi
If you know how to do this or it is already set up, you can skip this step. For RaspberryPi derivatives (for example OrangePi) things will work differently.
  * Setup Guide for OrangePi: https://www.instructables.com/Orange-Pi-One-Setup-Guide/

First you have to install your operating system. The standard Raspbian OS is recommended, because most things are already installed. It will sadly not work on the RaspberryPi derivatives (OrangePi etc.), so you have to look up how it works there.


#### 3.2.1 - Install Raspberry Imager
Enter https://www.raspberrypi.com/software/ and download Raspberry Imager for the operating system (OS) you are currently using on your PC. For Windows it will simply be an executable (* .exe), for Ubuntu it will be a * .deb file.

The Ubuntu installation did not work right away for me (with double-clicking), so I will describe some steps I had to take:
  * download Ubuntu version (* .deb file)
  * open terminal and enter: ```sudo dpkg –i filename.deb```
  * some error due missing packages occured
  * install missing dependencies with: ```sudo apt-get install -f```
  * enter again: sudo apt-get install -f
  * everything should be installed now.

You can now open the "Imager" (has a raspberry logo):

<p align="center">
   <img width="500" height="300" src="https://user-images.githubusercontent.com/101147656/158901203-9ad08e7f-12f5-4851-ac7f-4e5a5ef4802b.png">
</p>

Following steps are required:
  * Click "Choose OS" and select "Raspberry Pi OS (32-Bit)"
  * Then **insert an empty SD card (with adapter) into your current PC**, click "Choose Storage" and select your SD card adapter (can be "Generic mass storage")
  * Make sure again that the SD card is empty and no important information are on it. It will be formatted and all data will be deleted in the further process!
  * It is best to configure your password and WiFi connection now via the settings menu (little gear symbol), later it will only get harder. For the WiFi setting you set the SSID to your WiFi network name and enter the password of your WiFi network. WiFi will only be needed during startup when missing Python packages have to be installed, later it is not required anymore.
  * Click "Write" and approve that the SD card wil be formatted and all data will be overwritten
  * Now it will take some time (5min burning, 10min verifying) to burn the OS image on the SD card

After it has finished, put the MicroSD card into the RaspberryPi, RaspberryPi Zero or your alternative and start your system.


#### 3.2.2 - System Configuration
On first startup, you need to configure your region, password and so on.

**Be careful to plug in keyboard, mouse and display from the beginning, the RaspberryPi will only load drivers for the periphery it sees at startup. So when you start your RaspberryPi and plug in mouse or keyboard later, it might happen that it is not working or just after reboot.**

**CAUTION: Once the system has started, the most important thing is that you ENABLE THE CAMERA!**</br>
Enabling the camera can be dne via terminal, just enter ```sudo raspi-config```, select interface options select "(Legacy) Camera Enable" and enable the camera. After this, a **reboot is required** for the changes to become effective.

Now you have to update your package manager:
  * ```sudo apt-get update```
  * ```sudo apt-get upgrade```
  * ```sudo apt-get install -f```
 
After a **reboot**  you can install the required Python modules  and packages (execute this in folder where ```requirements.txt``` can be found, you can find the file in the Github repository):
```pip install requirements.txt```

There might be some problems with OpenCV (and also between OpenCV and Numpy) on the RaspberryPi (Zero). ```opencv-python==4.3.0.38``` and ```numpy==1.22.3``` worked well for me on a RaspberryPi.

You might also run into OpenCV-specific issues. They should be reduced when using a older versionof OpenCV (in the 4.3.x.x range), otherwise you can find some help on the web.

If you have problems setting this up, do not hesitate to contact me!


### 3.3 Software

The software is the same as in [A Stationary Night Vision System Based on PC or Laptop](#a-stationary-night-vision-system-based-on-pc-or-laptop) (2.3 and 2.4), but it is good to put the Python script in autostart, so you do not rely on mouse and keyboard everytime when you switch on the RaspberryPi. The script will just start everytime when you turn on the device.

**Executing the night vision Python srcipt in autostart mode:**</br>
  * On the RaspberryPi (!): access ```/etc/rc.local``` for example with a standard text editor
  * write into ```rc.local```: ```sudo python3 night_vision_flexible.py &``` and save the ```rc.local``` file
  * Reboot the RaspberryPi
  * The video stream should now start automatically after reboot.

More information and other variants on adding a Python script to autostar can be found [here](#https://www.itechfy.com/tech/auto-run-python-program-on-raspberry-pi-startup/).




## 4 - An Autonomously Usable Night Vision System for Mobile Usage

**Budget:   $60...$70**

TBD
TBD
TBD

This autonomously usable night vision system will use a battery pack with a solar cell, so the battery can be reloaded during the daylight and no charging is required. This makes the system independent of available power supplies.

TBD
TBD
TBD

Tutorial how to set up a TFT display for RaspberryPi:
https://tutorial.cytron.io/2019/12/25/getting-started-with-3-5-tft-touch-screen-using-raspberry-pi-4/

TBD
TBD
TBD



## 5 - Multiple Night Vision Nodes Accessible Via Website

TBD



## 6 - Safety Instructions

**Infrared Light:**<br/>
Infrared Radiation might harm your eyesight when continuously exposed. Nothing will happen immediately, but you should avoid staring into the infrared light to avoid long-term damage. Also do not point it directly to an animal or a friendly person nearby. It will not have a meaningful negative immediate effect on hostile animals or persons nearby, so infrared light cannot be used to chase an animal or person away or blind the subject temporarily.


**Visibility / Hearability:**<br/>
As you can see, the infrared light is not completely invisible. You will see red circles in the infrared LEDs. If you point the DIY night-vision gadget outside your window or your shelter, the observed animal or person can maybe see it and identify you as a target. So use carefully (safe distance to device, only look shortly or change positions regularly). You should try not to cover the infrared LEDs, because then night-vision will not work well and the cover material is exposed to heating, which can potentially result in a fire.

Also the camera aperture will make some clicking noise, which might be heard by hostile persons nearby.


**Heat:**<br/>
Infrared radiation develops heat, more than you think. Watch out when touching the infrared LEDs (or the PCB backplate behind them), they can become very hot. Also, do not cover the infrared LEDs with tape, textiles, clothes, … or put it on carpets etc. The materials with contact to the infrared LEDs can start to burn. Same goes for the backplate of the PCB, behind the infrared LEDs. It gets hot!


**Semiconductor Market and Supply Chain:**<br/>
Currently (2021/2022/2023), semiconductor market is under tension with supply chain issues leading to a shortage in semiconductors, processors, ICs, etc. Many products are off the market until late 2022 or even 2023. Not all components might be available at all times, starting with the standard RaspberryPi (v3 or v4). Wherever possible, alternatives will be presented to overcome these organisational obstacles.

If you find other alternatives for any component that are not mentioned here, do not hesitate to make contact, they will be added to the site if appropriate.



## 7 - Ordering and Delivery Hints
When ordering, **always keep the delivery date in mind**! It is no good ordering from Banggood, Amazon (China) or similar, if the goods will be delivered in 1-2 months. Infrared camera modules are available within a couple of days typically!

If it is currently not possible to ship to (your city in) Ukraine, contact persons from Poland, Romania, Slovakia or Hungary living close at the borders, or add the items to the lists when requesting help from other countries. They can maybe order it for you and hand it over at a border. Poland usually allows fast delivery from other European countries. Germany usually also has a short delivery time. Useful contacts for requesting delivery from other countries might be found on:	https://fightforua.org/

If necessary, you can also contact foreign groups or individuals coming to your country or supplying goods to Ukraine. Maybe they can also provide you the materials for the DIY night vision project.

When ordering: Maybe the express option makes sense for you, so that the components arrive some days earlier.



## 8 - Useful RaspberryPi Links
**Installer for RaspberryPi OS (Raspbian):** https://www.raspberrypi.com/software/

**How to setup WiFi on RaspberryPi 3/4/400/Zero:** https://raspberrytips.com/raspberry-pi-wifi-setup/

**How to enable a camera on RaspberryPi and some basics:** https://raspberrytips.com/install-camera-raspberry-pi/
