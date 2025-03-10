import pygame
import random
from PIL import Image, ImageDraw, ImageFont

# Negative self-talk messages
NEGATIVE_SELF_TALK = [
    "I'm not good enough", "I always fail", "I don't belong", "I'm not smart",
    "I'm too weak", "I should quit", "I'm a failure", "Nothing works for me",
    "I can't do this", "Why do I even try?", "Everyone is better than me",
    "I'm not capable", "I don't deserve success", "I'm stuck forever",
    "I'm unlovable", "Why me?", "I can't find a job", "I can't", "I hate myself"
]

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y  
        self.speed = random.randint(3, 6)
        self.text = random.choice(NEGATIVE_SELF_TALK)

        # 🔹 Re-add rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, 60, 60)

        # Load the emoji font
        font_path = "/System/Library/Fonts/Apple Color Emoji.ttc"
        self.emoji_image = self.render_emoji_as_image("🪨", font_path)

        # High-contrast text settings
        self.text_font = pygame.font.SysFont("Liberation Sans", 12)
        self.text_color = (173, 216, 230)  # Light Blue for high contrast

    def render_emoji_as_image(self, emoji, font_path):
        """Render an emoji as an image using Pillow (PIL) while keeping its colors."""
        font = ImageFont.truetype(font_path, 40)
        image = Image.new("RGBA", (60, 60), (0, 0, 0, 0))  
        draw = ImageDraw.Draw(image)
        draw.text((5, 5), emoji, font=font, fill=(255, 255, 255, 255))  
        return pygame.image.fromstring(image.tobytes(), image.size, "RGBA")

    def move(self):
        """Move the obstacle downward and update rect position."""
        self.y += self.speed
        self.x += random.randint(-1, 1)  

        # 🔹 Keep rect in sync with updated x, y position
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Draw the rock emoji and negative self-talk text on the screen."""
        # 🔹 **Ensure we're not drawing an unwanted background**
        #pygame.draw.rect(screen, (0, 0, 0), (self.rect.x, self.rect.y, 60, 60))  # Black rectangle behind the rock

        screen.blit(self.emoji_image, self.rect.topleft)  # Draw 🪨 emoji
        text_surface = self.text_font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 50))  # Place text below the rock
