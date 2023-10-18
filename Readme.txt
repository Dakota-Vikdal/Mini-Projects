# Choose_your_own_adventure
This is a simple coding challenge. It's really meant just for fun. Essentially you'll need to nest a bunch of conditionals 
and depending upon the players answers they will be sent down a different path. Loads of if statements and of course an input 
statement so we can grab the name of the traveler.


# number_guesser
In this script we first import random because we want the computer to randomly choose a number. Next we write an if
statement that makes sure the users input is a number and between 1 and 10. Then we use the random module to create 
a random number between 0 and the number the user chose. Lastly, we write out a while statement that changes the users 
guessed number into an integer, it then tells the user whether they guessed the number correctly or if they guessed too 
high or too low, it then gives them another chance to guess. At the end the user is shown how many guesses it took them 
to come to the correct answer.


# quiz_game
First the player is asked if they wish to play a game. If they answer anything but yes then the game will end. If they answer yes
then they are given information on how the game works and subsequently asked a question. If they get the question correct then they 
recieve a 'You are correct!' statement, if incorrect, 'Incorrect'. They are then asked the next question and so on until they answer all
6 questions. At the end they are told their score out of 10, some questions are worth more than others.