from circleshape import CircleShape
import pygame
import constants
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius == constants.ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(split_angle)
            vector2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_1.velocity = vector1 * 1.2
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_2.velocity = vector2 * 1.2
            
