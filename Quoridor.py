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

        # Walls: 0 means no wall, 1 means vertical wall,
        #        2 means horizontal wall
        self.walls = [[0 for x in range(8)] for y in range(8)]

        # Position of the players
        self.player1 = (4,0)
        self.player2 = (4,8)

        # Number of walls remaining
        self.p1_walls = 10
        self.p2_walls = 10

        # Option: 0 move, 1 place vertical wall, 2 place horizontal wall
        self.selection = 2

        self.walls[0][2]=2
        self.walls[7][2]=2

        # load the images
        self.initGraphics()

    def drawBoard(self):
        # This is under construction
        # Put the board
        self.screen.blit(self.board, [0,0])

        # Put the players
        x_p1, y_p1 = self.player1
        x_p2, y_p2 = self.player2
        self.screen.blit(self.black, [x_p1*60+13, y_p1*60+13])
        self.screen.blit(self.white, [x_p2*60+13, y_p2*60+13])

        for x in range(8):
            for y in range(8):
                if self.walls[y][x]!=0:
                    # If there is a vertical wall
                    if self.walls[y][x]==1:
                        self.screen.blit(self.wall_v, [60*x+61,60*y+6])
                    else:
                        self.screen.blit(self.wall_h, [60*x+6,60*y+61])

    def drawSide(self):

        myfont = pygame.font.Font(None,32)

        move = myfont.render('Mueve ficha', 1, (255,255,255))
        v_wall = myfont.render('Pon Muro Vertical', 1, (255,255,255))
        h_wall = myfont.render('Pon Muro Horizontal', 1, (255,255,255))

        self.screen.blit(move, [635,60])
        self.screen.blit(v_wall, [611,140])
        self.screen.blit(h_wall, [600,220])

        self.screen.blit(self.wall_h, [645, 80*self.selection + 85])
    

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
        self.drawSide()

        mouse = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] and mouse[0] > 550:
            if mouse[1] > 20 and mouse[1]< 120:
                self.selection=0
            elif mouse[1] > 125 and mouse[1] < 200:
                self.selection=1
            elif mouse[1] > 205 and mouse[1] < 280:
                self.selection=2
                    
        
        for event in pygame.event.get():
            # If people want to leave, you know what to do
            if event.type == pygame.QUIT:
                exit()
                
        pygame.display.flip()

qg = QuoridorGame()
while True:
    qg.update()
