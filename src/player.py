import pygame
from PIL import Image, ImageDraw, ImageFont

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)  # Hitbox
        self.speed = 5
        self.determination = 100

        # Correct font path for macOS
        font_path = "/System/Library/Fonts/Apple Color Emoji.ttc"
        self.emoji_image = self.render_emoji_as_image("⚡", font_path)

    def render_emoji_as_image(self, emoji, font_path):
        """Render an emoji as an image while keeping its original colors."""
        font = ImageFont.truetype(font_path, 40)
        image = Image.new("RGBA", (50, 50), (0, 0, 0, 0))  # Transparent background
        draw = ImageDraw.Draw(image)
        draw.text((5, 5), emoji, font=font, fill="yellow")  # Keep emoji color
        return pygame.image.fromstring(image.tobytes(), image.size, "RGBA")

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 450:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.emoji_image, self.rect.topleft)
