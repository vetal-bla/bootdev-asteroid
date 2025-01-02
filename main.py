import pygame
from constants import *
from player import Player

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    # fps settings
    clock = pygame.time.Clock()
    dt = 0

    # groups for classes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # added player to both group of update and draw
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # move objects
        for obj in updatable:
            obj.update(dt)

        # add black background
        screen.fill('black')

        # render objects
        for obj in drawable:
            obj.draw(screen)

        # update screen
        pygame.display.flip()

        # work with fps
        time_passed = clock.tick(60)
        dt = time_passed / 1000



if __name__ == "__main__":
    main()
