# Manifest Testing
## Table of contents:
1. [**Testing Overview**](#testing-overview)
1. [**Linter Results**](#manual-tests)
1. [**Manual Tests**](#manual-tests)
    * [***Test & Result***](#planning-overview)
    * [***Testing Feedback***](#planning-overview)
1. [**Know Issues**](#know-issues)
---
### **Testing Overview**

Throughout the project I was learning, coding, and testing as I went along. This was my first experience with python and I've progressed a lot.

- I had 6 other people test my game and I collected their input

In addition to the manual tests I did build test functions.

I did not keep a record of these and few if any were left in any committed code. In future I will store any testing code and the results for reference.

As an example I built a function to generate thousands of passenger objects. The test did pass and it gave me a good idea of how often I was generating medium and high risk passengers.
It also exposed a performance issue once past about 5000 passengers where the loops checking existing passengers really start to slow things down. This was in noway a concern for my game but did open my eyes to performance testing in bigger scale games.

---
### **Linter Results**

All of my files had zero issues reported in CI Linter

![logic Flow](./assets/docs/mainfest_linter.JPG)
![logic Flow](./assets/docs/config_linter.JPG)
![logic Flow](./assets/docs/data_loader_linter.JPG)
![logic Flow](./assets/docs/passenger_creator_linter.JPG)

I'm aware that the CI Linter is forgiving to some things such as line count for example.
I did intend to put more of the functions from manifest.py into the other files since I went over the 1k rec line count but I ran into issues with circular imports and was just running out of time for the cleanup.
I decided to leave the code alone for fear of introducing errors after testing.
PEP8 has been a regular reference point.

---


### **Manual Tests**
#### ***Test & Result***

    1 - Main menu displays correctly  

    Result - PASS
---
    2 - 
    - Tutorial screen triggered by 't' key
    - Displays tutorial text 
    - Progresses to page 2 on key press
    - Returns to main menu after next key press

    Result - PASS
---
    3 - Quit triggered by 'q' key and exits the program

    Result - PASS
---
    4 - New game triggered by 'n' key

    Result - PASS
---
    5 - Game difficulty selection displays and allows selection with keys '1','2', and '3'. Stores selection in global var.
    Selection triggers progression to duration selection

    Result - PASS
---
    6 - Duration selection displays and triggers with keys 1 to 5. Stores result in global var. Initiates main game display.

    Result - PASS
---
    7 -
    - Main game screen draws
    - Timer displays correct countdown and updates each second
    - Shutter 'animation' runs. 
    - Dialog starts. 
    - Implant read sequence runs
    - Implant data displays with correct delay to emulate data transfer
    - Manifest match sequence runs
    - Manifest data has been randomly encrypted and displays with in red with hashes
    - Action 'buttons' display - Quit / Board / Reject / Arrest / Decrypt

    Result - PASS
---
    8 - 
    - Hitting relevant key triggers correct action
    - Q triggers quit game confirm
    - B triggers boarding passenger
    - R triggers rejecting passenger
    - D triggers decryption game
    - not other keys trigger an actions or errors

    Result - PASS
---
    9 - 
    - Q triggers quit confirmation
    - N triggers confirmation closure and play continues
    - Y triggers the game to end and the main menu to display

    Result - PASS
---
    10 - 
    - D triggers decryption game to run
    - New window displays
    - Countdown starts
    - Random fake keys listed with 1 correct key
    - User input only allows valid alpha numeric characters
    - Backspace deletes and enter submits the current pattern
    - Empty input is valid (easy way to skip game)
    - Input limited to current key length and user gets warning
    - Feed displays last entered key
    - Correct characters in green, yellow partial match, red not in string
    -Entering the correct key displays valid key record recovered
    - Use up all 5 chances and failure message displays.
    - Countdown reaches 0 and failure message displays along with timeout message
    - Fail/Win/Countdown expires results in switch back to main game

    Result - PASS
---
    11 - 
    - Decryption game ending results in main game displaying.
    - If gate closure time expires while in mini game show the gate closed message in timer location
    - action buttons redrawn without decrypt option
    - If game was failed then screen remains unchanged
    - If game was won then redraw panel with all data showing

    Result - PASS
---
    12 - 
    - Player can take action to board / reject / arrest any passenger they see fit to
    - Correct dialogs show when action is taken
    - New passenger is loaded if gate still open

    Result - PASS
---
    13 - 
    - Countdown timer shows gate closed when time is up
    - Player get chance to finish handling of last passenger
    - Gate closure message displays and final office dialog
    - Screen cuts to officers personal terminal

    Result - PASS
---
    14 - 
    - Hypno box runs
    - Info message displays
    - Performance message comes up
    - Results reflect players actions
    - Hitting a key takes player back to main menu

    Result - PASS
---
#### ***Testing Feedback***

From the people that were kind enough to test the game they did not have any issues to report.

The main piece of feedback I got was regarding the decryption mini game being too tough. I've tried to balance it better by having shorter keys and less fake keys.

### **Know Issues**

Nothing came from my additional testers but I have logged what I can only guess is 20 or more hours of game time and thats probably grossly underestimating it.

I have observed 1 very rare issue that I was unable to catch or reproduce.

It involves screen corruption with characters that are not even part of the program. No errors or crashes, just a weird character where it shouldn't be.

What I believe is causing this is the way that I'm threading and using curses to write to multiple locations at the same time. This is how the timers were implemented. There seems to be a very rare condition where calls at the exact same time trigger screen corruption.

To remediate I introduced time.sleep() of .1 to points where we trigger draws at the same time.

It's a complex issue and very difficult to debug or find information on as I'm doing something so niche with this game.

My stage 2 remediation, if this application was released publicly and had adoption, would be to revert to full screen draws to include the timer. Stage 3 would be a removal of the countdown entirely and have updates as each new passenger came along.

I felt that the issue was so rare, and quickly corrected in the next refresh of the wider screen area that it was worth leaving in the submitted project as it took me a lot of work to get threading to work (after asyncio was a bust)