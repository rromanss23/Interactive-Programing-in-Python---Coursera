# Mini-project #6 - Blackjack

import simplegui
import random

# Load background 
BACKGROUND_SIZE = (1000, 500)
BACKGROUND_CENTER = (500, 250)
background = simplegui.load_image("https://dl.dropbox.com/s/6rfapg0bg6k1f4u/detail-custom-blackjack-layout-3.png?dl=0")

# Load title
TITLE_SIZE = (800, 267)
TITLE_CENTER = (800/2, 267/2)
TITLE_SCALE = (800/3, 267/3)
title = simplegui.load_image("https://dl.dropbox.com/s/dwfiaz66hqeu75n/503-2.png?dl=0")

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

PLAYER_CARDS_POSITION = (462, 280)
DEALER_CARDS_POSITION = (462,20)

# Load playing buttons
buttons = simplegui.load_image("https://dl.dropbox.com/s/1m3hn1k7j8vkjrb/Botones%20BJ.png?dl=0")
BUTTONS_SIZE = (120,60)
BUTTONS_CENTER = (60, 30)
IMAGE_SIZE = (121,221)
IMAGE_CENTER = (121/2, 221/2)
IMAGE_SIZE_SCALE = (121/1.75, 221/1.75)

# initialize some useful global variables
in_play = False
outcome = ""
player_score = 0
dealer_score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        s = "hand contains :"
        for i in self.hand:
            s += i.get_suit() + i.get_rank() +" "
        return s

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        hand_value = 0
        has_A = False
        for i in self.hand:
            hand_value += VALUES.get(i.get_rank())
            if i.get_rank() == "A":
                has_A = True
        
        if not has_A:
            return hand_value
        
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            
            else:
                return hand_value
   
    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, (pos[0] + 7*i, pos[1] + 20*i))
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i, j))

    def shuffle(self):
        random.shuffle(self.deck) 
        

    def deal_card(self):
        return self.deck.pop(random.randrange(len(self.deck)))
    
    def __str__(self):
        s = "Deck contains "
        for i in self.deck:
            s += i.get_suit() + i.get_rank() + " "
        return s



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, dealer_score
    
    
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    print ""
    print "Player " + str(player_hand) + ". Value is " +str(player_hand.get_value())
    print "Dealer " + str(dealer_hand) + ". Value is " +str(dealer_hand.get_value())
    
    if in_play:
        dealer_score += 1
    
    in_play = True
    outcome = ""

def hit():
    global outcome, in_play, dealer_score
    
    if player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
        print ""
        print "Player " + str(player_hand) + ". Value is " +str(player_hand.get_value())
        print "Dealer " + str(dealer_hand) + ". Value is " +str(dealer_hand.get_value())
        
        if player_hand.get_value() > 21:
            print "You have busted"
            outcome = "You have busted! Dealer Wins"
            in_play = False
            dealer_score += 1
            
    return                   
       
def stand():
    global outcome, in_play, player_score, dealer_score
    if player_hand.get_value() > 21:
        print "You have busted"
        outcome = "You have busted! Dealer Wins"
        in_play = False
        dealer_score += 1
        
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            print ""
            print "Player " + str(player_hand) + ". Value is " +str(player_hand.get_value())
            print "Dealer " + str(dealer_hand) + ". Value is " +str(dealer_hand.get_value())
        
            
    if dealer_hand.get_value() > 21 or player_hand.get_value() > dealer_hand.get_value() and in_play:
        print "Dealer have busted"
        outcome = "You Win!"
        in_play = False
        player_score += 1
                
    else:
        print "Dealer wins"
        outcome = "Dealer Wins!"
        in_play = False
        dealer_score += 1
        
    
    
                
# draw handler    
def draw(canvas):
    canvas.draw_image(background, BACKGROUND_CENTER, BACKGROUND_SIZE, BACKGROUND_CENTER, BACKGROUND_SIZE)
    canvas.draw_image(buttons, IMAGE_CENTER, IMAGE_SIZE, (630, 390), IMAGE_SIZE_SCALE)
    canvas.draw_image(title, TITLE_CENTER, TITLE_SIZE, (230, 80), TITLE_SCALE)
    player_hand.draw(canvas, PLAYER_CARDS_POSITION)
    dealer_hand.draw(canvas, DEALER_CARDS_POSITION)
    canvas.draw_text(outcome, (600, 150), 30, 'White', 'serif')
    canvas.draw_text("Player's score " + str(player_score), (600, 50), 30, 'White', 'serif')
    canvas.draw_text("Dealer's score " + str(dealer_score), (600, 100), 30, 'White', 'serif')
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (504, 88), CARD_BACK_SIZE)
        
    else: 
        canvas.draw_text('Value '+ str(dealer_hand.get_value()), (435, 200), 40, 'Black', 'serif')
        canvas.draw_text('Value '+ str(player_hand.get_value()), (435, 465), 40, 'Black', 'serif')
        

def click(pos):
    if pos[0] >= 595 and pos[0]<= 664:
        if pos[1] >= 327 and pos[1] <= 361:
            deal()
           
        elif pos[1] >= 373 and pos[1] <= 408:
            stand()
           
        elif pos[1] >= 418 and pos[1] <= 453:
            hit()
    
    return pos
# initialization frame
frame = simplegui.create_frame("Blackjack", 1000, 500)
frame.set_canvas_background("Black")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


# get things rolling
deal()
frame.start()
