
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
    * [***Main Menu***](#main-menu)
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

Core elements of the interface are green which is a nod to classic green monochrome terminals.
I used white for dialog text and most of the fields with changing data.

Yellow is used occasionally for a bit of variation and to emulate system interactions such as the scanner reading an implant.

Red is used for encrypted fields and arrest dialog.

Blue is used in the decryption game system to separate it from the core game.

### **Design Choices**
​
Maximizing the use of screen-space

#### **Defensive Design**

An important element of any program is defending from user generated issues. Any time we get input from a user we are exposed.

From the outset a decided to limit user input as much as I could.
I capture key press events in loops and then check for valid keys in relation to player actions.

I clear input buffers to avoid unintended progression.

I built a function to take input from the user during the decryption



---
​
## **Game Features**

### **Main Menu**

The main menu builds the games logo up from a file and randomly uses 3

#### *Desktop @1080p Example*

![Intro Desktop](./assets/docs/intro1080.webp)

#### *Mobile Example*

![Intro Desktop](./assets/docs/intromobile.webp)



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

### **Internal Enhancements**

* Upgrade from WILLTxtDB to a better method of storing data :)

## **Credits**
### **Honorable mentions**
​
Thanks to my mentor Richard who provided valuable input as always

​
### **Content:**
​
I created all the content for the game myself. Inspiration for this game was taken from the game [Papers Please](https://en.wikipedia.org/wiki/Papers,_Please)​ by Lucas Pope
  
### **Media:**
​
* The manifest logo was created with https://manytools.org/hacker-tools/ascii-banner/


