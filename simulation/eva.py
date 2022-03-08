import pygame
import sys

pygame.init()
win = pygame.display.set_mode((800, 600))
x = 40

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x+=1
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, 40, 20, 20))
    pygame.display.update()