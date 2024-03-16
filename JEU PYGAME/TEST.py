import pygame
i = 0


def rotate():
    global i
    rotated_sprite = pygame.transform.rotate(sprite_sheet.subsurface(sprite_rect), i)
    rotated_rect = rotated_sprite.get_rect(center=(100, 100))
    screen.blit(rotated_sprite, rotated_rect)
    i += 1


# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotate Sprite")

# Load the sprite sheet image
sprite_sheet = pygame.image.load("SPRITE/UNIT_BASE.png")
bg = pygame.image.load("SPRITE/MAP.png")

# Define the rectangle representing the area of the sprite sheet containing the sprite
sprite_rect = pygame.Rect(0, 0, 320, 320)  # Example rectangle, adjust as needed

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.blit(bg, (0, 0))
    # Rotate the sprite and blit it onto the screen
    rotate()

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    #pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
