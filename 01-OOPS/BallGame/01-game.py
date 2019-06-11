import pygame

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 100,105,150

x = 50
y = 50
ballRadius = 50
moveX = 1
moveY = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.circle(screen,red,[x,y],ballRadius)
    x += moveX
    y += moveY

    if x > width - ballRadius:
        moveX = -1
    elif y > height - ballRadius:
        moveY = -1
    elif x <ballRadius:
        moveX = 1
    elif y < ballRadius:
        moveY = 1


    # Updating screen
    pygame.display.flip()