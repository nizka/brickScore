import random
class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.y1=640
        self.speed_x = 4#+random.randint(0,2)
        self.speed_y = -4+random.randint(0,2)
        self.sz = 20
        self.active=True
        self.list_life=[10,30,50]
        
    def hit_test(self, posX):            
        if posX <self.pos_x>posX+120  and self.pos_y==602:
            self.active=False
            self.list_life.pop(-1)  
        if posX >self.pos_x<posX+120  and self.pos_y==602:
            self.active=False
            self.list_life.pop(0)
            return(self.list_life)              
    def draw(self):
            fill(242, 31, 12)
            circle(self.pos_x, self.pos_y, self.sz)
            fill(255,255,255)
            circle(self.pos_x-3, self.pos_y, self.sz-13)
 
    def update(self):
                for i in range (len(self.list_life)):
                    fill(255)
                    circle(self.list_life[i],10,17)
                self.pos_x = self.pos_x + self.speed_x
                self.pos_y = self.pos_y + self.speed_y
                if self.pos_x > width - self.sz:
                    self.speed_x *= -1
                if self.pos_x-10 < 0:
                    self.speed_x *= -1
                if self.pos_y > height - self.sz-20:
                    self.speed_y *= -1
                if self.pos_y < 35:
                    self.speed_y *= -1
                if self.active==False and len(self.list_life)==0:                   
                    self.speed_x = 0
                    self.speed_y = 0

                    background(50,10,227)
                    self.y1 =self.y1 - 1
                    if self.y1 < 0:
                       self.y1 = 640
                    textSize(80)
                    strokeWeight(8)
                    textAlign(CENTER)
                    text("GAME OVER", 260,self.y1)
                       
