import pygame, sys
pygame.init()
screen = pygame.display.set_mode([600,600])
screen.fill([255,255,255])
my_ball = pygame.image.load('pokeball.jpg')
x = 50
y = 50
x_speed = 10
y_speed = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(30)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 200, 200], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 95 or x < 0:
        x_speed = -x_speed
    if y > screen.get_width() - 95 or y < 0:
        y_speed = -y_speed
    screen.blit(my_ball,[x, y])
    pygame.display.flip()
pygame.quit()

