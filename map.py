import pygame


class miniMap:
    def __init__(self):

        self.wallColor = (255, 255, 255)
        self.allRectPosAndDim = [0, 0, 50, 50]
        self.wallWidth = 3
        self.spaceColor = (75, 75, 75)
        self.spaceWidth = 1
        self.mapSize = 10

        _ = 0
        self.gameMap = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, _, _, _, _, _, _, _, _, 1,
            1, _, 1, 1, 1, _, _, _, _, 1,
            1, _, _, _, 1, _, _, _, _, 1,
            1, _, 1, 1, 1, _, 1, 1, _, 1,
            1, _, _, _, _, _, _, _, _, 1,
            1, _, _, _, _, 1, 1, 1, _, 1,
            1, _, _, _, _, _, _, _, _, 1,
            1, _, _, _, _, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        ]


    def renderMap(self, screen):
        xStep = 0
        yStep = 0
        
        for line in range(0, len(self.gameMap), 10):
            iterator = self.gameMap[line:line+10]
            xStep = 0
            for number in iterator:
                if number == 0:
                    pygame.draw.rect(screen, self.spaceColor,
                                     [self.allRectPosAndDim[0] + xStep,
                                      self.allRectPosAndDim[1] + yStep,
                                      self.allRectPosAndDim[2],
                                      self.allRectPosAndDim[3]],
                                     self.spaceWidth)

                if number == 1:
                    pygame.draw.rect(screen, self.wallColor,
                                     [self.allRectPosAndDim[0] + xStep,
                                      self.allRectPosAndDim[1] + yStep,
                                      self.allRectPosAndDim[2],
                                      self.allRectPosAndDim[3]],
                                     self.wallWidth)
                xStep += 50
            yStep += 50

