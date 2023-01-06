import pygame

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
bg_image = pygame.image.load('Assets/Images/bg.jpg').convert()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

def playerAnimation():
    global player_index, player_image, players
    player_index += 0.15
    player_image = players[int(player_index) % 3]




players = []
player_walk1 = pygame.image.load('Assets/Images/p1.jpg').convert_alpha()
player_walk1 = pygame.transform.scale(player_walk1, PLAYER_SIZE)
player_walk1.set_colorkey(BLACK)
player_walk2 = pygame.image.load('Assets/Images/p2.jpg').convert_alpha()
player_walk2 = pygame.transform.scale(player_walk2, PLAYER_SIZE)
player_walk2.set_colorkey(BLACK)
player_walk3 = pygame.image.load('Assets/Images/p3.jpg').convert_alpha()
player_walk3 = pygame.transform.scale(player_walk3, PLAYER_SIZE)
player_walk3.set_colorkey(BLACK)
players.append(player_walk1)
players.append(player_walk2)
players.append(player_walk3)
player_index = 0
player_image = players[player_index]

player_dead = pygame.image.load('Assets/Images/pd.jpg').convert_alpha()
player_dead = pygame.transform.scale(player_dead, PLAYER_SIZE)
player_dead.set_colorkey(BLACK)

player_rect = player_image.get_rect(bottomleft = PLAYER_POS)

wall = pygame.image.load('Assets/Images/ww.jpg').convert_alpha()
wall = pygame.transform.scale(wall, WALL_SIZE)
wall.set_colorkey(BLACK)


vwall = pygame.image.load('Assets/Images/vww.jpg').convert_alpha()
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


kata = pygame.image.load('Assets/Images/k22.png').convert_alpha()
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
GAMESTATE = 0
OFFSET = 2
VOFFSET = 6
JUMP = True
LEFT = True
RIGHT = True
DEAD = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if GAMESTATE == 0:
        screen.blit(bg_image, (0, 0))
        for i in range(len(WALL_POS)):
            if len(WALL_POS) - 1 == i:
                screen.blit(vwall, wall_rect[i])
            else :
                screen.blit(wall, wall_rect[i])


        for i in range(len(KATA_POS)):
            screen.blit(kata, kata_rect[i])


        for i in range(len(WALL_POS)):
            j = 0
            if ((player_rect.top <= KATA_POS[i][1] - KATA_SIZE[(j+1)%2] and player_rect.bottom >= KATA_POS[i][
                1]) or (player_rect.top <= KATA_POS[i][1] and player_rect.top >= KATA_POS[i][1] - KATA_SIZE[
                (j+1)%2]) or (player_rect.bottom >= KATA_POS[i][1] - KATA_SIZE[(j+1)%2] and player_rect.bottom <= KATA_POS[i][
                1])) and (player_rect.left > KATA_POS[i][0] - OFFSET and player_rect.left < KATA_POS[i][
                0] + KATA_SIZE[j] + OFFSET):
                DEAD = True


        if DEAD:
            player_dead_rect = player_dead.get_rect(bottomleft=(player_rect.left, player_rect.bottom))
            screen.blit(player_dead, player_dead_rect)
        else:
            screen.blit(player_image, player_rect)


        VELOCITY += GRAVITY
        if player_rect.bottom >= 450:
            player_rect.bottom = 450
            VELOCITY = 0
            JUMP = True
        elif player_rect.top < 0:
            player_rect.top = 0
            VELOCITY = 0
            JUMP = False
        else:
            for i in range(len(WALL_POS)):
                j = 0
                if len(WALL_POS) - 1 == i:
                    j = 1
                if player_rect.bottom >= WALL_POS[i][1]-WALL_SIZE[(j+1)%2]-VOFFSET and player_rect.bottom <= WALL_POS[i][
                    1]-WALL_SIZE[(j+1)%2]+VOFFSET and player_rect.left >= WALL_POS[i][0] - PLAYER_SIZE[
                    0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[0] and VELOCITY > 0:
                    player_rect.bottom = WALL_POS[i][1] - WALL_SIZE[(j+1)%2]
                    VELOCITY = 0
                    JUMP = True
                elif player_rect.top >= WALL_POS[i][1]-VOFFSET and player_rect.top <= WALL_POS[i][
                    1]+VOFFSET and player_rect.left >= WALL_POS[i][0] - PLAYER_SIZE[
                    0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[0] and VELOCITY < 0:
                    player_rect.top = WALL_POS[i][1]
                    VELOCITY = 0
        player_rect.bottom += VELOCITY

        LEFT = True
        if player_rect.left <= 2:
            player_rect.left = 2
            LEFT = False
        for i in range(len(WALL_POS)):
            j = 0
            if len(WALL_POS)-1 == i:
                j = 1
            if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j+1)%2] and player_rect.bottom > WALL_POS[i][
                1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
                (j+1)%2]) or (player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j+1)%2] and player_rect.bottom < WALL_POS[i][
                1])) and (player_rect.left > WALL_POS[i][0] + WALL_SIZE[j] - OFFSET and player_rect.left < WALL_POS[i][
                0] + WALL_SIZE[j] + OFFSET):
                player_rect.left = WALL_POS[i][0] + WALL_SIZE[j]
                LEFT = False

        RIGHT = True
        if player_rect.right >= SCREEN_WIDTH-2:
            player_rect.right = SCREEN_WIDTH-2
            RIGHT = False
        for i in range(len(WALL_POS)):
            j = 0
            if len(WALL_POS) - 1 == i:
                j = 1
            if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j+1)%2] and player_rect.bottom > WALL_POS[i][
                1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
                (j+1)%2]) or (player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j+1)%2] and player_rect.bottom < WALL_POS[i][
                1])) and (player_rect.right > WALL_POS[i][0] - OFFSET and player_rect.right < WALL_POS[i][
                0] + OFFSET):
                player_rect.right = WALL_POS[i][0]
                RIGHT = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and JUMP:
            VELOCITY = -5
            player_rect.bottom -= 1
            JUMP = False
        if keys[pygame.K_LEFT] and LEFT:
            playerAnimation()
            player_rect.left -= 2
        if keys[pygame.K_RIGHT] and RIGHT:
            playerAnimation()
            player_rect.left += 2


    pygame.display.update()
    clock.tick(60)
lock.tick(60)