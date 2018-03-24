# implementation of card game - Memory

import simplegui
import random

#Creating random dock of 16 cards (8 pairs ofo 2)
deck = range(0, 8)
deck.extend(deck)

exposed = list(deck)

def hide_cards():
    global deck, exposed
    for index in range(len(deck)):
        exposed[index] = False
    

def new_game():
    global i, turn, deck
    turn = 0
    i = 0
    random.shuffle(deck)
    hide_cards()
    label.set_text("Turns = 0")

     
# define event handlers
def mouseclick(pos):
    global i, turn, deck_index0, deck_index1, deck_index2
    
    if i == 0:
        deck_index0 = pos[0]//50
        exposed[deck_index0] = True
        i = 1
        turn = 1
                     
    elif i == 1 and not exposed[pos[0]//50]:
        deck_index1 = (pos[0]//50)
        exposed[deck_index1] = True
        i = 2
            
        
    elif i == 2 and not exposed[pos[0]//50]:
            if deck[deck_index0] != deck[deck_index1]:
                exposed[deck_index0] = False
                exposed[deck_index1] = False               
            
            deck_index0 = pos[0]//50
            exposed[deck_index0] = True
            
            turn +=1
            i = 1
    
    label.set_text("Turns = " + str(turn))            
                                  
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed
    for index in range(len(deck)):
        canvas.draw_text(str(deck[index]), (16 + 50*index, 65), 40, "White")
        if not exposed[index]:
            canvas.draw_polygon([(0 + 50*index, 0), (50 +50*index, 0), (50 + 50*index, 100), (0 + 50*index, 100)], 1, "Red", "Green")


#create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0" )

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
