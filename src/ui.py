import pygame

class UI:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 18)  # Standard font

    def draw(self, screen, score, determination):
        """Draws Determination & Score at the top-center of the screen without extra characters."""

        # Ensure values are properly converted to strings and remove any special characters
        score = str(score).strip()
        determination = str(determination).strip()

        # Remove any non-ASCII characters that might cause rendering issues
        text = f"Determination: {determination}%  |  Score: {score}".encode("ascii", "ignore").decode()

        # Render text normally in white for contrast
        text_surface = self.font.render(text, True, (255, 255, 255))

        # Get text width & height to center it
        text_width, text_height = text_surface.get_size()
        screen_width = screen.get_width()

        # Center the text horizontally
        x_position = (screen_width - text_width) // 2

        # 🛑 **FORCE FULL UI CLEAR**
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, 50))  # Blackout full UI area

        # Draw text at the **top center**
        screen.blit(text_surface, (x_position, 20))
