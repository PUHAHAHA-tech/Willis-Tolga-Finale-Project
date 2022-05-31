
add_library('minim')

def setup():
    #ball variables
    global bx, by, bx_s, by_s
    bx = 400
    by = 300
    bx_s = 10
    by_s= 0
    
    #paddle1 variables
    global P1pos, P2pos, P1s, P2s, Ps
    P1pos = 280
    P2pos = 280
    P1s = 0
    P2s = 0
    Ps= 7
    
    #images
    global start_s, rules_s, end_s
    start_s = loadImage("start_s.PNG")
    rules_s = loadImage("rules_s.PNG")
    end_s = loadImage("end_s.PNG")

    #text font
    impact = createFont("impact.ttf", 64)
    textFont(impact)

    size(800,600)
    start_s.resize(800,600)
    rules_s.resize(800,600)
    end_s.resize(800,600)
    stroke(255)

    #sounds 
    minim = Minim(this)
    global Paddle, Score, Wall
    Paddle = minim.loadFile("Paddle.mp3")
    Score = minim.loadFile("Score.mp3")
    Wall = minim.loadFile("Wall.mp3")

    #Points
    global P1p, P2p, winner
    P1p = 0
    P2p = 0
    winner = 0
    
    #game states
    global start, game, score_pause, win, rules
    start = True
    game = False
    score_pause = False
    win = False
    rules = False
    
    #counter 
    global counter
    counter = 0
    
def draw():
    global start, game, score_pause, win, rules, P1p, P2p, winner, counter
    
    if counter > 0:
        counter -= 1
    if counter == 0 and score_pause == True:
        game = True
        score_pause = False
    
    #for start or instruction screen 
    if start == True:
        image(start_s, 0, 0)
    elif start == False and rules == True:
        image(rules_s, 0, 0)
       
    #for winner 
    if P1p == 5:
        win = True
        game = False
        winner = 1
    elif P2p == 5:
        win = True
        game = False
        winner = 2
    #ending screen
    if win == True:
        game_end()
    if game == True:
        play()
 
def background():
    fill(0)
    rect(0,0,800,600)
    #drawing out the middle line
    for i in range(30):
        fill(255)
        rect(400,0,10,600)
    
def ball():  
    #controlling ball stuff and paddle stuff
    global bx, by, bx_s, by_s, P1pos, P2pos, P1p, P2p, start, game, score_pause, win, rules, counter
    #ball walls collisons
    if (by <= 0 or by >= 590):
        by_s *= -1
    #music
        Wall.play()
        Wall.rewind()
    #ball moving
    bx += bx_s
    by += by_s
    #palyer1 collision
    if (bx <= 50 and bx >= 48):
        for i in range(5):
            #ball length is 10, so we did i times 10
            if (by > P1pos - 10 + i* 10 and by <= P1pos + i * 10):
    #switch direction
                bx_s *= -1
                by_s = -2*(2 - i)
                Paddle.play()
                Paddle.rewind()
    #player2 collision (repeat)
    if (bx >= 740 and bx <= 748):
        for i in range(5):
            if (by > P2pos - 10 + i* 10 and by <= P2pos + i * 10):
    #switch direction
                bx_s *= -1
                by_s= -2*(2 - i)
                Paddle.play()
                Paddle.rewind()
    #if ball leaves the screen
    if bx <= 0:
        bx = 400
        by = 300 
        by_s = 0
        #resets ball position
        P2p += 1
        game = False
        score_pause = True
        Score.play()
        Score.rewind()
        counter = 50
    #repeat for right side
    if bx >= 800:
        bx = 400
        by = 300
        by_s = 0
        P1p += 1
        game = False
        score_pause = True
        Score.play()
        Score.rewind()
        counter = 50
        
    fill(255)
    rect(bx, by, 10, 10)
def play():
    background()
    ball()
    paddle()
    score()

def game_end():
    global winner
    text1 = "Player " + str(winner) + " won"
    image(end_s, 0, 0)
    text(text1, 150, 200)
    text(P1p, 200, 400)
    text(P2p, 600, 400)

def game_pause():
    global counter
    background()
    paddle()
    score()
         
def paddle():
    global P1pos, P2pos, P1s, P2s, Ps
    fill(255)
    P1pos += P1s    
    P2pos += P2s
    rect(50,P1pos,10,40)
    rect(740,P2pos,10,40)
    
    #paddle out of bounds check
    if P1pos >= 580:
        P1pos = -20   
    elif P1pos <= -20:
        P1pos = 580
        
    if P2pos >= 580:
        P2pos = -20   
    elif P2pos <= -20:
        P2pos = 580
    
def score():
    text(P1p, 200, 120)
    text(P2p, 600, 120)
    
def keyPressed():
    global P1pos, P2pos, P1s, P2s, Ps, P1p, P2p, start, game, score_pause, win, rules
    if  (keyCode == UP):
        P2s = -Ps
    elif  (keyCode == DOWN):
        P2s = Ps
    
    if  ((key == 'W') or (key == 'w')):
        P1s = -Ps
    elif  ((key == 'S') or (key == 's')):
        P1s = Ps
        
    if (key == ' ' and win == True):
        win = False
        P1p = 0
        P2p = 0
        start = True
        game = False
        score_pause = False
        rules = False
        
def keyReleased():
    global P1pos, P2pos, P1s, P2s, Ps
    if  (keyCode == UP):
        P2s = 0
    if  (keyCode == DOWN):
        P2s = 0
        
    if  ((key == 'w') or (key == 'W')):
        P1s = 0
    if  ((key == 's') or (key == 'S')):
        P1s = 0
        
def mousePressed():
    global start, game, score_pause, win, rules, counter
    #start
    if (mouseX > 240 and mouseX < 560 and mouseY > 240 and mouseY < 320 and start == True):
        start = False
        score_pause = True 
    
    #rules
    if (mouseX > 220 and mouseX < 580 and mouseY > 340 and mouseY < 420 and start == True):
        start = False
        rules = True
    
    #return
    if (mouseX > 600 and mouseX < 800 and mouseY > 470 and mouseY < 540 and rules == True):
        start = True
        rules = False
