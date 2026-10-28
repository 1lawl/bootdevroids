from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
         self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            split1_velocity = self.velocity.rotate(angle)
            split2_velocity = self.velocity.rotate(-angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid1.velocity = split1_velocity * 1.2
            asteroid2.velocity = split2_velocity * 1.2
