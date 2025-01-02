import pygame
from constants import *
from player import Player

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    # fps settings
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # move player
        player.update(dt)
        
        # add black background
        screen.fill('black')

        # render player
        player.draw(screen)

        # update screen
        pygame.display.flip()

        # work with fps
        time_passed = clock.tick(60)
        dt = time_passed / 1000



if __name__ == "__main__":
    main()
