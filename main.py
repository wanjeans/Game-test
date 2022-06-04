import pygame
import os

width, height=900,500
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("First game!")

#
FPS = 60
#color
white=(255,255,255)

yellow_spaceship_image=pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
red_spaceship_image=pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))

def draw_windows():
    win.fill(white)
    pygame.display.update()

def main():
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_windows()


    pygame.quit()

if __name__=="__main__":
    main()