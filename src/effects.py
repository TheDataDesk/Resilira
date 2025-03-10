import pygame
import random

class ParticleEffect:
    def __init__(self, x, y):
        """Initialize particle explosion effect when a rock is crushed."""
        self.particles = [
            [x, y, random.randint(-3, 3), random.randint(-3, 3), random.randint(4, 7)]
            for _ in range(10)
        ]  # Each particle has (x, y, x_speed, y_speed, size)

    def update(self):
        """Move and shrink particles."""
        for particle in self.particles:
            particle[0] += particle[2]  # Move in X direction
            particle[1] += particle[3]  # Move in Y direction
            particle[4] -= 0.2  # Shrink over time

        # Remove finished particles
        self.particles = [p for p in self.particles if p[4] > 0]
        return len(self.particles) > 0  # Return False when all particles are gone

    def draw(self, screen):
        """Ensure particles are not affecting UI."""
        for particle in self.particles:
            x, y = int(particle[0]), int(particle[1])

            if y < 50:  # Do not draw if it's too close to UI
                continue

            pygame.draw.circle(screen, (255, 255, 0), (x, y), int(particle[4]))
