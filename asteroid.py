import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape): # Asteroid class inherits from CircleShape
    def __init__(self, x, y, radius): # Initialize the asteroid at position (x, y) with a given radius
        super().__init__(x, y, radius) # Call the parent constructor
        
    def draw(self, screen): # Draw the asteroid as a circle on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # Draw the circle with a white outline

    def update(self, dt): # Update the asteroid's position based on its velocity and delta time
        self.position += self.velocity * dt # Update position based on velocity and delta time
    
    def split(self): # Split the asteroid into smaller ones
        self.kill() # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS: # If the asteroid is already at the minimum radius, do not split further
            return  # Exit the split method if the asteroid is too small
        random_angle = random.uniform(20, 50) # Randomize the angle for splitting

        a = self.velocity.rotate(random_angle) # Rotate the velocity by the random angle
        b = self.velocity.rotate(-random_angle) # Rotate the velocity in the opposite direction

        new_radius = self.radius - ASTEROID_MIN_RADIUS # Calculate the new radius for the smaller asteroids
        asteroid = Asteroid(self.position.x, self.position.y, new_radius) # Create the first smaller asteroid
        asteroid.velocity = a * 1.2 # Set its velocity
        asteroid = Asteroid(self.position.x, self.position.y, new_radius) # Create the second smaller asteroid
        asteroid.velocity = b * 1.2 # Set its velocity