# Project 2 - Random Password Generator

This is a command-line (CLI) Python application that generates secure, random passwords based on user-selected difficulty level.


## Features:

1. User specifies the desired password length.  
2. Three difficulty levels:
  - Weak → only letters (a–z, A–Z)
  - Medium → letters + numbers
  - Strong → letters + numbers + symbols  
3. Checks minimum length per level (weak ≥ 3, medium ≥ 6, strong ≥ 8).  
4. Automatically copies the generated password to clipboard.


## How to Use:

1. Install required library (if not already installed).
2. Run the script in terminal.
3. Follow the prompts:
  - Enter password length (number).
  - Select difficulty level (weak, medium, strong).
4. The generated password will be displayed.
5. This password automatically copied to clipboard.



## Notes:------

* If you enter an invalid level or too short a length, the program will show an error.
* You can paste the copied password anywhere using Ctrl+V.


