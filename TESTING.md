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



---


### **Manual Tests**
#### ***Test & Result***

    1 - Main menu displays correctly  

    Result - PASS

---
    2 - Main menu key selection and progression works  

    Result - PASS
---
    3 - Main menu key selection and progression works  

    Result - PASS
---
    4 - Tutorial screen displays tutorial text, progresses to page 2 on key press and then returns to main menu after next key press

    Result - PASS