import pygame
import math
import map
import mainObjects

pygame.init()
screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Window 500x500")

# Instance
varMap = map.miniMap()
varPlayer = mainObjects.player()

clock = pygame.time.Clock()

running = True

while running:
    keyPressed = pygame.key.get_pressed()

    # Closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background color
    screen.fill((0, 0, 0))

    # Casting rays
    varPlayer.cast(screen)
    
    # Display map
    varMap.renderMap(screen)
    
    # Display player
    playerDisplay = pygame.draw.rect(screen, "yellow", varPlayer.playerObject, 1)
    pygame.draw.ellipse(screen, "red", varPlayer.playerObject, 10)

    # Player movements
    varPlayer.rotate(keyPressed)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()