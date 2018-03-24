#RPSLS Mini-Project
#This programs runs random iterations of the popular game 
#Rock,Spock,Paper,Lizard,Scissor

import random 

def name_to_number(name):
    
    if name=="rock":
        number=0
        
    elif name=="Spock":
        number=1
        
    elif name=="paper":
        number=2
        
    elif name=="lizard":
        number=3
    
    elif name=="scissors":
        number=4
        
    else:
        number = "Error. Invalid name"
        
    return number


def number_to_name(number):
    
    if number==0:
        name="rock"
        
    elif number==1:
        name="Spock"
        
    elif number==2:
        name="paper"
        
    elif number==3:
        name="lizard"
        
    elif number==4:
        name="scissors"
        
    else:
        name = "Error. Invalid number"
        
    return name
    

def rpsls(player_choice):
    
    print ""
   
    print "Player chooses " + str(player_choice)
   
    player_number=name_to_number(player_choice)
   
    comp_number=random.randrange(0,5,1)
   
    comp_choice=number_to_name(comp_number)
   
    print "Computer chooses " + str(comp_choice)
   
    modulo  = (player_number - comp_number)%5
   
    if modulo==1 or modulo==2:
        print "Player wins!"
        
    elif modulo==3 or modulo==4:
        print "Computer wins!"
        
    else:
        print "Player and computer tie!"
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
