import pygame
import math
import map

mapInstance = map.miniMap()

class player:
    def __init__(self):
        self.XPos = 175
        self.YPos = 350
        self.width = 20
        self.height = 20
        self.playersMiddleX = self.XPos + self.width / 2
        self.playersMiddleY = self.YPos + self.height / 2
        self.angle = math.pi    # Python uses radians instead of degrees (pi = 180°)
        self.renderDistance = 500
        self.FOV = math.pi / 3  # pi/3 = 60°
        self.halfFOV = self.FOV / 2
        self.endFOV = self.angle - self.halfFOV
        self.resolution = 70    # Number of rays that will be casted
        self.resolutionStep = self.FOV / self.resolution

        self.playerObject = pygame.Rect(self.XPos, self.YPos, self.width, self.height)
 
    def movements(self, keyPressed):
        keyPressed = pygame.key.get_pressed()
            
        # Forward
        if keyPressed[pygame.K_UP]:
            self.XPos

        # Backward

        # Strafe right

        # Strafe left

    def rotate(self, keyPressed):
        if keyPressed[pygame.K_q]:
            self.angle -= 0.1
        if keyPressed[pygame.K_d]:
            self.angle += 0.1

    def cast(self, screen):
        self.endFOV = self.angle - self.halfFOV
        for aaaa in range(self.resolution):
            for j in range(self.renderDistance):
                targetPosX = self.playersMiddleX - math.sin(self.endFOV) * j
                targetPosY = self.playersMiddleY + math.cos(self.endFOV) * j

                pygame.draw.line(screen, 
                                "green", 
                                (self.playersMiddleX, self.playersMiddleY),
                                (targetPosX, targetPosY), 
                                2)
                
                columnIndex = int(targetPosX / mapInstance.allRectPosAndDim[2])
                rowIndex = int(targetPosY / mapInstance.allRectPosAndDim[2])

                squareIndex = rowIndex * mapInstance.mapSize + columnIndex
                
                if mapInstance.gameMap[squareIndex] == 1:
                    pygame.draw.rect(screen, "purple", (columnIndex * mapInstance.allRectPosAndDim[2], rowIndex * mapInstance.allRectPosAndDim[2], mapInstance.allRectPosAndDim[2] - 2, mapInstance.allRectPosAndDim[2] - 2))
                    break

            self.endFOV += self.resolutionStep