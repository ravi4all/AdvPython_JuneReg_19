import pygame
import random

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 100,105,150

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ballRadius = 40
        self.moveX = random.randint(0,4)
        self.moveY = random.randint(0,4)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - self.ballRadius:
            self.moveX = random.randint(-4, -1)
        elif self.y > height - self.ballRadius:
            self.moveY = random.randint(-4, -1)
        elif self.x < self.ballRadius:
            self.moveX = random.randint(0, 4)
        elif self.y < self.ballRadius:
            self.moveY = random.randint(0, 4)

# ball_1 = Ball()
# ball_2 = Ball()

BALLS = []
for i in range(50):
    ball = Ball()
    BALLS.append(ball)

FPS = 100
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # pygame.draw.circle(screen,red,[ball_1.x,ball_1.y],ball_1.ballRadius)
    # pygame.draw.circle(screen, red, [ball_2.x, ball_2.y], ball_2.ballRadius)
    #
    # ball_1.update()
    # ball_2.update()

    for i in range(len(BALLS)):
        pygame.draw.circle(screen, BALLS[i].color, [BALLS[i].x, BALLS[i].y], BALLS[i].ballRadius)
        BALLS[i].update()

    # Updating screen
    pygame.display.flip()
    clock.tick(FPS)