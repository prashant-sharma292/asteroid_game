from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        color = (255, 255, 255)
        pygame.draw.circle(surface=screen, color=color, center=self.position, radius=self.radius, width=LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

        
