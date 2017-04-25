import pygame
import math

class QuoridorGame():
    def __init__(self):
        pygame.init()
        width, height = 848, 548

        # initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Quoridor")

        self.clock=pygame.time.Clock()

        # load the images
        self.initGraphics()

    def drawBoard(self):
        # This is under construction
        # Put the board
        self.screen.blit(self.board, [0,0])


    def initGraphics(self):
        self.board = pygame.image.load('tablero.png')
        self.black = pygame.image.load('ficha_negra.png')
        self.white = pygame.image.load('ficha_blanca.png')
        self.wall_v = pygame.image.load('pared_v.png')
        self.wall_h = pygame.image.load('pared_h.png')

    def update(self):
        # make the game 60 fps
        self.clock.tick(60)

        # clear the screen
        self.screen.fill(0)
        self.drawBoard()

        for event in pygame.event.get():
            # If people want to leave, you know what to do
            if event.type == pygame.QUIT:
                exit()
                
        pygame.display.flip()

qg = QuoridorGame()
while True:
    qg.update()