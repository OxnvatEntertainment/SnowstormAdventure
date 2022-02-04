attackspeed = 10
class Snowball:
    def __init__(self,a,b):
        self.x = mousex
        self.y = mousey
        self.r = pygame.Rect(self.x,self.y,a,b)
if bullettimer > -1:
    bullettimer += -1
for b in bullets:
    b.y += -5*stage
    b.r.topleft = b.x,b.y
    if b.y > 0:
        pygame.draw.circle(screen,(200,200,200),(b.x,b.y),10)
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
