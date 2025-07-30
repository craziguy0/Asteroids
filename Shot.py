import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape): # Shot class inherits from CircleShape
    def __init__(self, x, y): # Initialize the shot at position (x, y)
        super().__init__(x, y, SHOT_RADIUS) # Call the parent constructor
    
    def draw(self, screen): # Draw the shot as a circle on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # Draw the circle with a white outline
    
    def update(self, dt): # Update the shot's position based on its velocity
        self.position += self.velocity * dt # Update the shot's position based on its velocity and delta time