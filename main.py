import pygame
import os

width, height=1000,700
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("First game!")

#
FPS = 60
#color
white=(255,255,255)
ship_width,ship_height = 55,40


yellow_spaceship_image=pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship=pygame.transform.scale(
    yellow_spaceship_image,(ship_width,ship_height))
yellow_spaceship_rotated=pygame.transform.rotate(yellow_spaceship,90)

red_spaceship_image=pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))
red_spaceship=pygame.transform.scale(
    red_spaceship_image,(ship_width,ship_height))
red_spaceship_rotated=pygame.transform.rotate(red_spaceship,270)

def draw_windows(red,yellow):
    win.fill(white)
    win.blit(yellow_spaceship_rotated,(yellow.x,yellow.y))
    win.blit(red_spaceship_rotated,(red.x,red.y))
    pygame.display.update()

def main():
    yellow=pygame.Rect(300,100,ship_width,ship_height)
    red=pygame.Rect(700,100,ship_width,ship_height)
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_windows(red,yellow)


    pygame.quit()

if __name__=="__main__":
    main()