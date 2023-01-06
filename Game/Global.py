import pygame
from Danger_level import Danger
pygame.init()
BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
PLAYER_SIZE = (28, 37)
WALL_SIZE = (80, 20)
VWALL_SIZE = (20,80)
KATA_SIZE = (20, 36)
PLAYER_POS = (0, 180)

pygame.display.set_caption("Runners")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
bg_image = pygame.image.load('Game/Assets/Images/bg.jpg').convert()
bg_image = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))

#font
font=pygame.font.Font(None,40)

def gamestate(state):
    if state==0:
        print("yeah")
        state_font=font.render(f'{state+1}. Simple',False,'white')
        state_font_rect=state_font.get_rect(center=(100,50))
        screen.blit(state_font,state_font_rect)
def playerAnimation():
    global player_index, player_image, players
    player_index += 0.15
    player_image = players[int(player_index) % 3]




players = []
player_walk1 = pygame.image.load('Game/Assets/Images/p1.jpg').convert_alpha()
player_walk1 = pygame.transform.scale(player_walk1, PLAYER_SIZE)
player_walk1.set_colorkey(BLACK)
player_walk2 = pygame.image.load('Game/Assets/Images/p2.jpg').convert_alpha()
player_walk2 = pygame.transform.scale(player_walk2, PLAYER_SIZE)
player_walk2.set_colorkey(BLACK)
player_walk3 = pygame.image.load('Game/Assets/Images/p3.jpg').convert_alpha()
player_walk3 = pygame.transform.scale(player_walk3, PLAYER_SIZE)
player_walk3.set_colorkey(BLACK)
players.append(player_walk1)
players.append(player_walk2)
players.append(player_walk3)
player_index = 0
player_image = players[player_index]

player_dead = pygame.image.load('Game/Assets/Images/pd.jpg').convert_alpha()
player_dead = pygame.transform.scale(player_dead, PLAYER_SIZE)
player_dead.set_colorkey(BLACK)
player_dead_list=[]
player_rect = player_image.get_rect(bottomleft = PLAYER_POS)

wall = pygame.image.load('Game/Assets/Images/ww.jpg').convert_alpha()
wall = pygame.transform.scale(wall, WALL_SIZE)
wall.set_colorkey(BLACK)


vwall = pygame.image.load('Game/Assets/Images/vww.jpg').convert_alpha()
vwall = pygame.transform.scale(vwall, VWALL_SIZE)
vwall.set_colorkey(BLACK)

WALL_POS = [(0, 200),
            (140, 320),
            (265, 125),
            (400, 260),
            (550, 150),
            (625, 300),
            (450,450)
            ]

wall_rect = []
for i in range(len(WALL_POS)):
    if i== len(WALL_POS) - 1 :
        wall_rect.append(vwall.get_rect(bottomleft = WALL_POS[i]))
    else:
        wall_rect.append(wall.get_rect(bottomleft = WALL_POS[i]))


kata = pygame.image.load('Game/Assets/Images/k22.png').convert_alpha()
kata = pygame.transform.scale(kata, KATA_SIZE)
# kata.set_colorkey(BLACK)

KATA_POS = []

kata_rect = []

def multipleKata(count, bottomLeftX, bottomLeftY, vertical):
    for i in range(count):
        KATA_POS.append((bottomLeftX, bottomLeftY))
        kata_rect.append(kata.get_rect(bottomleft = (bottomLeftX, bottomLeftY)))
        if not vertical:
            bottomLeftX += KATA_SIZE[0]

multipleKata(3, 0, 450, False)
multipleKata(5, 500, 450, False)

GRAVITY = 0.05
VELOCITY = 0
SIDEMOVE = 2
GAMESTATE =1
OFFSET = 2
VOFFSET = 6
JUMP = True
LEFT = True
RIGHT = True
DEAD = False
FirstTime=False