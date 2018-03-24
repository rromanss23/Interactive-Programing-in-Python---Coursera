# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [1, 1]
ball_direction = RIGHT
ball_pos = [WIDTH/2, HEIGHT/2]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
PAD_VEL = 10
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, ball_direction
    
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    ball_vel[0] = random.randrange(1, 8)
    ball_vel[1] = random.randrange(1, 8)
    
    ball_direction = direction
       

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2 
    
    score1 = 0
    score2 = 0
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    
    
    spawn_ball(RIGHT)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global direction
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_direction == RIGHT:
        ball_pos[0] += ball_vel[0]
        ball_pos[1] -= ball_vel[1]
        
    else:
        ball_pos[0] -= ball_vel[0]
        ball_pos[1] -= ball_vel[1]
    
    if HEIGHT <= ball_pos[1] + BALL_RADIUS or BALL_RADIUS >= ball_pos[1]:
        ball_vel[1] = - ball_vel[1]
        
        
    if WIDTH - PAD_WIDTH <= ball_pos[0] + BALL_RADIUS: 
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT - 10) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT + 10):
            ball_vel[0] = - 1.1*ball_vel[0]
        
        else:
            if score1 < 9:
                score1 += 1 
                spawn_ball(LEFT)
        
            else:
                new_game()
        
    if BALL_RADIUS >= ball_pos[0] - PAD_WIDTH:
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT -10) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT + 10):
            ball_vel[0] = - 1.1*ball_vel[0]
            
        else:
            if score2 < 9:
                score2 += 1
                spawn_ball(RIGHT)
            
            else:
                new_game()
            
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]], 1, 'White', "White") #paddle1
    canvas.draw_polygon([[WIDTH - HALF_PAD_WIDTH-3, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH-3, paddle2_pos + HALF_PAD_HEIGHT]], 2, "White", "White")
    # determine whether paddle and ball collide     
    
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [230, 100], 40, "White")
    canvas.draw_text(str(score2), [350, 100], 40, "White")    

    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, PAD_VEL
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= PAD_VEL
        
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += PAD_VEL
        
    if key == simplegui.KEY_MAP["w"] and paddle1_pos > HALF_PAD_HEIGHT:
        paddle1_vel -= PAD_VEL
        
    if key == simplegui.KEY_MAP["s"] and paddle1_pos < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_vel += PAD_VEL
        
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]: 
        paddle2_vel = 0
        
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

def restart():
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button("Restart Game", restart, 100)
label1 = frame.add_label("The first one that reaches 10 goals wins!")
labels = frame.add_label("")
label2 = frame.add_label("Player 1:")
label3 = frame.add_label("W - Paddle up")
label4 = frame.add_label("S - Paddle down")
labels = frame.add_label("")
label6 = frame.add_label("Player 2:")
label7 = frame.add_label("Up arrow - Paddle up")
label8 = frame.add_label("Down arrow - Paddle down")


# start frame
new_game()
frame.start()
