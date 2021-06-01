# standards
import os

# third party
import pygame
import yaml

CONFIG_FILE = 'bdr.config.yml'
confs: dict = None


def init(fileAdd: str = ''):
    global confs
    # print("Welcome to Bolo de Rolo.", end='\n\n')

    pygame.init()
    video_info = pygame.display.Info()

    # decide file path
    if fileAdd == '':
        file_path = os.path.join('.', CONFIG_FILE)

    # load condig file
    with open(file_path) as file:
        confs = yaml.load(file, Loader=yaml.FullLoader)

    # treat entries
    confs['background_color'] = pygame.Color(*confs['background_color'])
    confs['fps'] = int(confs['fps'])
    confs['resolution'] = (
        video_info.current_w if confs['resolution'][0] == 'max' else int(confs['resolution'][0]),
        video_info.current_h if confs['resolution'][1] == 'max' else int(confs['resolution'][1])
    )
