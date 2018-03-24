import simplegui

# define global variables
counter = 0 	#Represents time in tenths of seconds
x = 0			#Number of watch stopped at .0 seconds
y = 0			#Numbers of tries
stop = True 	#Variable that determines wether the watch is running or stopped

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t//600
    B = (t//100)%6
    C = (t//10)%10
    D = t%10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stop
    timer.start()
    stop = False
    
def stop():
    global counter, stop, x, y
    timer.stop()
    if stop == False:
        y = y + 1
        stop = True
        
        if counter%10 == 0:
            x = x + 1
    
def restart():
    global counter, x, y
    timer.stop()
    counter = 0
    x = 0
    y = 0
    stop = True

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter = counter + 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [90, 170], 50, "White")
    canvas.draw_text(str(x) + "/" + str(y), [230, 40], 40, "Green")
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 300)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Restart", restart, 100)

# start frame
frame.start()
