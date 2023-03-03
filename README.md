
# Manifest
## **Game Overview**

Manifest is a retro, text based, observation and decryption game built purely in Python that runs in an emaulated terminal(xterm.js) and is deployed via Heroku.

You play the role of a spaceship security officer responsible for passenger boarding during a security breach of the ships systems.
​
![Menu](./assets/docs/main_menu.webp)
![Game Screen](./assets/docs/main_game.webp)

#### [The deployed website is here on Heroku](https://manifest.herokuapp.com/)​

## Table of contents:
1. [**Game Overview**](#game-overview)
1. [**Planning stage**](#planning-stage)
    * [***Planning Overview***](#planning-overview)
    * [***User Stories***](#user-stories)
    * [***Game Aims***](#game-aims)
    * [***Wireframes***](#wireframes)
    * [***Logic Flow***](#wireframes)
    * [***Color Scheme***](#color-scheme)
    * [***Design Choices***](#design-choices)
1. [**Game Features**](#game-features)
    * [***Logo & Main Menu***](#logo-mainmenue)
    * [***Tutorial***](#tutorial)
    * [***Security Terminal & Timer***](#security-terminal)
    * [***Shuttering Raises***](#shuttering-raises)
    * [***Dialog Area***](#dialog-area)
    * [***Passenger Implant Data Panel***](#passenger-implant-data-panel)
    * [***Ship Manifest Data Panel***](#ship-manifest-data-panel)
    * [***Action Buttons***](#action-buttons)
    * [***Gate Closure***](#gate-closure)
    * [***Performance Summary***](#perfomrance-summary)
1. [**Testing**](#testing)
    * [***linter***](#linter)
1. [**Deployment**](#deployment)
1. [**Technology and Applications**](#technology-and-applications)
1. [**Future-Enhancements**](#future-enhancements)
    * [***User Enhancements***](#user_enhacements)
    * [***Internal Enhancements***](#internal_enhacements)
1. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**Content**](#content)
    * [**Media**](#media)

---


## **Planning Stage**

### **Planning Overview:**

For this project I wanted to emulate an 80's sci-fi experience.
I explored what would be possible just using python and a terminal being emulated in xterm.js.
I decided to create record matching game with a decryption mini-game inside it that had elements of a text adventure in the mix.

My core aims for the project

* Do as much as possible visually with a text terminal
* Provide a fluid experience 
* Have a static screen-space without scrolling
* Include dialog as a nod to classic text adventure games
* Add an element of procedural / random generation of content
* Provide a fun challenge with rewards
* Limit users text entry
* Generate a feeling of pressure and being 'against the clock'


### **Target Audiences:**

* People that like puzzle games
* People that like text games
* People that like games with humor
* People that like Python 
* People that like retro sci-fi

### **User Stories:**

* As a player, I want a game with clear objectives
* As a player, I want simple inputs that provide responses
* As a player, I want an engaging experience
* As a player, I want to know how to play
* As a player, I want see a score / result


### **Game Aims:**

* The game should, provide a tutorial
* The game should, provide a main menu
* The game should, provide difficulty settings


---

### **Wireframes:**

I produced an initial wireframe but didn't want to commit to a complex vision when design options would be limited in a terminal. My game grew from that

![Wireframe 1](./assets/docs/wireframe.JPG)

---

### **Logic Flow:**

I built out the high level logic flow in draw.io.

![logic Flow](./assets/docs/manifest_flow.jpg)

---
​
### **Color Scheme:**

Working in a terminal, which in the case of xterm.js is limited to 8 colors did play a factor in my choices. Luckily I had the main colours I wanted for the game.

- Core elements of the interface are green which is a nod to classic green monochrome terminals.
I used white for dialog text and most of the fields with changing data.

- Yellow is used occasionally for a bit of variation and to emulate system interactions such as the scanner reading an implant.

- Red is used for encrypted fields and arrest dialog.

- Blue is used in the decryption game system to separate it from the core game.

- Magenta is used in the employee terminal and performance summary section

### **Design Choices**
​
Maximizing the use of screen-space was important in the overall design of the game.

I felt it was essential to have a very static layout for as much of the game area as possible so that the changing game elements would be challenging but not frustrating to spot.

A somewhat dystopian aesthetic is threaded through the dialog interactions but with a edge towards dark humor.


#### **Defensive Design**

An important element of any program is defending from user generated issues. Any time we get input from a user we are exposed.

From the outset a decided to limit user input as much as I could.

- I capture key press events in loops and then check for valid keys in relation to player actions.
- I clear input buffers to avoid unintended progression.
- I built a function to take input from the user during the decryption game which only allows specific keys and warns the user about invalid key presses

---
​
## **Game Features**

### ***Logo & Main Menu***

For the logo I wanted to simulate a type of digital distortion fade that was connected with the games core story point of a hackers

- The manifest logo is built up from a file read into a list
- A random red green or blue colour is picked for each character on each pass
- The logo is then drawn to screen in multiple passes
- A partial trail is left based on the last line of characters drawn
- The logo transitions up the screen
- The number of blanks is reduced as the logo moves up.
- The final pass draws the logo fully to screen

The menu items are selected with the relevant key
- Contrasting colours for the starting letter indicate the relate key to press

After the first load of the game the animation time is changed for the main menu so that latter calls load it quickly

#### *Example*

![logo](./assets/docs/logo.gif)

---

### **Tutorial**

The tutorial section explains the setup for the game and the core objective.

I did have plans to build an interactive tutorial that would be part of the game but time constraints did not allow for this and its a possible future enhancement.

---

### **Security Terminal & Timer**

* The terminal and window structure used throughout the game is drawn with a function I built that allows me to specify a 'window' with starting position, dimensions, and fill style
* I tried to maximize the use of screen space and it was a deliberate design choice to have it packed with data to analyze 

![logo](./assets/docs/timer.gif)

The timer was difficult to implement since I wanted to avoid full refreshes of the entire terminal.
* I used the threading library to display a countdown that is constantly updating
* I had to use global fags to hide the gate closure timer during the decryption game
* The purpose is to remind the player they are against a clock.
* The time shifts to yellow and then red once it reaches certain percentage thresholds

---
### **Shuttering Raises**

At the start of each run the shuttering on the security hatch raises.
Its just another little touch that adds to the immersion of the game.
This only displays before the first passenger.

![logo](./assets/docs/shuttering.gif)

---
### **Dialog Area**

- The dialog area displays passenger comments / actions / mood and the security officers (your) comments / actions / mood
- The aim was to add some richness and comedy to the game but they also connect to the core mechanic of catching out the infiltrators.
- Random selection of randomly shuffled lines in lists leads to some interesting interactions
- The passengers that get generated as the hackers have some custom dialog that points towards their guilt

![logo](./assets/docs/dialog.webp)

---
### **Passenger Implant Data Panel**

The core part of the game is checking the passengers implant chip which acts as a digital passport and boarding pass.
The policy is simple. It has to match the ships stored data in the manifest or they don't get on.

- Their is a passenger class that generates random passengers and their details
- Fields that are alpha numeric strings are randomly generated when the passenger is but the function checks the existing passenger list for any passenger that already had the number/key generated for them.

---
### **Ship Manifest Data Panel**

---
### **Action Buttons**

---
### **Gate Closure**

---
### **Performance Summary**

---
---
## **Testing**

Testing documentation is [here](./TESTING.md)

## **Deployment**
I deployed the page on GitHub pages via the following the standard procedure: -
​
1. From the project's [repository](https://github.com/Will-Griffiths-Ireland/Manifest), go to the **Settings** tab.
2. From the left-hand menu, select the **Pages** tab.
3. Under the **Source** section, select the **Main** branch from the drop-down menu and click **Save**.
4. A message will be displayed to indicate a successful deployment to GitHub pages and provide the live link.
​

Deployment to another host is also possible

1. From the project's [repository](https://github.com/Will-Griffiths-Ireland/Manifest), click **Code**.
2. Under the local tab click *Download Zip*.
3. Extract the files and copy them over to a webserver of your choice.

### **To fork the repository on GitHub** 
  
To make a copy of this GitHub repository that allows you to view the content and make changes without affecting the original repository, please take the following steps:
  
1. Login to <b>GitHub</b> and find [this repository](https://github.com/Will-Griffiths-Ireland/Manifest).
2. Locate the <b>Fork</b> button in the top, right hand side of the page.
3. Click on the <b>Fork</b> button to create a copy of the repository in your GitHub account.
4. Enjoy yourself and be creative, I welcome feedback if you have any to give!

---
​
## **Technology and Applications**
​
These are the technologies used for this project.

- Python
- Python - [Curses Lib](https://docs.python.org/3/howto/curses.html)
- Gitpod
- Github
- Heroku

----

## **Future-Enhancements**


### **User Enhancements**

* decrypt game uses letters as identifiers so the player just hits the relevant key
* enhance dialog and add player interaction / qustioniung
* Build interactive tutorial that runs with game

### **Internal Enhancements**

* Upgrade from WILLTxtDB to a better method of storing data :)
* Refactor code to be shorter and cleaner

## **Credits**
### **Honorable mentions**
​
Thanks to my mentor Richard who provided valuable input as always

​
### **Content:**
​
I created all the content for the game myself. Inspiration for this game was taken from the game [Papers Please](https://en.wikipedia.org/wiki/Papers,_Please)​by Lucas Pope
  
### **Media:**
​
* The manifest logo was created with https://manytools.org/hacker-tools/ascii-banner/


