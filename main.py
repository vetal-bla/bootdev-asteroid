import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    # fps settings
    clock = pygame.time.Clock()
    dt = 0

    # groups for classes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # added player to both group of update and draw
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

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

        # iterate over asteroids and check if asteroid collide with player
        # if yes game over
        for obj in asteroids:
            if obj.colliding(player):
                print("Game over!")
                sys.exit(0)

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
