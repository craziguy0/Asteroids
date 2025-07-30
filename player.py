import pygame
from constants import *
from circleshape import CircleShape
from Shot import Shot

class Player(CircleShape): # Player class inherits from CircleShape
    def __init__(self, x, y): # Initialize the player at position (x, y)
        super().__init__(x, y, PLAYER_RADIUS) # Call the parent constructor
        self.rotation = 0  # Initial rotation angle
        self.shoot_timer = 0  # Initialize a timer for shooting cooldown
    
    def draw(self, screen): # Draw the player as a triangle on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # Draw the triangle with a white outline

    def triangle(self): # Calculate the triangle vertices based on the player's position and rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # Forward direction based on rotation
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # Right direction for the triangle
        a = self.position + forward * self.radius # Vertex at the front of the triangle
        b = self.position - forward * self.radius - right # Vertex at the back left of the triangle
        c = self.position - forward * self.radius + right # Vertex at the back right of the triangle
        return [a, b, c] # Return the vertices of the triangle as a list


    def update(self, dt): # Update the player's position and rotation based on input
        self.shoot_timer -= dt  # Decrease the timer by the delta time
        keys = pygame.key.get_pressed() # Get the current state of all keys

        if keys[pygame.K_w]:
            self.move(dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right
        if keys[pygame.K_SPACE]:
            self.shoot() # Shoot a projectile
            
    def shoot(self):
        if self.shoot_timer > 0: # If the timer is greater than 0, it means the player cannot shoot yet
            return  # Exit the shoot method if the cooldown is not over
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN # Reset the shooting cooldown timer
        shot = Shot(self.position.x, self.position.y) # Create a shot at the player's position
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED # Set the shot's velocity based on the player's rotation
        


    def move(self, dt): # Move the player forward in the direction of its rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # Forward direction based on rotation
        self.position += forward * PLAYER_SPEED * dt # Move the player in the forward direction scaled by speed and delta time

    def rotate(self, dt): # Rotate the player based on input
        self.rotation += PLAYER_TURN_SPEED * dt # Rotate the player by PLAYER_TURN_SPEED degrees per second scaled by delta time