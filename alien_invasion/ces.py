#ces
#2022/10/16
#author:linxu
import pygame


from pygame.locals import *


def DrawRect(screen):
    mycolcor = (0, 0, 255)
    x = 300
    y = 250
    position = (x, y, 100, 100)
    width = 0
    pygame.draw.rect(screen, mycolcor, position, width)


def main():
    pygame.init()
    pygame.display.set_caption('Draw Rectangle')
    screen = pygame.display.set_mode([600, 500])

    mRunning = True
    while mRunning:
        for event in pygame.event.get():
            if event.type == QUIT:
                mRunning = False
        DrawRect(screen)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()