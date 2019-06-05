import pygame, sys
pygame.init()
screen = pygame.display.set_mode([550,500])
screen.fill([255,255,255])
tree1 = pygame.image.load("Merry-Christmas_Gif1.gif")
tree2 = pygame.image.load("Merry-Christmas2.gif")
tree3 = pygame.image.load("Merry-Christmas3.gif")
tree4 = pygame.image.load("Merry-Christmas4.gif")
for i in range(1,10001):
    screen.blit(tree1,[30,50])
    pygame.display.flip()
    pygame.time.delay(500)
    screen.blit(tree2,[30,50])
    pygame.display.flip()
    pygame.time.delay(500)
    screen.blit(tree3,[30,50])
    pygame.display.flip()
    pygame.time.delay(500)
    screen.blit(tree4,[30,50])
    pygame.display.flip()
    pygame.time.delay(500)
    i = i + 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()



