import pygame
import math
import os

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Line Follower")
icon = pygame.image.load(os.path.join('imgs', 'icon.png'))
pygame.display.set_icon(icon)

backgroundImg = pygame.image.load(os.path.join('imgs', 'track.png'))

# bot
botImg = pygame.image.load(os.path.join('imgs', 'bot.jpg'))
# current position of bot should be chosen in the way that it should spawn correctly on the screen
botSize = 60  # diameter of bot
botCurrent_y = 320
running = True
while running:
    screen.fill(black)
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    botCurrent_y -= 1
    screen.blit(botImg, (146 - botSize / 2, botCurrent_y - botSize / 2))
    pygame.display.update()
