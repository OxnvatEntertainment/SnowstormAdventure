import pygame
import random
pygame.init()

width = 360
height = 640
screen = pygame.display.set_mode((width,height))

text = pygame.font.SysFont("Arial Bold", 25)
menufont = pygame.font.SysFont("Arial Bold", 75)

skins = ["Noodle","Chris","Mary"]
skin = 0
timer = 0
sceneinscene = 0
scene = 0
bullettimer = 0
snowballtimer = 0
spritetimer = 0
snowmantimer = 50
currentnoodlesprite = 0
score = 0
coincount = 0
stage = 0
stagenames = ["Chestershire","Manchester","Hooksett","Allenstown","Concord","Epsom","Pittsfield","Laconia","Ossipee","Glen","Lancaster","Quebec","Newfoundland","Greenland","The North F'ing Pole"]
stagetimer = 2500
sodas = 0
keys = pygame.key.get_pressed()
def blit(image,scale,pos):
    image = pygame.transform.scale(image, (scale[0], scale[1]))
    screen.blit(image,pos)

bullets = []
coins = []
snowmen = []
snowmanrects = []
menuitems = []

titlecard = pygame.image.load("openingCutscene/titlecard.png")
playbutton = [pygame.image.load("openingCutscene/play.png"),pygame.Rect(10,375,340,127)]
skinsbutton = [pygame.image.load("openingCutscene/skins.png"),pygame.Rect(10,505,340,127)]
applyrect = pygame.Rect(25,552,65,65)

opscene = [pygame.image.load("openingCutscene/logo.png"),pygame.image.load("openingCutscene/fauxmanhouse.png"),pygame.image.load("openingCutscene/noodletyping.png"),pygame.image.load("openingCutscene/noodletalking.png")]
opsounds = ["openingCutscene/wind.mp3","openingCutscene/typing.mp3","openingCutscene/eh.mp3","openingCutscene/wind.mp3"]
music = True
thissong = pygame.mixer.music.load(opsounds[0])

noodlesprites = [pygame.image.load("player/"+skins[skin]+"/standleft.png"),pygame.image.load("player/"+skins[skin]+"/stepleft.png"),pygame.image.load("player/"+skins[skin]+"/standright.png"),pygame.image.load("player/"+skins[skin]+"/stepright.png")]

asnowman = pygame.image.load("snowman.png")
acoin = pygame.image.load("coin.png")
win = pygame.image.load("win.png")
loss = pygame.image.load("loss.png")
lossbutscore = pygame.image.load("highscore.png")
nosoda = pygame.image.load("nosoda.png")
menubutton = pygame.image.load("menubutton.png")
skinsmenu = pygame.image.load("skinsmenu.png")
applybutton = pygame.image.load("apply.png")

throw = pygame.mixer.Sound("snowball.mp3")
hit = pygame.mixer.Sound("snowmanhit.mp3")
explosion = pygame.mixer.Sound("sodabomb.mp3")
kaching = pygame.mixer.Sound("kaching.mp3")

clock = pygame.time.Clock()

class Snowman:
    def __init__(self,start,end,a,b):
        self.x = random.randrange(0,310)
        self.y = 0
        self.r = pygame.Rect(random.randrange(0,310),0,a,b)

class Coin:
    def __init__(self,start,end,a,b):
        self.x = random.randrange(0,310)
        self.y = 0
        self.r = pygame.Rect(random.randrange(0,310),0,a,b)

class MenuItem:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = pygame.Rect(0,0,296,65)

exec(open("highscore.py").read())

running = True

while running:
    if stage < 15:
        stagename = stagenames[stage-1]
    else:
        stagename = stagenames[14]
    mousex,mousey = pygame.mouse.get_pos()
    noodlerect = pygame.Rect(mousex-25,mousey-54,50,74)
    screen.fill((255,255,255))
    if music:
        pygame.mixer.music.play(0,0.0)
        music = False

    if scene == 0:
        if timer < 75:
            blit(opscene[sceneinscene], (360,640), (0,0))
        else:
            thissong = pygame.mixer.music.load(opsounds[sceneinscene])
            music = True
            timer = 0
            if sceneinscene == 3:
                sceneinscene = 0
            else:
                sceneinscene += 1
        timer += 1
        if sceneinscene != 0:
            blit(titlecard, (360,78), (0,0))
            blit(playbutton[0], (340,127), playbutton[1])
            blit(skinsbutton[0], (340,127), skinsbutton[1])
            screen.blit(text.render("High Score: "+str(highscore), False, (100,100,100)),(10,78))
        if sceneinscene == 3:
            screen.blit(text.render("Man, I'm really craving a soda right now.", False, (0,128,0)),(10,355))
        if pygame.mouse.get_pressed()[0] and playbutton[1].collidepoint(pygame.mouse.get_pos()) and sceneinscene != 0:
            pygame.mixer.music.load("song.mp3")
            music = True
            coincount = 0
            sodas = 0
            stagetimer = 1000
            stage = 1
            score = 0
            scene = 1
        if pygame.mouse.get_pressed()[0] and skinsbutton[1].collidepoint(pygame.mouse.get_pos()) and sceneinscene != 0:
            pygame.mixer.music.load("menu.mp3")
            music = True
            scene = 6
    elif scene == 1:
        screen.blit(text.render("Stage "+str(stage)+": "+stagename, False, (0,0,0)),(0,0))
        screen.blit(text.render("Coins: "+str(coincount), False, (0,0,0)),(0,25))
        screen.blit(text.render("Score: "+str(score), False, (0,0,0)),(0,50))
        screen.blit(text.render("Sodas: "+str(sodas), False, (0,0,0)),(0,75))
        screen.blit(text.render(str(round(stagetimer/24))+" seconds until next stage", False, (0,0,0)),(0,100))
        if spritetimer < 1:
            spritetimer += 1
        else:
            spritetimer = 0
            if currentnoodlesprite == 3:
                currentnoodlesprite = 0
            else:
                currentnoodlesprite += 1
        if pygame.mouse.get_pressed()[0] and bullettimer < 0:
            throw.play()
            bullets.append(Snowball(20,20))
            bullettimer = attackspeed
        exec(open("player/"+skins[skin]+"/attack.py").read())
        for c in coins:
            c.y += 5*stage
            c.r.topleft = c.x,c.y
            if c.r.colliderect(noodlerect):
                if c.y < 640:
                    kaching.play()
                    coincount += 1
                    coins.remove(c)
            if c.y < 640:
                blit(acoin,(50,50),(c.x,c.y))
            else:
                coins.remove(c)
        if snowmantimer > -1:
            snowmantimer += -1
        else:
            snowmantimer = round(15/stage)
            snowmen.append(Snowman(78,302,50,78))
            coins.append(Coin(78,302,50,50))
        if stagetimer > -1:
            stagetimer += -1
        else:
            snowmen = []
            coins = []
            bullets = []
            if coincount >= 10*stage:
                pygame.mixer.music.load("win.mp3")
                music = True
                scene = 2
            else:
                pygame.mixer.music.load("nosoda.mp3")
                music = True
                scene = 5
        blit(noodlesprites[currentnoodlesprite],(50,108),noodlerect)
    elif scene == 2:
        screen.blit(win,(0,0))
        if pygame.mouse.get_pressed()[0]:
            pygame.mixer.music.load("song.mp3")
            music = True
            coincount += -15*stage
            sodas += 1
            stagetimer = 1000
            stage += 1
            scene = 1
    elif scene == 3:
        with open("highscore.py","r") as file:
            filedata = file.read()
        filedata = filedata.replace(str(highscore),str(score))
        with open("highscore.py","w") as file:
            file.write(filedata)
        highscore = score
        screen.blit(lossbutscore,(0,0))
        if pygame.mouse.get_pressed()[0]:
            sceneinscene = 0
            scene = 0
    elif scene == 4:
        screen.blit(loss,(0,0))
        if pygame.mouse.get_pressed()[0]:
            sceneinscene = 0
            scene = 0
    elif scene == 5:
        screen.blit(nosoda,(0,0))
        if pygame.mouse.get_pressed()[0]:
            pygame.mixer.music.load("song.mp3")
            music = True
            stagetimer = 1000
            stage += 1
            scene = 1
    elif scene == 6:
        screen.blit(skinsmenu,(0,0))
        for item in skins:
            menuitems.append(MenuItem())
            for j in menuitems:
                j.x = 25
                j.y = skins.index(item)*70+155
                j.r = pygame.Rect(j.x,j.y,296,65)
                screen.blit(menubutton,(25,skins.index(item)*70+155))
                screen.blit(menufont.render(item, False, (0,0,0)),(0+30,skins.index(item)*70+165))
                if pygame.mouse.get_pressed()[0] and j.r.collidepoint(pygame.mouse.get_pos()):
                    skin = skins.index(item)
                    noodlesprites = [pygame.image.load("player/"+skins[skin]+"/standleft.png"),pygame.image.load("player/"+skins[skin]+"/stepleft.png"),pygame.image.load("player/"+skins[skin]+"/standright.png"),pygame.image.load("player/"+skins[skin]+"/stepright.png")]
        menuitems = []    
        blit(noodlesprites[0],(50,108),(300,512))
        screen.blit(applybutton,(applyrect))
        if pygame.mouse.get_pressed()[0] and applyrect.collidepoint(pygame.mouse.get_pos()):
            sceneinscene = 0
            scene = 0 
    clock.tick(24)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and sodas > 0 and scene == 1:
                explosion.play()
                score += stage*10*len(snowmen)
                snowmen = []
                sodas += -1

pygame.quit()
