#GUESS THE NUMBER MINI PROJECT

import simplegui
import random
import math

def new_game(range):
    
    #The function runs a new game each time is called, when
    #the current game is finished or when the range 
    #selected changes
    
    global secret_number #Number to guess randomly generated
    global num_range     #Range of the current game
    global n			 #Number of guesses, they vary from 7 to 10 if the range selected is [0, 100) or [0, 100)
    
    num_range = range
    secret_number = random.randrange(0,num_range)
    n = int(math.ceil(math.log(range+1)/math.log(2))) 
    
    print "New game. Range is from 0 to " + str(range)   
    print "Number of remaining guesses is " + str(n)
    print ""

def range100():
    
    #Event handler called when the range [0, 100) button is clicked
    #Starts a new game
    
    global num_range
    num_range = 100
    print ""
    new_game(num_range)

def range1000():
    
    #Event handler called when the range [0, 1000) button is clicked
    #Starts a new game
    
    global num_range
    num_range = 1000
    print ""
    new_game(num_range)
    
def input_guess(guess):
    
    #Event handler called when a guess is inputed.
    #Checks the numer of remaining guesses and if there
    #are some left, continues with the game.
    
    global n #Number of guesses
    
    n = n -1 #Each guess, decreases the number of remaining guesses
    
    if n>=0:
        print ""
        print "Guess was " + guess 
        print "Number of remaining guesses " + str(n)
         
        player_guess = int(guess)

        if player_guess<secret_number: 
            print "Higher!"
            
        elif player_guess>secret_number:
            print "Lower!"

        else:
            print "Correct!" #When the number is correctly guessed, show it and starts a new game in the same range a the last one
            print ""
            new_game(num_range)
            
            
    else:
        print "" #When there aren´t guesses left, starts a new game in the last range as the last one
        print "You have ran out of guesses. Try a new game"
        print ""
        new_game(num_range)

#Creation of the frame.
frame = simplegui.create_frame("Guess the number", 300,300)

#Creation of the range buttons and the text input.
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
inp = frame.add_input("Enter a Guess", input_guess, 200)

#Starts frame.
frame.start()

#Starts a new game.
new_game(100)


