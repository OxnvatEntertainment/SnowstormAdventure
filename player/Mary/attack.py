attackspeed = 10
class Snowball:
    def __init__(self,a,b):
        self.xleft = mousex
        self.xright = mousex
        self.y = mousey
        self.rleft = pygame.Rect(self.xleft,self.y,a,b)
        self.rright = pygame.Rect(self.xright,self.y,a,b)
if bullettimer > -1:
    bullettimer += -1
for b in bullets:
    b.xleft += -2*stage
    b.xright += 2*stage
    b.y += -5*stage
    b.rleft.topleft = b.xleft,b.y
    b.rright.topleft = b.xright,b.y
    if b.y > 0:
        pygame.draw.circle(screen,(200,200,200),(b.xleft,b.y),10)
        pygame.draw.circle(screen,(200,200,200),(b.xright,b.y),10)
    else:
        bullets.remove(b)
for s in snowmen:
    s.y += 5*stage
    s.r.topleft = s.x,s.y   
    for b in bullets:
        if s.r.colliderect(b.rleft) or s.r.colliderect(b.rright):
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
