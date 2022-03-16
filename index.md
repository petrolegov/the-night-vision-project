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
6. [Safety Instructions](#safety-instructions)
7. [Ordering and Delivery Hints](#ordering-and-delivery-hints)



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


<br/>

**PLEASE ALWAYS CONSIDER THE [SAFETY INSTRUCTIONS](#safety-instructions) FOR INFRARED LIGTH, VISIBILITY BY OTHERS, SIGNIFICANT HEAT DEVELOPMENT AND ORDERING ISSUES!**

<br/>


## A Stationary Night Vision System Based on PC or Laptop

The simplest (but also least flexible) way to build a night vision system is based on a PC (workstation) or laptop. Because you already have a power supply and a computing gadget, you will only need a camera that supports night vision (for example a cheap camera with switchable IR cut filter, see the two images below).

<p align="center">
    <img width="300" height="300" src="https://user-images.githubusercontent.com/101147656/158514531-b2ebbc28-085f-40c5-bb1c-c21e659364b9.png">
    <img width="300" height="300" src="https://user-images.githubusercontent.com/101147656/158514647-66dade3b-909b-49e4-8694-f2e5add9bd35.png">
</p>





## A More Flexible Night Vision System Based on RaspberryPi
TBD



## An Autonomously Usable Night Vision System for Mobile Usage
TBD



## Multiple Night Vision Systems Accessible Via Website
TBD



## Safety Instructions

**Infrared Light:**<br/>
Infrared Radiation might harm your eyesight when continuously exposed. Nothing will happen immediately, but you should avoid staring into the infrared light to avoid long-term damage. Also do not point it directly to an animal or a friendly person nearby. It will not have a meaningful negative immediate effect on hostile animals or persons nearby, so infrared light cannot be used to chase an animal or person away or blind the subject temporarily.

**Visibility / Hearability:**<br/>
As you can see, the infrared light is not completely invisible. You will see red circles in the infrared LEDs. If you point the DIY night-vision gadget outside your window or your shelter, the observed animal or person can maybe see it and identify you as a target. So use carefully (safe distance to device, only look shortly or change positions regularly). You should try not to cover the infrared LEDs, because then night-vision will not work well and the cover material is exposed to heating, which can potentially result in a fire.

Also the camera aperture will make some clicking noise, which might be heard by hostile persons nearby.

**Heat:**<br/>
Infrared radiation develops heat, more than you think. Watch out when touching the infrared LEDs (or the PCB backplate behind them), they can become very hot. Also, do not cover the infrared LEDs with tape, textiles, clothes, … or put it on carpets etc. The materials with contact to the infrared LEDs can start to burn. Same goes for the backplate of the PCB, behind the infrared LEDs. It gets hot!

**Confidentiality, Semiconductor Market and Supply Chain:**<br/>
Currently (2021/2022/2023), semiconductor market is under tension with supply chain issues leading to a shortage in semiconductors, processors, ICs, etc. Many products are off the market until late 2022 or even 2023. Not all components might be available at all times, starting with the standard RaspberryPi (v3 or v4). Wherever possible, alternatives will be presented to overcome these organisational obstacles.

If you find other alternatives for any component that are not mentioned here, do not hesitate to make contact, they will be added to the site if appropriate.



## Ordering and Delivery Hints
When ordering, **always keep the delivery date in mind**! It is no good ordering from Banggood, Amazon (China) or similar, if the goods will be delivered in 1-2 months. Infrared camera modules are available within a couple of days typically!  
If it is currently not possible to ship to (your city in) Ukraine, contact persons from Poland, Romania, Slovakia or Hungary living close at the borders, or add the items to the lists when requesting help from other countries. They can maybe order it for you and hand it over at a border. Poland usually allows fast delivery from other European countries. Germany usually also has a short delivery time. Useful contacts for requesting delivery from other countries might be found on:	https://fightforua.org/  
If necessary, you can also contact foreign groups or individuals coming to your country or supplying goods to Ukraine. Maybe they can also provide you the materials for the DIY night vision project.  
When ordering: Maybe the express option makes sense for you, so that the components arrive some days earlier.

