import pygame

RIGHTDIRECTION = 0
LEFTDIRECTION = 1
BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
PLAYER_SIZE = (28, 37)
WALL_SIZE = (40, 20)
VWALL_SIZE = (20,40)
KATA_SIZE = (15, 30)
DOOR_SIZE = (10, 65)
PLAYER_POS = (0, 180)
DOOR_POS = (790, 150)

pygame.display.set_caption("Runners")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
bg_image = pygame.image.load('Assets/Images/bg.jpg').convert()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

def playerAnimation():
    global player_index, player_image, players
    player_index += 0.15


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

player_walk1 = pygame.image.load('Assets/Images/pr1.jpg').convert_alpha()
player_walk1 = pygame.transform.scale(player_walk1, PLAYER_SIZE)
player_walk1.set_colorkey(BLACK)
player_walk2 = pygame.image.load('Assets/Images/pr2.jpg').convert_alpha()
player_walk2 = pygame.transform.scale(player_walk2, PLAYER_SIZE)
player_walk2.set_colorkey(BLACK)
player_walk3 = pygame.image.load('Assets/Images/pr3.jpg').convert_alpha()
player_walk3 = pygame.transform.scale(player_walk3, PLAYER_SIZE)
player_walk3.set_colorkey(BLACK)
players.append(player_walk1)
players.append(player_walk2)
players.append(player_walk3)

dead_img = []
player_dead = pygame.image.load('Assets/Images/pd.jpg').convert_alpha()
player_dead = pygame.transform.scale(player_dead, PLAYER_SIZE)
player_dead.set_colorkey(BLACK)
dead_img.append(player_dead)
player_dead = pygame.image.load('Assets/Images/prd.jpg').convert_alpha()
player_dead = pygame.transform.scale(player_dead, PLAYER_SIZE)
player_dead.set_colorkey(BLACK)
dead_img.append(player_dead)

player_rect = player_image.get_rect(bottomleft = PLAYER_POS)

wall = pygame.image.load('Assets/Images/ww.jpg').convert_alpha()
wall = pygame.transform.scale(wall, WALL_SIZE)
wall.set_colorkey(BLACK)


vwall = pygame.image.load('Assets/Images/vww.jpg').convert_alpha()
vwall = pygame.transform.scale(vwall, VWALL_SIZE)
vwall.set_colorkey(BLACK)

door = pygame.image.load('Assets/Images/door.jpg').convert_alpha()
door = pygame.transform.scale(door, DOOR_SIZE)
door.set_colorkey(BLACK)

WALL_POS = [(0, 200),
            (140, 320),
            (265, 125),
            (400, 260),
            (550, 150),
            (625, 300),
            (760, 170),
            (760, 235),
            (450, 450)
            ]

wall_rect = []
for i in range(len(WALL_POS)):
    if i == len(WALL_POS) - 1 :
        wall_rect.append(vwall.get_rect(bottomleft = WALL_POS[i]))
    else:
        wall_rect.append(wall.get_rect(bottomleft = WALL_POS[i]))


kata = pygame.image.load('Assets/Images/k22.png').convert_alpha()
kata = pygame.transform.scale(kata, KATA_SIZE)
ultakata = pygame.image.load('Assets/Images/uk22.png').convert_alpha()
ultakata = pygame.transform.scale(ultakata, KATA_SIZE)
# kata.set_colorkey(BLACK)

KATA_POS = []
kata_rect = []
ULTAKATA_POS = []
ultakata_rect = []

def multipleKata(count, bottomLeftX, bottomLeftY):
    for i in range(count):
        KATA_POS.append((bottomLeftX, bottomLeftY))
        kata_rect.append(kata.get_rect(bottomleft = (bottomLeftX, bottomLeftY)))
        bottomLeftX += KATA_SIZE[0]

def ultaMultipleKata(count, bottomLeftX, bottomLeftY):
    for i in range(count):
        ULTAKATA_POS.append((bottomLeftX, bottomLeftY))
        ultakata_rect.append(ultakata.get_rect(bottomleft = (bottomLeftX, bottomLeftY)))
        bottomLeftX += KATA_SIZE[0]

multipleKata(3, 0, 450)
multipleKata(5, 500, 450)
ultaMultipleKata(2, 270, 155)
ultaMultipleKata(2, 630, 330)

GRAVITY = 0.1
VELOCITY = 0
SIDEMOVE = 2
GAMESTATE = 0
OFFSET = 2
VOFFSET = 6
JUMP = True
LEFT = True
RIGHT = True
DEAD = False
DEAD_TIME = 0
DIRECTION = RIGHTDIRECTION

#def colide(x , y) :


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if GAMESTATE == 0:
        screen.blit(bg_image, (0, 0))
        screen.blit(door,DOOR_POS)
        for i in range(len(WALL_POS)):
            if len(WALL_POS) - 1 == i:
                screen.blit(vwall, wall_rect[i])
            else :
                screen.blit(wall, wall_rect[i])


        for i in range(len(KATA_POS)):
            screen.blit(kata, kata_rect[i])
        for i in range(len(ULTAKATA_POS)):
            screen.blit(ultakata, ultakata_rect[i])


        for i in range(len(KATA_POS)):
            j = 0
            if ((player_rect.top <= KATA_POS[i][1] - KATA_SIZE[(j+1)%2] and player_rect.bottom >= KATA_POS[i][
                1]) or (player_rect.top <= KATA_POS[i][1] and player_rect.top >= KATA_POS[i][1] - KATA_SIZE[
                (j+1)%2]) or (player_rect.bottom >= KATA_POS[i][1] - KATA_SIZE[(j+1)%2] and player_rect.bottom <= KATA_POS[i][
                1])) and (player_rect.right > KATA_POS[i][0] + OFFSET and player_rect.left < KATA_POS[i][
                0] + KATA_SIZE[j] - OFFSET):
                DEAD = True
        for i in range(len(ULTAKATA_POS)):
            j = 0
            if ((player_rect.top <= ULTAKATA_POS[i][1] - KATA_SIZE[(j+1)%2] and player_rect.bottom >= ULTAKATA_POS[i][
                1]) or (player_rect.top <= ULTAKATA_POS[i][1] and player_rect.top >= ULTAKATA_POS[i][1] - KATA_SIZE[
                (j+1)%2]) or (player_rect.bottom >= ULTAKATA_POS[i][1] - KATA_SIZE[(j+1)%2] and player_rect.bottom <= ULTAKATA_POS[i][
                1])) and (player_rect.right > ULTAKATA_POS[i][0] + OFFSET and player_rect.left < ULTAKATA_POS[i][
                0] + KATA_SIZE[j] - OFFSET):
                DEAD = True


        if DEAD:
            DEAD_TIME += 0.5
            player_dead_rect = player_dead.get_rect(bottomleft=(player_rect.left, player_rect.bottom))
            dead_image = dead_img[DIRECTION]
            screen.blit(dead_image, player_dead_rect)
            if DEAD_TIME >= 20:
                DEAD_TIME = 0
                DEAD = False
                DIRECTION = RIGHTDIRECTION
                player_rect.left = PLAYER_POS[0]
                player_rect.bottom = PLAYER_POS[1]
        else:
            player_image = players[int(player_index) % 3 + 3 * DIRECTION]
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

        if not DEAD:
            if keys[pygame.K_UP] and JUMP:
                VELOCITY = -5
                player_rect.bottom -= 1
                JUMP = False
            # if keys[pygame.K_UP] and JUMP :
            #     for i in range(0 , len(WALL_POS)) :
            #         position = 0
            #         while player_rect.collidepoint(WALL_POS[i]+position) :
            #             position+=1
            #             print('TRUE')
            #             VELOCITY = -5
            #             player_rect.bottom -= 1
            #
            #
            #             if position + WALL_POS[i] > WALL_POS[i] +
            #     JUMP = False
            if keys[pygame.K_LEFT] and LEFT:
                DIRECTION = LEFTDIRECTION
                playerAnimation()
                player_rect.left -= 2
            if keys[pygame.K_RIGHT] and RIGHT:
                DIRECTION = RIGHTDIRECTION
                playerAnimation()
                player_rect.left += 2


    pygame.display.update()

    clock.tick(60)
lock.tick(60)