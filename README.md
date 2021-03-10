# ISS Assignment 3 
### Game Development using Python and PyGame 
> _Shaurya Rajat Dewan
> 2019101017_

### Read the instructions and try out my game.  


### Gameplay and Rules :  

When you run the game, initially a screen opens up where you must choose the difficulty level you wish to start at and also the player icons for both players by clicking the respective buttons with the mouse. By default, difficulty is set at easy/noob and the player icons are set as a ghost picture.

The game has multiple rounds. 

Player 1 starts at the bottom and has to reach the other end by avoiding all the obstacles in minimum time.  
Player 2 starts at the top of the screen and has to reach the bottom by avoiding all the obstacles and in minimum time.

As the player crosses a stream, he/she is rewarded points according to the number of obstacles in that band, the rules are :–   
+5 for fixed obstacles  
+10 for moving obstacles  

Also, at the end of each round, time taken by the respective player in that round is deducted from their score for that round and saved as the final score for that round.  

The player who survived more rounds wins. However, if both players survived the same number of rounds then the player with the greater score wins the game. If still no winner is decided, then it is declared as a tie.

In the subsquent rounds, the speed as well as number of moving obstacles increases      

### Controls: 

Keyboard `Arrow Keys` to move up, down, left and right for `PLAYER 1`. 
Keyboard `Arrow Keys` to move up, down, left and right for  `PLAYER 2`.     

### How to install : 

1. Download the folder/copy it to your local device. 
1. Install python, pygame, configparser 
	1. Check this link to get them installed on linux – https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/ 
	1. Download PyGame – https://www.pygame.org/download.shtml 
	1. Further help - https://www.pygame.org/wiki/GettingStarted
1. Open the folder in Terminal and run : 
	python3 game.py 
		(OR)
 	python game.py
1. Enjoy the Game.  

For the game development I have used Vim Text Editor

