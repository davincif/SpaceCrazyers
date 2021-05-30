# third party
import pygame
from pygame.locals import *

# internals
import config
from src.planet import Planet
from src.player import Player
from src.aircraft import Aircraft

config.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(config.confs['resolution'])
fps = config.confs['fps']
bgc = config.confs['background_color']

# test
play1 = Player(
    pos=(0, 0),
    name='Leo'
)
p1 = Planet(
    onwer=play1,
    pos=(100, 100),
    name='xablau',
    color=(255, 0, 0),
    max_health=1000
)
a1 = Aircraft(
    onwer=play1,
    planet=p1,
    pos=(612, 412),
    name='mob1',
    color=pygame.Color(0, 150, 150),
    max_health=1000
)

play2 = Player(
    pos=(0, 0),
    name='Liza'
)
p2 = Planet(
    onwer=play2,
    pos=(850, 100),
    name='cosita',
    color=(0, 0, 255),
    max_health=1000
)
a2 = Aircraft(
    onwer=play2,
    planet=p2,
    pos=(702, 602),
    name='asd',
    color=pygame.Color(200, 0, 100),
    max_health=1000
)

while True:
    clock.tick(fps)
    screen.fill(bgc)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    p1.draw(screen)
    a1.draw(screen)
    p2.draw(screen)
    a2.draw(screen)
    pygame.display.flip()
