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
        self.walls = [[0 for x in range(9)] for y in range(9)]

        # Position of the players
        self.players = [(4,8),(4,0)]

        # Number of walls remaining
        self.num_walls = 10

        # Option: 0 move, 1 place vertical wall, 2 place horizontal wall
        self.selection = 0

        # load the images
        self.initGraphics()

    def drawBoard(self):
        # This is under construction
        # Put the board
        self.screen.blit(self.board, [0,0])

        # Put the players
        x_p1, y_p1 = self.players[0]
        x_p2, y_p2 = self.players[1]
        self.screen.blit(self.black, [x_p1*60+14, y_p1*60+13])
        self.screen.blit(self.white, [x_p2*60+14, y_p2*60+13])

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

        mouse_on_board = mouse[0] <= 542

        # Hovering effect if mouse is on board
        if mouse_on_board:
            # If you want to move
            if self.selection==0:
                xpos = int(math.ceil((mouse[0]-3)/60.)-1)
                ypos = int(math.ceil((mouse[1]-3)/60.)-1)
                if self.canmove(0, self.walls, xpos, ypos):
                    self.screen.blit(self.white, [xpos*60 + 14, ypos*60+14])
                    if pygame.mouse.get_pressed()[0]:
                        self.players[0]=(xpos,ypos)
            # If you want to put a vertical wall
            else:
                xpos = int(math.ceil((mouse[0]-34)/60.)-1)
                ypos = int(math.ceil((mouse[1]-34)/60.)-1)
                if self.canputwallin(xpos, ypos):
                    if self.selection==1:
                        self.screen.blit(self.wall_v, [60*xpos+61,60*ypos+6])
                    else:
                        self.screen.blit(self.wall_h, [60*xpos+6,60*ypos+61])

                    if pygame.mouse.get_pressed()[0]:
                        self.walls[ypos][xpos] = self.selection
                        self.num_walls= self.num_walls-1

        # If the mouse is on the menu
        if pygame.mouse.get_pressed()[0] and mouse[0] > 550:
            if mouse[1] > 20 and mouse[1]< 120:
                self.selection=0
            elif mouse[1] > 125 and mouse[1] < 200:
                self.selection=1
            elif mouse[1] > 205 and mouse[1] < 280:
                self.selection=2
        # If the mouse is on the board
        else:
            pass
                    
        
        for event in pygame.event.get():
            # If people want to leave, you know what to do
            if event.type == pygame.QUIT:
                exit()
                
        pygame.display.flip()

    def canputwallin(self,x,y):
        # There are going to be a bunch of test to see if it can put a wall
        there_are_walls = self.num_walls > 0
        in_a_good_position = False
        if x>=0 and x<8 and y>=0 and y <8:
            if self.walls[y][x]==0:
                if self.selection == 1 and self.walls[y+1][x]!=1 and self.walls[y-1][x]!=1:
                    in_a_good_position = True
                elif self.selection == 2 and self.walls[y][x+1]!=2 and self.walls[y][x-1]!=2:
                    in_a_good_position = True

        
        return there_are_walls and in_a_good_position

    def canmove(self, player, board, x, y):
        x_p, y_p = self.players[player]
        canit = False
        if x_p == x:
            if y == y_p + 1 and board[y_p][x] != 2 and board[y_p][x-1] != 2:
                canit = True
            elif y == y_p-1 and board[y][x]!=2 and board[y][x-1] != 2:
                canit = True
        elif y == y_p:
            if x == x_p + 1 and board[y][x_p] !=1 and board[y-1][x_p] != 1:
                canit = True
            elif x==x_p-1 and board[y][x]!=1 and board[y-1][x] !=1:
                canit = True
        return canit

    def cancross(self, player, board):
        canit = False
        goal = set([[i,player*8] for i in range(9)])
        reachable = set(self.players[player])
        finished = False
        while not finished:
            new_reachable = set()
            for place in rechable:
                pass
                
    
qg = QuoridorGame()
while True:
    qg.update()
