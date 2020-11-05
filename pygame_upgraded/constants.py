import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
YELLOW_LIGHT = (225, 200, 0)
COLOR_LIGHT_UNSELECTED = (170, 170, 170, 70)
COLOR_LIGHT_SELECTED = (200, 200, 200, 150)
LIGHT_RED_SELECTED = (255, 100, 100)
LIGHT_RED_UNSELECTED = (225, 70, 70)
LIGHT_BLUE_SELECTED = (120, 120, 255)
LIGHT_BLUE_UNSELECTED = (70, 70, 225)
LIGHT_GREEN_SELECTED = (120, 255, 120)
LIGHT_GREEN_UNSELECTED = (70, 225, 70)

width = 800
height = 600

bg = pg.image.load("pics/Background_forest.jpg")
background = pg.transform.scale(bg, (width, height))

vs_sign = pg.image.load("pics/VS.PNG")
vs_sign = pg.transform.scale(vs_sign, (200, 150))

background_win = pg.image.load("pics/winning_pic.jpg")
background_win = pg.transform.scale(background_win, (width, height))

logo = pg.image.load("pics/LOGO.PNG")
logo = pg.transform.scale(logo, (360, 222))

start_background = pg.image.load("pics/background_start.png")
start_background = pg.transform.scale(start_background, (width, height))

instructions_frame = pg.image.load("pics/Frame_background.PNG")
instructions_frame = pg.transform.scale(instructions_frame, (650, 450))

robofont = "fonts//RobotoSlab-Black.ttf"
robofont_medium = "fonts//RobotoSlab-Medium.ttf"