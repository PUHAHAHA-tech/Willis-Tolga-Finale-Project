add_library('minim')
Paddle = None
Score = None
Wall = None

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
    global menuImg, instructionsImg, endImg
    menuImg = loadImage("start_s.PNG")
    instructionsImg = loadImage("instructions.PNG")
    endImg = loadImage("End_S.PNG")

    #text font
    Impact= createFont("impact.ttf", 64)
    textFont(Impact)

    size(800,600)
    stroke(255)

    #sounds 
    minim = Minim(this)
    global Paddle, Score, Wall
    Paddle = minim.loadSample("Paddle.mp3")
    Score = minim.loadSample("Score.mp3")
    Wall = minim.loadSample("Wall.mp3")

    #Points
    global P1p, P2p, winner
    P1p = 0
    P2p = 0
    winner = 0
    
    #game states
    global menu, playing, score_pause, win, instructions
    menu = True
    playing = False
    score_pause = False
    win = False
    instructions = False
    
    #counter 
    global counter
    counter = 0
