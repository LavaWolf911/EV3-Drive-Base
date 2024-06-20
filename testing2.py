import pygame
pygame.init()
pygame.joystick.init()
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except pygame.error:
    print("No Controller")
    pygame.quit()
    quit()
else:
    def get_axis(axis):
        return joystick.get_axis(axis)
 
 
    def get_digital(button):
        return joystick.get_button(button)
 
 
    def hat(hat):
        return joystick.get_hat(hat)