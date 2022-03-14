# Welcome to the Night Vision Project!

This is a DIY project about the topic "night vision", which can be used to observe animals or other sceneries.

It is more a collection of tutorials how to build such a system. Necessary code will be provided, but is just seen as a component to build the night vision system.

Different tutorials targeting a variety of night vision systems will be uploaded continuously to serve as a starting point for development and adaptation of own night vision systems.



## Contents

1. [Technical Basics of Night Vision](#technical-basics-of-night-vision)
2. [A Stationary Night Vision System Based on PC or Laptop](#a-stationary-night-vision-system-based-on-pc-or-laptop)
3. [A More Flexible Night Vision System Based on RaspberryPi](#a-more-flexible-night-vision-system-based-on-raspberrypi)
4. [An Autonomously Usable Night Vision System for Mobile Usage](#an-autonomously-usable-night-vision-system-for-mobile-usage)
5. [Multiple Night Vision Systems Accessible Via Website](#multiple-night-vision-systems-accessible-via-website)



## Technical Basics of Night Vision

<p align="center">
    <img width="400" height="400" src="https://user-images.githubusercontent.com/101147656/158277081-7132d559-cd76-4878-a340-4fadb5897f2c.jpeg">
</p>

Most cheap night vision cameras are simple optical cameras with a switchable IR cut filter. The IR cut filter typically filters out infrared (IR) light during daytime, leaving only (humanly) visible light for observation, which preserves "natural" colors for the human eye.

At night (or low illumination), this IR cut filter is switched off. The infrared light then is visible, resulting in more visible features during the night.

When the IR cut filter is switched on or off, you usually hear a clicking noise. You hear the clicking noise because the IR cut filter is a mechanical shutter that blocks or passes infrared light. This might be a valuable information if you are in environments with varying light conditions and do not want to be heard, e.g. by a shy animal in the forest or inside a abandoned house.

**To avoid the clicking noise** and be noiseless in varying light conditions, you need to understand the circuit behind a little better:

The decision "IR cut filter on/off" is usually depending on a comparator circuit using a photoresistor (see image above, red circles). Photoresistors are more conductive when illuminated, so they have a high resistance in darkness and a low resistance in light. The comparator circuit detects when the resistance of the photoresistor rises above the (fixed) value of another (standard) resistor, resulting in a signal to turn the IR cut filter off in darkness or low light. Vice versa, the IR cut filter is switched on when the resistance of the photoresistor drops below the other resistor value again in a bright surrounding.

<p align="center">
    <img width="300" height="200" src="https://user-images.githubusercontent.com/101147656/158277406-b5c0aac5-0a20-4165-96b5-584a56d373bb.jpeg">
</p>

If you now replace the photoresistor with a high resistor value (R=1MΩ for example, see image above), it will seem to the comparator circuit like the photoresistor is always in the dark. Then the IR cut filter will always be off, and you will always have a "night vision" display. You can look at it when you need it and ignore it when you are in the light, but **you will hear no clicking, so you are less noisy**...also works with putting a tape over the photoresistor ;)

If you want, you can also make the IR cut filter switchable via software. You need to use the GPIOs of a RaspberryPi in this case (when you use a RaspberryPi as computing gadget).



## A Stationary Night Vision System Based on PC or Laptop

The simplest (but also least flexible) way to build a night vision system is based on a PC (workstation) or laptop. Because you have a power supply and a computing gadget, you will only need a camera that supports night vision.

TBD



## A More Flexible Night Vision System Based on RaspberryPi
TBD



## An Autonomously Usable Night Vision System for Mobile Usage
TBD



## Multiple Night Vision Systems Accessible Via Website
TBD


