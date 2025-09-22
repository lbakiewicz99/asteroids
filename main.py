import pygame
from circleshape import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    spawn = AsteroidField()
    print(pygame.init())
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    new_clock = pygame.time.Clock()
    dt = 0.00
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
        

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over")
                sys.exit()


        pygame.display.flip()
        # new_clock.tick(60)
        dt = new_clock.tick(60) / 1000
    


    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
