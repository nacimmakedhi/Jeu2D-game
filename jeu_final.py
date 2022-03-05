import pygame
import random

##interface

pygame.font.init()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Eggs Rain')

background = pygame.image.load('nassim.jpg')
kipper = pygame.image.load('kipper.png')
kipper = pygame.transform.scale(kipper, (140, 60))
egg = pygame.image.load('egg.png')
egg = pygame.transform.scale(egg, (50, 50))

rect_egg = egg.get_rect()
rect_kipper = kipper.get_rect()

x_kipper = 500
y_kipper = 450
x2_kipper = x_kipper + 140
y2_kipper = y_kipper + 60

x_egg = random.randrange(0, screen_width - 50)
y_egg = 100
x2_egg = x_egg + 50
y2_egg = y_egg + 50

speed = 2
kipper_speed = 5

chances = 3
score = 0

font = pygame.font.SysFont("comicsansms", 25)
font1 = pygame.font.SysFont("comicsansms", 25)
font2 = pygame.font.SysFont("comicsansms", 40)

text = font.render("Score : " + str(score) ,True, (255,0,0))
text0 = font.render("Chances : " + str(chances) , True , (255,0,0))
game_over = font2.render("G A M E   O V E R", True , (255,0,0))



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    text = font.render("Score : " + str(score), True, (255, 0, 0))
    text0 = font.render("Chances : " + str(chances), True, (255, 0, 0))
    game_over = font2.render("G A M E   O V E R", True, (255, 0, 0))

    screen.blit(background, (0, 0))
    screen.blit(kipper, (x_kipper, y_kipper))
    screen.blit(egg, (x_egg, y_egg))
    screen.blit(text, (50, 40))
    screen.blit(text0,(700,40))


    keys = pygame.key.get_pressed()

    x2_kipper = x_kipper + 140
    y2_kipper = y_kipper + 60

    ##control kipper
    if x_kipper <= screen_height + 150:
        if keys[pygame.K_RIGHT]:
            x_kipper = x_kipper + kipper_speed
    if x_kipper >= 0:
        if keys[pygame.K_LEFT]:
            x_kipper = x_kipper - kipper_speed

    ## drop down eggs
    y_egg = y_egg + speed

    ## logic 
    if y_egg >= 450:

        if x2_kipper > x_egg > x_kipper or x2_kipper > x2_egg > x_kipper :
            print("egg taken")
            score = score + 1
            print("score : ",score)
            y_egg = 0
            x_egg = random.randrange(0, screen_width - 50)

        else:
            print("Filed")
            chances = chances - 1
            y_egg = 0
            x_egg = random.randrange(0, screen_width - 50)

    ## level up 

    if score > 10:
        speed = 3
        kipper_speed = 8

    elif score > 25:
        speed = 4
        kipper_speed = 8

    elif score > 50:
        speed = 5
        kipper_speed = 9

    elif score > 70:
        speed = 6
        kipper_speed = 10

    elif score > 100:
        speed = 7
        kipper_speed = 10



    ##  game over 

    if chances == 0 :
        y_egg = -100
        screen.blit(game_over , (320,280))


    pygame.display.update()