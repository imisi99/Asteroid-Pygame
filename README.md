# Asteroid-Pygame
This is a basic space shooting game built using pygame and pyinstaller.  
It is an endless game which main objective is for the player to have fun.   
What the game entails:
 - The game can be played by using a mouse or touchpad only
 - Players can move the spaceship anywhere on the screen to avoid the incoming meteors
 - The game is played by moving around with the aid of a mouse and trying to shoot meteors while avoiding them 
 - There is a total of 5 life for a player in the beginning of the game but this can go up or down: 
   - If the spaceship comes in contact with a meteor there is a single life deduction
   - If a meteor successfully passes the spaceship and goes through the bottom of the screen there is a single life deduction
   - If a bomb comes in contact with the spaceship then there is a double life deduction
   - If a player manages to shoot a single heart that comes randomly then a life is added to the player
 - Throughout the event of the game a player cannot have more than 5 life
    -    
 - If a player manages to shoot a fuel tank then for a finite time there is an automated rapid laser shooting
 - Once a plyer life is below zero then it is game-over for the player and the player can do the following:
   - Press the t button to restart the game
   - Press the q button to quit the game    
    

The game has been made into an executable file using pyinstaller therefore there is no need for any package installation to run the game, It can be downloaded [here]().    
Here is the installation Process:
 - Navigate to the main folder and then

To run the game on your terminal however you would run have to clone the [repo]() and run this command on your terminal:
 -      pip intall requirements.txt
 -      python main.py

It was fun creating the game and I hope you enjoy it if you can star the repository and check out this [one]().