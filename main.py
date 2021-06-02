# third party
import pygame
from pygame.locals import *

# internals
import config
from src.events import CustomEvent
from src.universe import Universe
from src.gui.container import Container
from src.gui.label import Label

config.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(config.confs['resolution'])
fps = config.confs['fps']
bgc = config.confs['background_color']

# test
uni = Universe()
cont = Container(pos=(100, 100), dimension=(100, 300))
cont.add_child(Label(pos=(0, 0), text='xablau', margin=(10, 10, 0, 0)))
cont.show_background = True

# main loop
run = True
while run:
    clock.tick(fps)
    screen.fill(bgc)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type >= CustomEvent.UNIVERSE_EVENT.value and event.type <= CustomEvent.UNIVERSE_EVENT_F.value:
            uni.update(event.type)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = uni.click(event.pos)

    cont.draw(screen)
    pygame.display.flip()

# end game
pygame.quit()
exit()
