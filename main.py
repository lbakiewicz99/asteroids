import pygame
from constants import *
from player import *

def main():
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
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        new_clock.tick(60)
        dt = new_clock.tick(60) / 1000
    


    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
