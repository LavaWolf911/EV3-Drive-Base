import pygame as pg
import traceback
import math

# checking the pygame version because they behave different
version = pg.__version__
PGVERSION = int(version.split('.')[0])

offset_y = 64
WIDTH = 812
HEIGHT = 554 + offset_y

# initialize pygame
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
gamepad_bg = pg.image.load('assets/gamepad.png')
vec = pg.math.Vector2
font = pg.font.SysFont('Arial', 24)
pg.joystick.init()

running = True


try:
    while running:
        clock.tick(60)
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    
        screen.fill((50, 50, 50))
        # draw the gamepad
        screen.blit(gamepad_bg, (0, offset_y))
        
        # detect gamepad
        gamepads = [pg.joystick.Joystick(x) for x in range(
                     pg.joystick.get_count())]
        if len(gamepads) > 0:
            gamepads[0].init()
            name = gamepads[0].get_name()
            buttons = gamepads[0].get_numbuttons()
            axes = gamepads[0].get_numaxes()
            dpads = gamepads[0].get_numhats()
    
            stick_l_pressed = False
            stick_r_pressed = False
        
            trigger_r = 0
            trigger_l = 0   
            
            text = "Device: " + name
            text_surf = font.render(text, False, (200, 200, 200))
    else:
            text = "No Device plugged in."
            text_surf = font.render(text, False, (200, 200, 200))
            screen.blit(text_surf, (120, 16))
    pg.display.update()
    
    pg.quit()
except Exception:
    traceback.print_exc()
    pg.quit()