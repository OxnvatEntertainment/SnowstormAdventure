attackspeed = 5
knife = pygame.image.load("player/Chris/knife.png")
class Snowball:
    def __init__(self,a,b):
        self.x = mousex
        self.y = mousey
        self.r = pygame.Rect(self.x,self.y,a,b)
if bullettimer > -1:
    bullettimer += -1
for b in bullets:
    b.x = mousex
    b.y += -10*stage
    b.r.topleft = b.x-25,b.y-32
    if b.y > mousey-64:
        blit(knife, [50,64],[b.x-25,b.y-32])
    else:
        bullets.remove(b)
for s in snowmen:
    s.y += 5*stage
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
        coins = []
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
