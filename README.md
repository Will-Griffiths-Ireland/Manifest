
# Manifest
## **Game Overview**

Manifest is a retro, text based, observation game built purely in Python.
You play the role of a spaceship security officer responsible for passenger boarding
​
![Menu](./assets/docs/main_menu.webp)
![Game Screen](./assets/docs/main_game.png)

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

For this project I wanted to emulate an 80's scfi experience.
I explored what would be possible just using python and a terminal being emulated in xterm.js.
I decided to create record matching game with a decryption mini-game inside it

My core aims for the project

* Do as much as possible visually with a text terminal
* Have a static screen-space without scrolling
* 
* Add an element of procedural / random generation
* Provide


### **Target Audiences:**

* People that like puzzle games
* People that like text games
* People that like games with humor

### **User Stories:**

* As a player, I want a game with clear objectives
* As a player, I want simple inputs that provide responses
* As a player, I want an engaging experience


### **Game Aims:**

* The game should, provide a tutorial
* The game should, provide a main menu



### **Wireframes:**

I did produce an initial wireframe but didn't want to commit to a vision when design options would be limited

![Wireframe 1](./assets/docs/wireframe1.JPG)

### **Logic Flow:**

I created a flowchart for the core flow although
​
### **Color Scheme:**

Working in a terminal, which in the case of xterm.js is limited to 8 colors did play a factor in my choices.

Core elements of the interface are green which is a nod to classic green monochrome terminals.
I used white for dialog text and

### **Design Choices**
​
Maximizing the use of screen-space

---
​
## **Game Features**

### **Intro**

The intro screen gives the player a feel for the game. I have a stacking animation that uses 16 random cards and slows down on the final card that is back face up and shows the Memoria logo.

The click to continue button drops in quickly so that a returning player can skip the animation.

#### *Desktop @1080p Example*

![Intro Desktop](./assets/docs/intro1080.webp)

#### *Mobile Example*

![Intro Desktop](./assets/docs/intromobile.webp)



---
## **Testing**

Throughout development I thoroughly tested each piece of code from a core logic perspective and a visual one, before commits.
My approach to testing is to do everything I can, from an end user perspective, to break the application. Always expect the unexpected click!
Please note all testing code & comments were removed from final production code.
The general dev cycle testing procedure was..

## **Defects**

Rigorous testing of my code while I built it paid off when it came to testing the end product.
I don't feel I have any major defects outside of platform specific problems.

I did find a few bugs in my final testing that were not covered by specific tests...

Issue - Player can click on a previously selected cards and trigger game over.
Fix - Removed event listener from card once its click event fires. I was positive I already had this code in there but must have removed it at some stage.

Issue - Theme Beat audio effect was playing over the round well done effect.
Fix - Moved the playback call to when we show the main menu again.

### **Unresolved**

The main outstanding issue is display glitches on MAC/IOS/IpadOS although minor, along with the challenges with playing sounds consistently. If I had hardware to test on more then I'd do more work with the various css webkit extensions that might resolve things.

Recommendation for Apple devices is to leave music disabled.
From my research it's clear the best path is to convert this into an IOS app. The irony that I created the music on an Ipad is not lost on me.


## **Deployment**
I deployed the page on GitHub pages via the following the standard procedure: -
​
1. From the project's [repository](https://github.com/Will-Griffiths-Ireland/Memoria), go to the **Settings** tab.
2. From the left-hand menu, select the **Pages** tab.
3. Under the **Source** section, select the **Main** branch from the drop-down menu and click **Save**.
4. A message will be displayed to indicate a successful deployment to GitHub pages and provide the live link.
​
You can find the live site via the following URL - [live webpage](https://will-griffiths-ireland.github.io/Memoria/)

Deployment to another host is also possible

1. From the project's [repository](https://github.com/Will-Griffiths-Ireland/Memoria), click **Code**.
2. Under the local tab click *Download Zip*.
3. Extract the files and copy them over to a webserver of your choice.

### **To fork the repository on GitHub** 
  
To make a copy of this GitHub repository that allows you to view the content and make changes without affecting the original repository, please take the following steps:
  
1. Login to <b>GitHub</b> and find [this repository](https://github.com/Will-Griffiths-Ireland/Memoria).
2. Locate the <b>Fork</b> button in the top, right hand side of the page.
3. Click on the <b>Fork</b> button to create a copy of the repository in your GitHub account.
4. Enjoy yourself and be creative, I welcome feedback if you have any to give!

---
​
## **Technology and Applications**
​
These are the technologies used for this project.

- HTML5
- CSS3
- Javascript (vanilla)
- MS Powerpoint (cards)
- Balsamiq for wireframes
- Paint.net (Image editing/sizing/compression)
- XnCovert (image resizing)
- Audacity (Sound Editing)
- Garage Band (music Creation)
- Github for version control and deployment
- Gitpod for development
- Google Icons
- https://cssgradient.io/ (gradient code generator)
- https://favicon.io/favicon-generator/ 

----

## **Future-Enhancements**


### **User Enhancements**

* The music needs work :)
* Adding a mode that doesn't use animations at all but still has the mechanics of making the player pause for a second or 2 before selecting cards.
* Multiple saved states in local storage all connected to the username and parsing keys/values for their related settings.
* Augmenting the 'low' quality card image mode with a 'pixel art' setting would be cool but a lot of hands-on crafting.
* Building a full IOS app... 

### **Internal Enhancements**

* Modularize JS into multiple files and use import/export (I know I could have just split the file up and loaded in multiple tags but thats not useful in production environments )
* Refactor code further to reduce size and structure. This was my first JS application and I have learned so much on the journey thats its hard to resist the urge to change things just before submission!

## **Credits**
### **Honorable mentions**
​
Thanks to my mentor Richard who provided valuable input.
Thanks to the multiple talented folks across the globe that put effort into producing tutorials and guides.
Just to name a couple..
- Kevin Powell https://www.youtube.com/@KevinPowell
- developedbyed https://www.youtube.com/@developedbyed

​
### **Content:**
​
The game concept is my original idea. I took some inspiration from a video by developedbyed https://youtu.be/-tlb4tv4mC4 but I really tried to go and do my own thing rather than copy any of his code. 
  
### **Media:**
​
* All images were self created in MS Powerpoint using inbuilt icons
* All sound effects and music were self created using Audacity and Garage Band


