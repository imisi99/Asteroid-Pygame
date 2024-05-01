# Asteroid-Pygame
This is a basic space shooting game built using pygame and pyinstaller.  
It is an endless game which it's main objective is for the player to have fun.      
The project has two forms which are [pygame only]() and [pygame with class]()   
There is very little difference between the two projects, it's just that the one with classes is more efficient and some certain methods were allowed for better game experience which isn't quite noticeable.   
What the game entails:
 - The game can be played by using a mouse or touchpad only
 - Players can move the spaceship anywhere on the screen to avoid the incoming meteors
 - The game is played by moving around with the aid of a mouse and trying to shoot meteors while avoiding them 
 - There is a total of 5 life for a player in the beginning of the game but this can go up or down: 
   - If the spaceship comes in contact with a meteor there is a single life deduction
   - If a meteor successfully passes the spaceship and goes through the bottom of the screen there is a single life deduction
   - If a bomb comes in contact with the spaceship then there is a double life deduction
   - If a player manages to come in contact with a single heart that comes randomly then a life is added to the player
 - Throughout the event of the game the player can have a max of five life only
    -    
 - If a player manages to come in contact with a fuel tank then for a finite amount of time there is an automated rapid laser shooting
 - Once a plyer life is below zero then it is game-over for the player and the player can do the following:
   - Press the p button to restart the game
   - Press the q button to quit the game    
    

The game has been made into an executable file using pyinstaller therefore there is no need for any package installation to run the game, It can be downloaded [here]() or [here]().    
Here is the installation Process:
 - You can clone any of these [pygame without class]() or [pygame with class]()
 - Once you have cloned the folder you can run the game by clicking on the executable file main.exe
 - Alternatively you can create a shortcut of the executable file and place it on your desktop for easy access

To run the game on your terminal however you would have to clone this [repo]() or this [one with class]() and run this command on your terminal:
 -      pip intall requirements.txt
 -      python main.py

It was fun creating the game and I hope you enjoy it if you did, you can star the repository and check out this [one](https://github.com/imisi99/OOP).