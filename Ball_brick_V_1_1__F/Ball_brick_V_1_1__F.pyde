import Ball
import Brick
import random
pos_x = 10
pos_y = 590
posX = 0
y=35
x=10
n=0
scr=0
list_x=[]
list_y=[]
key_mode=0
bcolor="cblue2"
active=True
lines_list=[]
def rectangle_gray():
    fill(129,135,128)
    rect(0,20,width,height)
def rectangle_bleu():
    fill(50,10,227)
    rect(10,30,width-20,height)    
def circ():
    fill(219,29,29)
    circle(9, 618,15)
    circle(126,618, 15)
def rectang():
    fill(141, 137, 136)
    rect(10,610,115,15)            
def paddle():
    circ()
    rectang()
def my_score():
      global scr
      textSize(20)
    #strokeWeight(4)
      textAlign(CENTER)
      text("SCORE",130,20)
      fill(0)
      stroke(0)
      rect(180,0,40,20)
      fill(219,29,29)
      text(scr, 200, 20)
#def start_prog():
  #  if len(list_life)>0

def setup():
    global the_ball,x,y,pos_x,pos_y, my_brick, bcolor, active,n        
    size(540,640)
    background(0)
    file=open("layout.txt","r")
    content=file.read()
    file.close()
    lines_list = content
    the_ball = Ball.Ball(pos_x, pos_y)
    my_brick = []
    a=0
    b=0
    for i in range (len(lines_list)):              
            if lines_list[i]=="V":            
                    if active==True:
                        active=True
                        bcolor="cred"
                    else:
                        active=False
            if  lines_list[i]=="R":       
                    if active==True:
                        active=True
                        bcolor="cblue" 
            if  lines_list[i]==" ":
                        active=True
                        bcolor="cblue2"
            if i>0 and i%34==0:            
                    n=n+1
                    y=y+25
                    
            list_x.append(x+15*(i-(34*n)))
            brick = Brick.Brick(list_x[i],y,active,bcolor)
            my_brick.append(brick)
                
    noLoop
    
def draw():
    global the_ball, x, y, my_brick, list_x, list_y, pos_x, pos_y, key_mode,speed_x, posX,scr,lines_list
    rectangle_gray()
    rectangle_bleu()
    y=500
    fill(255,255,227)
    rect(random.randint(10,width-20),random.randint(240,height-20),4,4)
    for j in range(271): 
        my_brick[j].hit_test(the_ball.pos_x, the_ball.pos_y, active)
                    #my_brick[j].score(scr)
        my_brick[j].draw()
        my_score()
    if keyPressed:
        key_mode = 1
    if mousePressed:
        key_mode = 0
    if key_mode:
        if keyPressed:
            if keyCode == RIGHT:
                posX = posX + 5
                if posX > 395:
                    posX = 395
            elif keyCode == LEFT:
                posX = posX - 5
                if posX<10:
                    posX = 10
    else:
        posX = mouseX
        if mouseX<12:
            posX = 12
        elif mouseX > 395:
            posX = 395
    if keyPressed:
        if keyCode == RIGHT:
           posX = posX + 5
        elif keyCode == LEFT:
           posX = posX - 5           
    pushMatrix()
    translate(posX,0)
    paddle()
    popMatrix()
    #fill(219,29,29)
    the_ball.update()
    the_ball.draw()
    the_ball.hit_test(posX)
