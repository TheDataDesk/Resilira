class GameManager:
    def __init__(self):
        self.score = 0
        self.difficulty = 1
        self.determination = 100  # Sirisha's determination starts at 100%

    def increase_difficulty(self):
        """Increase difficulty as the player progresses."""
        self.difficulty += 0.1  # Obstacles fall faster
        if self.difficulty > 5:
            self.difficulty = 5  # Cap max difficulty

    def decrease_determination(self, amount=10):
        """Reduce determination when Sirisha is hit."""
        self.determination -= amount
        if self.determination < 0:
            self.determination = 0  # Minimum determination is 0

    def increase_determination(self, amount=10):
        """Increase determination when collecting a power-up."""
        self.determination += amount
        if self.determination > 100:
            self.determination = 100  # Cap max determination at 100%

    def check_game_over(self):
        """Check if the game is over (determination = 0)."""
        return self.determination <= 0
