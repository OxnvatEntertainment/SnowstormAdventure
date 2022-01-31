import pygame
import random
pygame.init()

width = 360
height = 640
screen = pygame.display.set_mode((width,height))

text = pygame.font.SysFont("Arial Bold", 25)

timer = 0
sceneinscene = 0
scene = 0
bullettimer = 0
snowballtimer = 0
spritetimer = 0
snowmantimer = 50
currentnoodlesprite = 0
score = 0
stage = 0
stagetimer = 2500
sodas = 0
keys = pygame.key.get_pressed()
def blit(image,scale,pos):
    image = pygame.transform.scale(image, (scale[0], scale[1]))
    screen.blit(image,pos)

bullets = []

snowmen = []
snowmanrects = []

titlecard = pygame.image.load("openingCutscene/titlecard.png")
playbutton = [pygame.image.load("openingCutscene/play.png"),pygame.Rect(10,505,340,127)]

opscene = [pygame.image.load("openingCutscene/logo.png"),pygame.image.load("openingCutscene/fauxmanhouse.png"),pygame.image.load("openingCutscene/noodletyping.png"),pygame.image.load("openingCutscene/noodletalking.png")]
opsounds = ["openingCutscene/wind.mp3","openingCutscene/typing.mp3","openingCutscene/eh.mp3","openingCutscene/wind.mp3"]
music = True
thissong = pygame.mixer.music.load(opsounds[0])
noodlesprites = [pygame.image.load("player/standleft.png"),pygame.image.load("player/stepleft.png"),pygame.image.load("player/standright.png"),pygame.image.load("player/stepright.png")]

asnowman = pygame.image.load("snowman.png")
win = pygame.image.load("win.png")
loss = pygame.image.load("loss.png")
lossbutscore = pygame.image.load("highscore.png")

throw = pygame.mixer.Sound("snowball.mp3")
hit = pygame.mixer.Sound("snowmanhit.mp3")
explosion = pygame.mixer.Sound("sodabomb.mp3")

clock = pygame.time.Clock()

class Snowman:
    def __init__(self,start,end,a,b):
        self.x = random.randrange(0,310)
        self.y = 0
        self.r = pygame.Rect(random.randrange(0,310),0,a,b)

class Snowball:
    def __init__(self,a,b):
        self.x = mousex
        self.y = mousey
        self.r = pygame.Rect(self.x,self.y,a,b)

class Enemyball:
    def __init__(self,a,b):
        self.x = 0
        self.y = 0
        self.r = pygame.Rect(self.x,self.y,a,b)

exec(open("highscore.py").read())

running = True

while running:
    mousex,mousey = pygame.mouse.get_pos()
    noodlerect = pygame.Rect(mousex-25,mousey-54,50,108)
    screen.fill((255,255,255))
    if music:
        pygame.mixer.music.play(0,0.0)
        music = False

    if scene == 0:
        if timer < 150:
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
            blit(titlecard, (360,105), (0,0))
            blit(playbutton[0], (340,127), playbutton[1])
            screen.blit(text.render("High Score: "+str(highscore), False, (100,100,100)),(10,105))
        if sceneinscene == 3:
            screen.blit(text.render("Man, I'm really craving a soda right now.", False, (0,128,0)),(10,450))
        if pygame.mouse.get_pressed()[0] and playbutton[1].collidepoint(pygame.mouse.get_pos()) and sceneinscene != 0:
            pygame.mixer.music.load("song.mp3")
            music = True
            sodas = 0
            stagetimer = 3500
            stage = 1
            score = 0
            scene = 1
    elif scene == 1:
        screen.blit(text.render("Stage "+str(stage), False, (0,0,0)),(0,0))
        screen.blit(text.render("Score: "+str(score), False, (0,0,0)),(0,25))
        screen.blit(text.render("Sodas: "+str(sodas), False, (0,0,0)),(0,50))
        screen.blit(text.render(str(round(stagetimer/60))+" seconds until next stage", False, (0,0,0)),(0,75))
        if spritetimer < 20:
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
            bullettimer = 25
        if bullettimer > -1:
            bullettimer += -1
        for b in bullets:
            b.y += -2*stage
            b.r.topleft = b.x,b.y
            if b.y > 0:
                pygame.draw.circle(screen,(200,200,200),(b.x,b.y),10)
            else:
                bullets.remove(b)
        if snowmantimer > -1:
            snowmantimer += -1
        else:
            snowmantimer = round(75/stage)
            snowmen.append(Snowman(78,302,50,78))
        for s in snowmen:
            s.y += 2*stage
            s.r.topleft = s.x,s.y
            for b in bullets:
                if s.r.colliderect(b.r):
                    hit.play()
                    snowmen.remove(s)
                    bullets.remove(b)
                    score += 20*stage
            if s.r.colliderect(noodlerect):
                snowmen = []
                bullets = []
                if score > highscore:
                    pygame.mixer.music.load("win.mp3")
                    music = True
                    scene = 3
                else:
                    pygame.mixer.music.load("loss.mp3")
                    music = True
                    scene = 4
            if s.y < 640:
                blit(asnowman,(50,78),(s.x,s.y))
            else:
                snowmen.remove(s)
        if stagetimer > -1:
            stagetimer += -1
        else:
            snowmen = []
            bullets = []
            pygame.mixer.music.load("win.mp3")
            music = True
            scene = 2
        blit(noodlesprites[currentnoodlesprite],(50,108),noodlerect)
    elif scene == 2:
        screen.blit(win,(0,0))
        if pygame.mouse.get_pressed()[0]:
            pygame.mixer.music.load("song.mp3")
            music = True
            sodas += 1
            stagetimer = 2500
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
    clock.tick(60)
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
