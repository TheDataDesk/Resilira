import pygame

class PowerUp:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)  # Hitbox
        self.font = pygame.font.SysFont("Liberation Sans", 40)  # Ensure emoji support

    def draw(self, screen):
        text_surface = self.font.render("💪", True, (0, 255, 0))  # Green power-up
        screen.blit(text_surface, self.rect.topleft)
