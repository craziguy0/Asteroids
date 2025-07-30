import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot

def main():
    pygame.init() # Initialize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the screen size
    clock = pygame.time.Clock() # Create a clock to manage the frame rate
    
    updatable = pygame.sprite.Group() # Create sprite groups for updatable and drawable objects
    drawable = pygame.sprite.Group() # Create sprite groups for updatable and drawable objects
    asteroids = pygame.sprite.Group() # Create a group for asteroids
    shots = pygame.sprite.Group() # Create a group for shots


    Asteroid.containers = (asteroids, updatable, drawable) # Set up sprite groups for asteroids
    Shot.containers = (shots, updatable, drawable) # Set up sprite groups for shots
    AsteroidField.containers = updatable # Set up sprite groups for asteroid field
    asteroid_field = AsteroidField() # Create an instance of the asteroid field

    Player.containers = (updatable, drawable) # Set up sprite groups

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create player instance
    
    dt = 0 # Initialize delta time

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all updatable sprites
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):   # Check for asteroid collision with player
                print("Game over!") # Print game over message
                sys.exit() # Exit the game
            for shot in shots:
                if asteroid.collides_with(shot): # Check for collision between asteroid and shot
                    shot.kill() # Remove the asteroid and shot if they collide
                    asteroid.split() # Split the asteroid if it collides with a shot
                    
        # Clear the screen
        screen.fill("black")
        # Draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)
        # Flip the display
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000.0 


if __name__ == "__main__": # Entry point of the program
    main()
