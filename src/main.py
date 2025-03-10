import pygame
import random
from src.player import Player
from src.obstacle import Obstacle
from src.powerup import PowerUp
from src.game_manager import GameManager
from src.ui import UI
from src.effects import ParticleEffect

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()

# Initialize game components
player = Player(225, 500)
ui = UI()
game_manager = GameManager()
obstacles = []
powerups = []
effects = []  # Store particle effects

running = True
while running:
    screen.fill((0, 0, 0))  # Black background
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move(keys)

    # Spawn obstacles (rocks 🪨)
    if random.randint(0, 50) < game_manager.difficulty:
        obstacles.append(Obstacle(random.randint(0, 450), 0))

    # Spawn power-ups
    if random.randint(0, 300) < game_manager.difficulty:
        powerups.append(PowerUp(random.randint(0, 450), 0))

    # Move & draw obstacles (rocks)
    obstacles_to_remove = []
    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw(screen)

        # Check for collision
        if player.rect.colliderect(obstacle.rect):
            if player.determination >= 50:  # Crush rock if determination is high
                game_manager.score += 10
                effects.append(ParticleEffect(obstacle.rect.centerx, obstacle.rect.centery))
                obstacles_to_remove.append(obstacle)  # Mark for removal
            else:
                game_manager.decrease_determination()  # Reduce determination
                if game_manager.check_game_over():
                    running = False  # Game over
                obstacles_to_remove.append(obstacle)  # Mark for removal

    # Remove collided obstacles after looping
    for obstacle in obstacles_to_remove:
        obstacles.remove(obstacle)

    # Move & draw power-ups
    powerups_to_remove = []
    for powerup in powerups:
        powerup.draw(screen)

        # Check if player collects power-up
        if player.rect.colliderect(powerup.rect):
            game_manager.increase_determination()
            powerups_to_remove.append(powerup)

    # Remove collected power-ups after looping
    for powerup in powerups_to_remove:
        powerups.remove(powerup)

    # Draw effects safely
    effects = [effect for effect in effects if effect.update()]
    for effect in effects:
        effect.draw(screen)

    # Draw UI & Player
    ui.draw(screen, game_manager.score, game_manager.determination)
    player.draw(screen)
    pygame.display.update()
    clock.tick(30)
pygame.quit()
