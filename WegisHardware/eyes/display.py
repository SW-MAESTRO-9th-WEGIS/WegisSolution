import pygame
import math

pygame.display.init()
window = pygame.display.set_mode((800, 400))
mapImg = pygame.image.load("1.bmp")

done = False

while not done:

   window.fill((0,0,0))
   evtList = pygame.event.get()
   for evt in evtList:
       if evt.type == pygame.QUIT:
          done = True

   window.blit(mapImg, (0,0)) #<<will not blit
   pygame.display.update() # solution: you forgot this...

pygame.quit()
