import pygame
pygame.init()
#variable initialise 
run=True 
#colour
black=(0,0,0)
white=(255,255,255)
grey=(176,190,197)
red=(191,54,12)
blue=(101,31,255)
yellow=(255,235,59)
green=(58,142,60)
light_orange=(251,140,0)
light_blue=(63,81,181)
butn_back_colour=(0,121,107)
gravity=1
class player:
    def __init__(self):
        #game character position and other capabilities 
        self.x=150
        self.y=750
        self.height=100
        self.width=100
        self.speed=20
        self.jump_vel=20
        self.is_jumping=False 
        self.left=False 
        self.right=False
        self.walkcount=0
        self.left_direction=False 
        self.right_direction=False   
        self.hitbox=(self.x+10,self.y+5,80,80)
        self.health=200
    def draw(self,win):
        if naruto.health>0:
            self.game_over_played=False
            if self.walkcount>5: 
                self.walkcount=0
                self.left=False 
                self.right=False 
            if self.left and not self.is_jumping:
                win.blit(walkleft[self.walkcount//2],(self.x,self.y))
                self.walkcount+=1
            elif self.right and not self.is_jumping:
                win.blit(walkright[self.walkcount//2],(self.x,self.y))
                self.walkcount+=1
            elif self.left_direction and self.is_jumping:
                win.blit(jump_left,(self.x,self.y))
            elif self.right_direction and self.is_jumping:
                win.blit(jump_right,(self.x,self.y))
            elif self.is_jumping and not self.left_direction and not self.right_direction:
                win.blit(jump_right,(self.x,self.y))
            elif not self.is_jumping and not self.left_direction and not self.right_direction:
                win.blit(stand,(self.x,self.y))
            elif self.left_direction and not self.is_jumping and not self.left and not self.right :
                win.blit(walkleft[2],(self.x,self.y))
            elif self.right_direction and not self.is_jumping and not self.left and not self.right :
                win.blit(walkright[2],(self.x,self.y))
        else:
                win.blit(pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/Nd.png'),(self.x,self.y))
                win.blit(GOF.render('GAME OVER',True,light_blue),(160,550))
                if not self.game_over_played:
                    pygame.mixer.music.stop()
                    game_over.play()
                    self.game_over_played=True 
        self.hitbox=(self.x+10,self.y+5,80,80)
        #pygame.draw.rect(win,(red),self.hitbox,4)
        Nbar2=pygame.draw.rect(win,red,(230,390,200,20))
        Nbar1=pygame.draw.rect(win,yellow,(225,395,self.health,10))
        win.blit(Nh,(150,355))
    def hit(self):
        self.health-=5
class weapon:
    def __init__(self,x,y,direction):
        self.x=x
        self.y=y
        self.height=40
        self.width=40
        self.direction=direction
        self.speed=20
        self.hitbox=(self.x,self.y,self.height,self.width)
    def draw(self,win):
        win.blit(pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/shur.png'),(self.x,self.y))
        self.hitbox=(self.x,self.y,self.height,self.width)
        #pygame.draw.rect(win,(red),self.hitbox,4)
        
class enemy:
    walkleft=[pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/SL2.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/SL3.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/SL1.png')]
    walkright=[pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/SR2.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/SR3.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/SR1.png')]
    dead=pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/Sd.png')
    def __init__(self):
        self.x=750
        self.y=750
        self.height=100
        self.width=100
        self.initial_speed=10
        self.speed=10
        self.end=150
        self.path=[self.x,self.end]
        self.walkcount=0
        self.hitbox=(self.x+10,self.y+5,80,80)
        self.health=200
    def draw(self,win):
        self.move()
        if sasuke.health>0:
            self.you_win_played=False
            if self.walkcount>5:
                 self.walkcount=0
            if self.speed>0:
                 win.blit(self.walkright[self.walkcount//2],(self.x,self.y))
                 self.walkcount+=1
            else:
                win.blit(self.walkleft[self.walkcount//2],(self.x,self.y))
                self.walkcount+=1
        else:
            win.blit(sasuke.dead,(sasuke.x,sasuke.y))
            sasuke.speed=0
            win.blit(CF.render('YOU WIN',True,light_orange),(230,550))
            if not self.you_win_played:
                pygame.mixer.music.stop()
                you_win.play()
                you_win.play()
                self.you_win_played=True 
        Sbar2=pygame.draw.rect(win,red,(570,390,200,20))
        Sbar1=pygame.draw.rect(win,yellow,(575,395,self.health,10))
        win.blit(Sh,(770,355))
    def move(self):     
        if self.speed>0:
            if self.x+self.speed<self.path[0]:
                self.x+=self.speed
            else:
                self.speed=self.speed*(-1)
                self.walkcount=0
        else:
            if self.x+self.speed>self.path[1]:
                self.x+=self.speed
            else:
                self.speed=self.speed*-1
                self.walkcount=0
        self.hitbox=(self.x+10,self.y+5,80,80)
        #pygame.draw.rect(win,(red),self.hitbox,4)
    def hit(self):
            self.health-=10
#window 
win=pygame.display.set_mode((1000,1500))
pygame.display.set_caption('naruto vs sasuke')
#clock
clock=pygame.time.Clock()
#font initialise 
font=pygame.font.SysFont(None,30,bold=False,italic=False)
CF=pygame.font.SysFont('comicsans',170,True)
GOF=pygame.font.SysFont('comicsans',160,True)
#images
bg=pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/bg.png')
shurikins=[]#empty list
walkleft=[pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NL2.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NL3.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NL1.png')]
jump_left=pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NL4.png')
walkright=[pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NR2.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NR3.png'),pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NR1.png')]
jump_right=pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/NR4.png')
stand=pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/Nstanding.png')
Nh=pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/Nh.png')
Sh=pygame.image.load('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/Sh.png')
#sounds
shurikinsound=pygame.mixer.Sound('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/shuriken.wav')
hitsound=pygame.mixer.Sound('/storage/emulated/0/Ninja images /Naruto-vs-Sasuke-Pygame-main/Naruto-vs-Sasuke-Pygame-main/pics/hit.wav')
bgm=pygame.mixer.music.load('/storage/emulated/0/Download/noncopyright-music-pianos-295174.mp3')
game_over=pygame.mixer.Sound('/storage/emulated/0/Download/cartoon-trombone-sound-effect-241387.mp3')
you_win=pygame.mixer.Sound('/storage/emulated/0/Download/you-win-female-gfx-sounds-3-3-00-01.mp3')
# music play 
pygame.mixer.music.play()
#button  positions and sizes
btn_lngt=100
btn_widt=60
left_btn=pygame.Rect(200,1300,btn_lngt,btn_widt)
right_btn=pygame.Rect(700,1300,btn_lngt,btn_widt)
up_btn=pygame.Rect(450,1200,btn_lngt,btn_widt)
down_btn=pygame.Rect(450,1400,btn_lngt,btn_widt)
shoot_btn=pygame.Rect(450,1300,btn_lngt,btn_widt)
quit_btn=pygame.Rect(850,1200,btn_lngt,btn_widt)
restart_btn=pygame.Rect(50,1200,btn_lngt,btn_widt)
naruto=player()
sasuke=enemy()
def redrawgamewindow(): 
    naruto.draw(win)
    sasuke.draw(win)
    for shurikin in shurikins:
        shurikin.draw(win)
#start game running 
while run:
    #add background 
     win.blit(bg,(150,350))
    #frame rate
     #pygame.time.delay(25):
     clock.tick(25)#25 FPS
     #button functioning 
     for event in pygame.event.get():#
       if event.type==pygame.QUIT:
            run=False 
       if event.type==pygame.MOUSEBUTTONDOWN:
         mx,my=pygame.mouse.get_pos()#getting pressed location and save in mx and my
         if quit_btn.collidepoint(mx,my):
                run=False 
         if restart_btn.collidepoint(mx,my):
            if not naruto.health>0 or not sasuke.health>0:
                naruto.x=150
                naruto.y=750
                naruto.health=200
                sasuke.health=200
                sasuke.speed=sasuke.initial_speed
                sasuke.x=750
                sasuke.y=750
                pygame.mixer.music.play()
         if naruto.health>0: 
             if left_btn.collidepoint(mx,my):
                naruto.x-=naruto.speed
                naruto.left=True  
                naruto.right=False 
                naruto.left_direction=True
                naruto.right_direction=False
             elif right_btn.collidepoint(mx,my):
                naruto.x+=naruto.speed
                naruto.left=False 
                naruto.right=True 
                naruto.right_direction=True 
                naruto.left_direction=False 
             elif up_btn.collidepoint(mx,my):
                naruto.is_jumping=True 
                y_vel=-naruto.jump_vel
                naruto.left=False 
                naruto.right=False 
             elif down_btn.collidepoint(mx,my):
                naruto.y+=naruto.speed
             elif shoot_btn.collidepoint(mx,my):
                if len(shurikins)<5:
                    if naruto.left_direction:
                        shurikins.append(weapon(round(naruto.x+50),round(naruto.y+20),'left'))
                        shurikinsound.play()
                    elif naruto.right_direction or not naruto.left and not naruto.right:
                        shurikins.append(weapon(round(naruto.x+15),round(naruto.y+20),'right'))
                        shurikinsound.play()
             
     if naruto.is_jumping:   
         naruto.y+=y_vel
         y_vel+=gravity
     if naruto.y>750:
       naruto.y=750
       naruto.is_jumping=False 
    
    # win.blit(naruto,(x,y))
    # draw button
     pygame.draw.rect(win,butn_back_colour,(10,1150,980,410))
     pygame.draw.rect(win,(green),left_btn)
     pygame.draw.rect(win,(yellow),right_btn)
     pygame.draw.rect(win,(blue),up_btn)
     pygame.draw.rect(win,(red),down_btn)
     pygame.draw.rect(win,(white),shoot_btn)
     pygame.draw.rect(win,(grey),quit_btn)
     pygame.draw.rect(win,(grey),restart_btn)
     #display font
     win.blit(font.render('LEFT',True, white),(220,1320))
     win.blit(font.render('RIGHT',True, white),(720,1320))
     win.blit(font.render('UP',True, white),(485,1220))
     win.blit(font.render('DOWN',True, white),(470,1420))
     win.blit(font.render('SHOOT',True,black),(465,1320))
     win.blit(font.render('QUIT',True, white,red),(870,1220))
     win.blit(font.render('RESTART',True, white,red),(55,1220))
     
     #Naruto max an min position 
     naruto.x=max(150,min(naruto.x,750))
     naruto.y=max(350,min(naruto.y,750))
     if naruto.health>0 and sasuke.health>0:
             if naruto.hitbox[0]+naruto.hitbox[2]>sasuke.hitbox[0] and naruto.hitbox[0]<sasuke.hitbox[0]+sasuke.hitbox[2]and naruto.hitbox[1]+naruto.hitbox[3]>sasuke.hitbox[1]and naruto.hitbox[1]<sasuke.hitbox[1]+sasuke.hitbox[3]:
                     naruto.hit()
                     hitsound.play()
     for shurikin in shurikins:
         if sasuke.health>0:
             if shurikin.hitbox[0]+shurikin.hitbox[2]>sasuke.hitbox[0] and shurikin.hitbox[0]<sasuke.hitbox[0]+sasuke.hitbox[2]and shurikin.hitbox[1]+shurikin.hitbox[3]>sasuke.hitbox[1]and shurikin.hitbox[1]<sasuke.hitbox[1]+sasuke.hitbox[3]:
                     sasuke.hit()
                     hitsound.play()
                     shurikins.pop(shurikins.index(shurikin))
         if shurikin.direction=='right':
                shurikin.x+=shurikin.speed
         if shurikin.direction=='left':
                shurikin.x-=shurikin.speed
         if shurikin.x<150 or shurikin.x>800:
             shurikins.pop(shurikins.index(shurikin))
     redrawgamewindow()
     pygame.display.update()#update the window after any change
pygame.quit()

