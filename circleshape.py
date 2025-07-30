import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite): # CircleShape class inherits from pygame's Sprite
    """A circle shape with position, velocity, and radius."""
    # This class will be used as a base for other shapes like Player
    # It initializes position, velocity, and radius, and provides a draw method to be overridden
    def __init__(self, x, y, radius): # Initialize the circle shape with position (x, y) and radius
        # If the class has a 'containers' attribute, initialize the sprite with those groups
        # Otherwise, initialize without any groups
        # This allows the class to be used as a sprite in Pygame's sprite system
        # This is useful for grouping sprites for updates and drawing
        # The 'containers' attribute can be set by subclasses to specify which sprite groups the object
        # should belong to
        # This allows for better organization and management of sprites in the game
        # For example, the Player class can set its containers to specific sprite groups
        # to manage its updates and drawing separately from other sprites
        # This is a common pattern in Pygame to allow for flexible sprite management
        
        if hasattr(self, "containers"): # Check if the class has a 'containers' attribute
            super().__init__(self.containers) # Initialize the sprite with the specified groups
        else: # Initialize without any groups
            super().__init__() # Call the parent constructor without groups

        self.position = pygame.Vector2(x, y) # Position of the circle shape
        self.velocity = pygame.Vector2(0, 0) # Velocity of the circle shape
        self.radius = radius # Radius of the circle shape

    def collides_with(self, other): # Check for collision with another circle shape
        return self.position.distance_to(other.position) <= self.radius + other.radius # Return True if the distance between the two shapes is less than the sum of their radii
   
    def draw(self, screen): # Draw the circle shape on the screen
        # sub-classes must override
        pass

    def update(self, dt): # Update the circle shape's position based on its velocity and delta time
        # sub-classes must override
        pass