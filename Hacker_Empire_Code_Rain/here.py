import pygame
import random
# 参数
SCREENSIZE=(600,600)
BLACK=(0,0,0,13)
# 初始化
pygame.init()
font = pygame.font.SysFont('微软雅黑', 20)
screen = pygame.display.set_mode(SCREENSIZE)
surface = pygame.Surface(SCREENSIZE, flags=pygame.SRCALPHA)
pygame.Surface.convert(surface)
surface.fill(BLACK)
screen.fill(BLACK)
# 内容
lib=[chr(i) for i in range(48,48+10)] + [chr(i) for i in range(97,97+26)]   # [0-9 a-z]
texts = [font.render(l, True, (0, 255, 0)) for l in lib]
cols = list(range(40))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(33)
    screen.blit(surface, (0, 0))
    for i in range(n:=len(cols)):
        text = random.choice(texts)
        x,y=random.randint(0,n-1),random.randint(0,n-1)
        screen.blit(text, (i * 15, cols[i] * 15))
        cols[i] = 0 if cols[i] >80 or random.random() > 0.95 else cols[i]+1
    pygame.display.flip()
