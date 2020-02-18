class Brick:
  def __init__(self, x, y, active,bcolor):
    self.x=x
    self.y=y
    self.active = True
    self.c_active = active
    self.bcolor = bcolor
    self.scr=0
    
        
  def hit_test(self, x, y,scr):
    if self.x < x < self.x + 520/34 and self.y < y < self.y + 25:
        self.active=False
    if self.bcolor=="cred" and self.active==False:
                self.scr=self.scr+100
    if self.bcolor=="cblue" and self.active==False:
                self.scr=self.scr+200

  def checkColor(self):
    if self.active == True:
        if self.bcolor == "cred":
            fill(219,29,29)
        if self.bcolor == "cblue":
            fill(7, 238, 242)
        if self.bcolor=="cblue2":
            stroke(50,10,227)            
            fill(50,10,227)
        
    if self.active==False:
            stroke(50,10,227)            
            fill(50,10,227)
  def draw(self):
    if self.active==True:
        stroke(0)
        fill(219,29,29)
        self.checkColor()
        rect(self.x,self.y,(width-20)/40,15)
    else:
        
        stroke(50,10,227)            
        fill(50,10,227)
        rect(self.x,self.y,(width-20)/60,15)
        
           
