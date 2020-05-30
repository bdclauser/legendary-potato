import pygame
from pygame import display, event, image

pygame.init()


display.set_caption('My Game')


screen = display.set_mode((512, 512))

running = True

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

print('Goodbye!')
