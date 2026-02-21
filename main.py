from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot 

import sys
import pygame

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable) 

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids: 
            
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
