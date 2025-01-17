# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.get_init()
    
    # Get a new GUI window
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with solid black
        screen.fill("black")

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
