import pygame
pygame.init()

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
DOOR_POS = (790, 220)
CDOOR_POS = (790, 155)
BUTTON_SIZE = (80, 20)
BUTTON_POS = (400, 260)

pygame.display.set_caption("Runners")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
bg_image = pygame.image.load('Assets/Images/bg.jpg').convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

bg_image_rect=bg_image.get_rect()
bg_image_rect.x=0
bg_image_rect.y=0

bg_image1 = bg_image
bg_image1_rect = bg_image1.get_rect()


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
player_rect = player_image.get_rect(bottomleft = PLAYER_POS)

dead_img = []
player_dead = pygame.image.load('Assets/Images/pd.jpg').convert_alpha()
player_dead = pygame.transform.scale(player_dead, PLAYER_SIZE)
player_dead.set_colorkey(BLACK)
dead_img.append(player_dead)
player_dead = pygame.image.load('Assets/Images/prd.jpg').convert_alpha()
player_dead = pygame.transform.scale(player_dead, PLAYER_SIZE)
player_dead.set_colorkey(BLACK)
dead_img.append(player_dead)
dead_image = dead_img[0]
player_dead_rect = dead_image.get_rect(bottomleft = (0, 0))


wall = pygame.image.load('Assets/Images/ww.jpg').convert_alpha()
wall = pygame.transform.scale(wall, WALL_SIZE)
wall.set_colorkey(BLACK)


vwall = pygame.image.load('Assets/Images/vww.jpg').convert_alpha()
vwall = pygame.transform.scale(vwall, VWALL_SIZE)
vwall.set_colorkey(BLACK)

door = pygame.image.load('Assets/Images/door.jpg').convert_alpha()
door = pygame.transform.scale(door, DOOR_SIZE)
door.set_colorkey(BLACK)
door_rect = door.get_rect(bottomleft = DOOR_POS)
cdoor_rect = door.get_rect(bottomleft = CDOOR_POS)

button = pygame.image.load('Assets/Images/b.jpg').convert_alpha()
button = pygame.transform.scale(button, BUTTON_SIZE)
button.set_colorkey(BLACK)
button_rect = button.get_rect(bottomleft = BUTTON_POS)

WALL_POS = [(0, 200), (140, 320),
            (265, 125), (305, 125),
            (615, 120), (625, 300),
            (760, 155), (760, 240),
            (760, 410), (720, 410), 
            (760, 350),
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
kata.set_colorkey(BLACK)
ultakata.set_colorkey(BLACK)

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

def playerAnimation():
    global player_index, player_image, players
    player_index += 0.15

dead_time = 0
def deathAnimation():
    global dead_time, DIRECTION, DEAD
    dead_time += 0.25
    if dead_time >= 20:
        dead_time = 0
        DEAD = False
        DIRECTION = RIGHTDIRECTION
        player_rect.left = PLAYER_POS[0]
        player_rect.bottom = PLAYER_POS[1]

door_index = 0
def doorOpen():
    global door_index, door, door_rect
    door_index += 0.5
    if door_rect.bottom >= CDOOR_POS[1]:
        sz = (int)(door_index)
        door_rect.bottom -= sz
    if door_index > 1:
        door_index = 0

def doorClose():
    global door_index, door, cdoor_rect
    door_index += 0.5
    if cdoor_rect.bottom <= DOOR_POS[1]:
        sz = (int)(door_index)
        cdoor_rect.bottom += sz
    if door_index > 1:
        door_index = 0

def kataDeath(KATA):
    for i in range(len(KATA)):
        j = 0
        if ((player_rect.top <= KATA[i][1] - KATA_SIZE[(j + 1) % 2] and player_rect.bottom >= KATA[i][
            1]) or (player_rect.top <= KATA[i][1] and player_rect.top >= KATA[i][1] - KATA_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom >= KATA[i][1] - KATA_SIZE[(j + 1) % 2] and player_rect.bottom <= KATA[i][
                1])) and (player_rect.right > KATA[i][0] + OFFSET and player_rect.left < KATA[i][
            0] + KATA_SIZE[j] - OFFSET):
            return True
    return False


multipleKata(5, 0, 450)
multipleKata(4, 270, 450)
multipleKata(5, 500, 450)
ultaMultipleKata(5, 267, 155)
ultaMultipleKata(2, 630, 330)
ultaMultipleKata(3, 80, 30)
ultaMultipleKata(4, 680, 30)


GRAVITY = 0.1
LEVEL = 0
VELOCITY = 0
SIDEMOVE = 2
SCENESHIFT = False
OFFSET = 2
VOFFSET = 6
JUMP = True
LEFT = True
RIGHT = True
DEAD = False
DIRECTION = RIGHTDIRECTION
BUTTONPRESS = False
BG = True
BG2 = False

def level1():
    global SCENESHIFT, door_rect, BUTTONPRESS, DEAD, DIRECTION, VELOCITY, JUMP, BG, RIGHT, player_rect, SCREEN_WIDTH
    screen.blit(door, door_rect)
    screen.blit(button, button_rect)

    # Door open
    if BUTTONPRESS:
        doorOpen()

    # Wall
    for i in range(len(WALL_POS)):
        if len(WALL_POS) - 1 == i:
            screen.blit(vwall, wall_rect[i])
        else:
            screen.blit(wall, wall_rect[i])

    # Kata
    for i in range(len(KATA_POS)):
        screen.blit(kata, kata_rect[i])
    for i in range(len(ULTAKATA_POS)):
        screen.blit(ultakata, ultakata_rect[i])

    # Dead with Kata
    if not DEAD:
        DEAD = kataDeath(KATA_POS)
    if not DEAD:
        DEAD = kataDeath(ULTAKATA_POS)

    # Death Animation/Player Image Load
    if DEAD:
        player_dead_rect = player_dead.get_rect(bottomleft=(player_rect.left, player_rect.bottom))
        dead_image = dead_img[DIRECTION]
        screen.blit(dead_image, player_dead_rect)
        deathAnimation()
    else:
        player_image = players[int(player_index) % 3 + 3 * DIRECTION]
        screen.blit(player_image, player_rect)

    # Vertical Movement
    VELOCITY += GRAVITY
    if player_rect.bottom >= 450:
        player_rect.bottom = 450
        VELOCITY = 0
        JUMP = True
    elif player_rect.top < 0:
        player_rect.top = 0
        VELOCITY = 0
        JUMP = False
    elif player_rect.bottom >= BUTTON_POS[1] - BUTTON_SIZE[1] - VOFFSET and player_rect.bottom <= BUTTON_POS[
        1] - BUTTON_SIZE[1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY > 0:
        player_rect.bottom = BUTTON_POS[1] - BUTTON_SIZE[1]
        VELOCITY = 0
        JUMP = True
        BUTTONPRESS = True
    elif player_rect.top >= BUTTON_POS[1] - VOFFSET and player_rect.top <= BUTTON_POS[
        1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY < 0:
        player_rect.top = BUTTON_POS[1]
        VELOCITY = 0
    else:
        for i in range(len(WALL_POS)):
            j = 0
            if len(WALL_POS) - 1 == i:
                j = 1
            if player_rect.bottom >= WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] - VOFFSET and player_rect.bottom <= \
                    WALL_POS[i][
                        1] - WALL_SIZE[(j + 1) % 2] + VOFFSET and player_rect.left >= WALL_POS[i][0] - \
                    PLAYER_SIZE[
                        0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[
                0] and VELOCITY > 0:
                player_rect.bottom = WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2]
                VELOCITY = 0
                JUMP = True
            elif player_rect.top >= WALL_POS[i][1] - VOFFSET and player_rect.top <= WALL_POS[i][
                1] + VOFFSET and player_rect.left >= WALL_POS[i][0] - PLAYER_SIZE[
                0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[0] and VELOCITY < 0:
                player_rect.top = WALL_POS[i][1]
                VELOCITY = 0
    player_rect.bottom += VELOCITY

    # Left Movement
    LEFT = True
    if player_rect.left <= 2:
        player_rect.left = 2
        LEFT = False
    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[1]) or (
            player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[1]) or (
                    player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
                1])) and (
            player_rect.left > BUTTON_POS[0] + BUTTON_SIZE[0] - OFFSET and player_rect.left < BUTTON_POS[
        0] + BUTTON_SIZE[0] + OFFSET):
        player_rect.left = BUTTON_POS[0] + BUTTON_SIZE[0]
        LEFT = False
    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.left > WALL_POS[i][0] + WALL_SIZE[j] - OFFSET and player_rect.left < WALL_POS[i][
            0] + WALL_SIZE[j] + OFFSET):
            player_rect.left = WALL_POS[i][0] + WALL_SIZE[j]
            LEFT = False

    # Right Movement
    RIGHT = True
    if player_rect.right >= SCREEN_WIDTH - 2:
        if (player_rect.top >= DOOR_POS[1] - DOOR_SIZE[1] - OFFSET and player_rect.bottom <= DOOR_POS[
            1] + OFFSET) and SCENESHIFT == False:
            SCENESHIFT = True
        else:
            player_rect.right = SCREEN_WIDTH - 2
            RIGHT = False

    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[
        1]) or (player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[
        1]) or (player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
        1])) and (player_rect.right > BUTTON_POS[0] - OFFSET and player_rect.right < BUTTON_POS[
        0] + OFFSET):
        player_rect.right = BUTTON_POS[0]
        RIGHT = False
    elif ((player_rect.top < door_rect.bottom - DOOR_SIZE[1] and player_rect.bottom > door_rect.bottom) or (
            player_rect.top < door_rect.bottom and player_rect.top > door_rect.bottom - DOOR_SIZE[
        1]) or (player_rect.bottom > door_rect.bottom - DOOR_SIZE[
        1] and player_rect.bottom < door_rect.bottom)) and (
            player_rect.right > DOOR_POS[0] - OFFSET and player_rect.right < DOOR_POS[
        0] + OFFSET):
        player_rect.right = DOOR_POS[0]
        RIGHT = False

    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.right > WALL_POS[i][0] - OFFSET and player_rect.right < WALL_POS[i][
            0] + OFFSET):
            player_rect.right = WALL_POS[i][0]
            RIGHT = False

    # Keys pressed
    keys = pygame.key.get_pressed()

    if not DEAD:
        if keys[pygame.K_UP] and JUMP:
            VELOCITY = -5
            player_rect.bottom -= 1
            JUMP = False
        if keys[pygame.K_LEFT] and LEFT:
            DIRECTION = LEFTDIRECTION
            playerAnimation()
            player_rect.left -= SIDEMOVE
        if keys[pygame.K_RIGHT] and RIGHT:
            DIRECTION = RIGHTDIRECTION
            playerAnimation()
            player_rect.left += SIDEMOVE
 
def level2():
    global SCENESHIFT, cdoor_rect, BUTTONPRESS, DEAD, DIRECTION, VELOCITY, JUMP, BG, RIGHT, player_rect, SCREEN_WIDTH

    screen.blit(door, cdoor_rect)
    screen.blit(button, button_rect)

    # Door open
    if BUTTONPRESS:
        doorClose()

    # Wall
    for i in range(len(WALL_POS)):
        if len(WALL_POS)-1 == i:
            screen.blit(vwall, wall_rect[i])
        else:
            screen.blit(wall, wall_rect[i])

    # Kata
    for i in range(len(KATA_POS)):
        screen.blit(kata, kata_rect[i])
    for i in range(len(ULTAKATA_POS)):
        screen.blit(ultakata, ultakata_rect[i])

    # Dead with Kata
    if not DEAD:
        DEAD = kataDeath(KATA_POS)
    if not DEAD:
        DEAD = kataDeath(ULTAKATA_POS)

    # Death Animation/Player Image Load
    if DEAD:
        player_dead_rect = player_dead.get_rect(bottomleft=(player_rect.left, player_rect.bottom))
        dead_image = dead_img[DIRECTION]
        screen.blit(dead_image, player_dead_rect)
        deathAnimation()
        cdoor_rect = door.get_rect(bottomleft = CDOOR_POS)
        BUTTONPRESS = False
    else:
        player_image = players[int(player_index) % 3 + 3 * DIRECTION]
        screen.blit(player_image, player_rect)

    # Vertical Movement
    VELOCITY += GRAVITY
    if player_rect.bottom >= 450:
        player_rect.bottom = 450
        VELOCITY = 0
        JUMP = True
    elif player_rect.top < 0:
        player_rect.top = 0
        VELOCITY = 0
        JUMP = False
    elif player_rect.bottom >= BUTTON_POS[1] - BUTTON_SIZE[1] - VOFFSET and player_rect.bottom <= BUTTON_POS[
        1] - BUTTON_SIZE[1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY > 0:
        player_rect.bottom = BUTTON_POS[1] - BUTTON_SIZE[1]
        VELOCITY = 0
        JUMP = True
        BUTTONPRESS = True
    elif player_rect.top >= BUTTON_POS[1] - VOFFSET and player_rect.top <= BUTTON_POS[
        1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY < 0:
        player_rect.top = BUTTON_POS[1]
        VELOCITY = 0
    else:
        for i in range(len(WALL_POS)):
            j = 0
            if len(WALL_POS) - 1 == i:
                j = 1
            if player_rect.bottom >= WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] - VOFFSET and player_rect.bottom <= \
                    WALL_POS[i][
                        1] - WALL_SIZE[(j + 1) % 2] + VOFFSET and player_rect.left >= WALL_POS[i][0] - \
                    PLAYER_SIZE[
                        0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[
                0] and VELOCITY > 0:
                player_rect.bottom = WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2]
                VELOCITY = 0
                JUMP = True
            elif player_rect.top >= WALL_POS[i][1] - VOFFSET and player_rect.top <= WALL_POS[i][
                1] + VOFFSET and player_rect.left >= WALL_POS[i][0] - PLAYER_SIZE[
                0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[0] and VELOCITY < 0:
                player_rect.top = WALL_POS[i][1]
                VELOCITY = 0
    player_rect.bottom += VELOCITY

    # Left Movement
    LEFT = True
    if player_rect.left <= 2:
        player_rect.left = 2
        LEFT = False
    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[1]) or (
            player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[1]) or (
                    player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
                1])) and (
            player_rect.left > BUTTON_POS[0] + BUTTON_SIZE[0] - OFFSET and player_rect.left < BUTTON_POS[
        0] + BUTTON_SIZE[0] + OFFSET):
        player_rect.left = BUTTON_POS[0] + BUTTON_SIZE[0]
        LEFT = False
    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.left > WALL_POS[i][0] + WALL_SIZE[j] - OFFSET and player_rect.left < WALL_POS[i][
            0] + WALL_SIZE[j] + OFFSET):
            player_rect.left = WALL_POS[i][0] + WALL_SIZE[j]
            LEFT = False

    # Right Movement
    RIGHT = True
    if player_rect.right >= SCREEN_WIDTH - 2:
        if (player_rect.top >= DOOR_POS[1] - DOOR_SIZE[1] - OFFSET and player_rect.bottom <= DOOR_POS[
            1] + OFFSET) and SCENESHIFT == False:
            SCENESHIFT = True
        else:
            player_rect.right = SCREEN_WIDTH - 2
            RIGHT = False

    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[
        1]) or (player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[
        1]) or (player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
        1])) and (player_rect.right > BUTTON_POS[0] - OFFSET and player_rect.right < BUTTON_POS[
        0] + OFFSET):
        player_rect.right = BUTTON_POS[0]
        RIGHT = False
    elif ((player_rect.top < cdoor_rect.bottom - DOOR_SIZE[1] and player_rect.bottom > cdoor_rect.bottom) or (
            player_rect.top < cdoor_rect.bottom and player_rect.top > cdoor_rect.bottom - DOOR_SIZE[
        1]) or (player_rect.bottom > cdoor_rect.bottom - DOOR_SIZE[
        1] and player_rect.bottom < cdoor_rect.bottom)) and (
            player_rect.right > CDOOR_POS[0] - OFFSET and player_rect.right < CDOOR_POS[
        0] + OFFSET):
        player_rect.right = CDOOR_POS[0]
        RIGHT = False

    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.right > WALL_POS[i][0] - OFFSET and player_rect.right < WALL_POS[i][
            0] + OFFSET):
            player_rect.right = WALL_POS[i][0]
            RIGHT = False

    # Keys pressed
    keys = pygame.key.get_pressed()

    if not DEAD:
        if keys[pygame.K_UP] and JUMP:
            VELOCITY = -5
            player_rect.bottom -= 1
            JUMP = False
        if keys[pygame.K_LEFT] and LEFT:
            DIRECTION = LEFTDIRECTION
            playerAnimation()
            player_rect.left -= SIDEMOVE
        if keys[pygame.K_RIGHT] and RIGHT:
            DIRECTION = RIGHTDIRECTION
            playerAnimation()
            player_rect.left += SIDEMOVE

def level3():
    global GRAVITY, SCENESHIFT, door_rect, BUTTONPRESS, DEAD, DIRECTION, VELOCITY, JUMP, BG, RIGHT, player_rect, SCREEN_WIDTH
    GRAVITY = 0.05
    screen.blit(door, door_rect)
    screen.blit(button, button_rect)

    # Door open
    if BUTTONPRESS:
        doorOpen()

    # Wall
    for i in range(len(WALL_POS)):
        if len(WALL_POS) - 1 == i:
            screen.blit(vwall, wall_rect[i])
        else:
            screen.blit(wall, wall_rect[i])

    # Kata
    for i in range(len(KATA_POS)):
        screen.blit(kata, kata_rect[i])
    for i in range(len(ULTAKATA_POS)):
        screen.blit(ultakata, ultakata_rect[i])

    # Dead with Kata
    if not DEAD:
        DEAD = kataDeath(KATA_POS)
    if not DEAD:
        DEAD = kataDeath(ULTAKATA_POS)

    # Death Animation/Player Image Load
    if DEAD:
        player_dead_rect = player_dead.get_rect(bottomleft=(player_rect.left, player_rect.bottom))
        dead_image = dead_img[DIRECTION]
        screen.blit(dead_image, player_dead_rect)
        deathAnimation()
    else:
        player_image = players[int(player_index) % 3 + 3 * DIRECTION]
        screen.blit(player_image, player_rect)

    # Vertical Movement
    VELOCITY += GRAVITY
    if player_rect.bottom >= 450:
        player_rect.bottom = 450
        VELOCITY = 0
        JUMP = True
    elif player_rect.top < 0:
        player_rect.top = 0
        VELOCITY = 0
        JUMP = False
    elif player_rect.bottom >= BUTTON_POS[1] - BUTTON_SIZE[1] - VOFFSET and player_rect.bottom <= BUTTON_POS[
        1] - BUTTON_SIZE[1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY > 0:
        player_rect.bottom = BUTTON_POS[1] - BUTTON_SIZE[1]
        VELOCITY = 0
        JUMP = True
        BUTTONPRESS = True
    elif player_rect.top >= BUTTON_POS[1] - VOFFSET and player_rect.top <= BUTTON_POS[
        1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY < 0:
        player_rect.top = BUTTON_POS[1]
        VELOCITY = 0
    else:
        for i in range(len(WALL_POS)):
            j = 0
            if len(WALL_POS) - 1 == i:
                j = 1
            if player_rect.bottom >= WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] - VOFFSET and player_rect.bottom <= \
                    WALL_POS[i][
                        1] - WALL_SIZE[(j + 1) % 2] + VOFFSET and player_rect.left >= WALL_POS[i][0] - \
                    PLAYER_SIZE[
                        0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[
                0] and VELOCITY > 0:
                player_rect.bottom = WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2]
                VELOCITY = 0
                JUMP = True
            elif player_rect.top >= WALL_POS[i][1] - VOFFSET and player_rect.top <= WALL_POS[i][
                1] + VOFFSET and player_rect.left >= WALL_POS[i][0] - PLAYER_SIZE[
                0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[0] and VELOCITY < 0:
                player_rect.top = WALL_POS[i][1]
                VELOCITY = 0
    player_rect.bottom += VELOCITY

    # Left Movement
    LEFT = True
    if player_rect.left <= 2:
        player_rect.left = 2
        LEFT = False
    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[1]) or (
            player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[1]) or (
                    player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
                1])) and (
            player_rect.left > BUTTON_POS[0] + BUTTON_SIZE[0] - OFFSET and player_rect.left < BUTTON_POS[
        0] + BUTTON_SIZE[0] + OFFSET):
        player_rect.left = BUTTON_POS[0] + BUTTON_SIZE[0]
        LEFT = False
    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.left > WALL_POS[i][0] + WALL_SIZE[j] - OFFSET and player_rect.left < WALL_POS[i][
            0] + WALL_SIZE[j] + OFFSET):
            player_rect.left = WALL_POS[i][0] + WALL_SIZE[j]
            LEFT = False

    # Right Movement
    RIGHT = True
    if player_rect.right >= SCREEN_WIDTH - 2:
        if (player_rect.top >= DOOR_POS[1] - DOOR_SIZE[1] - OFFSET and player_rect.bottom <= DOOR_POS[
            1] + OFFSET) and SCENESHIFT == False:
            SCENESHIFT = True
        else:
            player_rect.right = SCREEN_WIDTH - 2
            RIGHT = False

    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[
        1]) or (player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[
        1]) or (player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
        1])) and (player_rect.right > BUTTON_POS[0] - OFFSET and player_rect.right < BUTTON_POS[
        0] + OFFSET):
        player_rect.right = BUTTON_POS[0]
        RIGHT = False
    elif ((player_rect.top < door_rect.bottom - DOOR_SIZE[1] and player_rect.bottom > door_rect.bottom) or (
            player_rect.top < door_rect.bottom and player_rect.top > door_rect.bottom - DOOR_SIZE[
        1]) or (player_rect.bottom > door_rect.bottom - DOOR_SIZE[
        1] and player_rect.bottom < door_rect.bottom)) and (
            player_rect.right > DOOR_POS[0] - OFFSET and player_rect.right < DOOR_POS[
        0] + OFFSET):
        player_rect.right = DOOR_POS[0]
        RIGHT = False

    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.right > WALL_POS[i][0] - OFFSET and player_rect.right < WALL_POS[i][
            0] + OFFSET):
            player_rect.right = WALL_POS[i][0]
            RIGHT = False

    # Keys pressed
    keys = pygame.key.get_pressed()

    if not DEAD:
        if keys[pygame.K_UP] and JUMP:
            VELOCITY = -5
            player_rect.bottom -= 1
            JUMP = False
        if keys[pygame.K_LEFT] and LEFT:
            DIRECTION = LEFTDIRECTION
            playerAnimation()
            player_rect.left -= SIDEMOVE
        if keys[pygame.K_RIGHT] and RIGHT:
            DIRECTION = RIGHTDIRECTION
            playerAnimation()
            player_rect.left += SIDEMOVE

def level4():
    global GRAVITY, SCENESHIFT, door_rect, BUTTONPRESS, DEAD, DIRECTION, VELOCITY, JUMP, BG, RIGHT, player_rect, SCREEN_WIDTH
    GRAVITY = -0.08
    screen.blit(door, door_rect)
    screen.blit(button, button_rect)

    # Door open
    if BUTTONPRESS:
        doorOpen()

    # Wall
    for i in range(len(WALL_POS)):
        if len(WALL_POS) - 1 == i:
            screen.blit(vwall, wall_rect[i])
        else:
            screen.blit(wall, wall_rect[i])

    # Kata
    for i in range(len(KATA_POS)):
        screen.blit(kata, kata_rect[i])
    for i in range(len(ULTAKATA_POS)):
        screen.blit(ultakata, ultakata_rect[i])

    # Dead with Kata
    if not DEAD:
        DEAD = kataDeath(KATA_POS)
    if not DEAD:
        DEAD = kataDeath(ULTAKATA_POS)

    # Death Animation/Player Image Load
    if DEAD:
        player_dead_rect = player_dead.get_rect(bottomleft=(player_rect.left, player_rect.bottom))
        dead_image = dead_img[DIRECTION]
        screen.blit(dead_image, player_dead_rect)
        deathAnimation()
    else:
        player_image = players[int(player_index) % 3 + 3 * DIRECTION]
        screen.blit(player_image, player_rect)

    # Vertical Movement
    VELOCITY += GRAVITY
    if player_rect.bottom >= 450:
        player_rect.bottom = 450
        VELOCITY = 0
        JUMP = False
    elif player_rect.top < 0:
        player_rect.top = 0
        VELOCITY = 0
        JUMP = True
    elif player_rect.bottom >= BUTTON_POS[1] - BUTTON_SIZE[1] - VOFFSET and player_rect.bottom <= BUTTON_POS[
        1] - BUTTON_SIZE[1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY > 0:
        player_rect.bottom = BUTTON_POS[1] - BUTTON_SIZE[1]
        VELOCITY = 0
        JUMP = True
        BUTTONPRESS = True
    elif player_rect.top >= BUTTON_POS[1] - VOFFSET and player_rect.top <= BUTTON_POS[
        1] + VOFFSET and player_rect.left >= BUTTON_POS[0] - PLAYER_SIZE[
        0] and player_rect.right <= BUTTON_POS[0] + BUTTON_SIZE[0] + PLAYER_SIZE[0] and VELOCITY < 0:
        player_rect.top = BUTTON_POS[1]
        VELOCITY = 0
    else:
        for i in range(len(WALL_POS)):
            j = 0
            if len(WALL_POS) - 1 == i:
                j = 1
            if player_rect.bottom >= WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] - VOFFSET and player_rect.bottom <= \
                    WALL_POS[i][
                        1] - WALL_SIZE[(j + 1) % 2] + VOFFSET and player_rect.left >= WALL_POS[i][0] - \
                    PLAYER_SIZE[
                        0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[
                0] and VELOCITY > 0:
                player_rect.bottom = WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2]
                VELOCITY = 0
                JUMP = False
            elif player_rect.top >= WALL_POS[i][1] - VOFFSET and player_rect.top <= WALL_POS[i][
                1] + VOFFSET and player_rect.left >= WALL_POS[i][0] - PLAYER_SIZE[
                0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[j] + PLAYER_SIZE[0] and VELOCITY < 0:
                player_rect.top = WALL_POS[i][1]
                VELOCITY = 0
                JUMP = True
    player_rect.bottom += VELOCITY

    # Left Movement
    LEFT = True
    if player_rect.left <= 2:
        player_rect.left = 2
        LEFT = False
    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[1]) or (
            player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[1]) or (
                    player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
                1])) and (
            player_rect.left > BUTTON_POS[0] + BUTTON_SIZE[0] - OFFSET and player_rect.left < BUTTON_POS[
        0] + BUTTON_SIZE[0] + OFFSET):
        player_rect.left = BUTTON_POS[0] + BUTTON_SIZE[0]
        LEFT = False
    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.left > WALL_POS[i][0] + WALL_SIZE[j] - OFFSET and player_rect.left < WALL_POS[i][
            0] + WALL_SIZE[j] + OFFSET):
            player_rect.left = WALL_POS[i][0] + WALL_SIZE[j]
            LEFT = False

    # Right Movement
    RIGHT = True
    if player_rect.right >= SCREEN_WIDTH - 2:
        if (player_rect.top >= DOOR_POS[1] - DOOR_SIZE[1] - OFFSET and player_rect.bottom <= DOOR_POS[
            1] + OFFSET) and SCENESHIFT == False:
            SCENESHIFT = True
        else:
            player_rect.right = SCREEN_WIDTH - 2
            RIGHT = False

    elif ((player_rect.top < BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom > BUTTON_POS[
        1]) or (player_rect.top < BUTTON_POS[1] and player_rect.top > BUTTON_POS[1] - BUTTON_SIZE[
        1]) or (player_rect.bottom > BUTTON_POS[1] - BUTTON_SIZE[1] and player_rect.bottom < BUTTON_POS[
        1])) and (player_rect.right > BUTTON_POS[0] - OFFSET and player_rect.right < BUTTON_POS[
        0] + OFFSET):
        player_rect.right = BUTTON_POS[0]
        RIGHT = False
    elif ((player_rect.top < door_rect.bottom - DOOR_SIZE[1] and player_rect.bottom > door_rect.bottom) or (
            player_rect.top < door_rect.bottom and player_rect.top > door_rect.bottom - DOOR_SIZE[
        1]) or (player_rect.bottom > door_rect.bottom - DOOR_SIZE[
        1] and player_rect.bottom < door_rect.bottom)) and (
            player_rect.right > DOOR_POS[0] - OFFSET and player_rect.right < DOOR_POS[
        0] + OFFSET):
        player_rect.right = DOOR_POS[0]
        RIGHT = False

    for i in range(len(WALL_POS)):
        j = 0
        if len(WALL_POS) - 1 == i:
            j = 1
        if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom > WALL_POS[i][
            1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
            (j + 1) % 2]) or (
                    player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[(j + 1) % 2] and player_rect.bottom <
                    WALL_POS[i][
                        1])) and (
                player_rect.right > WALL_POS[i][0] - OFFSET and player_rect.right < WALL_POS[i][
            0] + OFFSET):
            player_rect.right = WALL_POS[i][0]
            RIGHT = False

    # Keys pressed
    keys = pygame.key.get_pressed()

    if not DEAD:
        if keys[pygame.K_UP] and JUMP:
            VELOCITY = 5
            player_rect.bottom += 1
            JUMP = False
        if keys[pygame.K_LEFT] and LEFT:
            DIRECTION = LEFTDIRECTION
            playerAnimation()
            player_rect.left -= SIDEMOVE
        if keys[pygame.K_RIGHT] and RIGHT:
            DIRECTION = RIGHTDIRECTION
            playerAnimation()
            player_rect.left += SIDEMOVE
         


def play():
    #global GRAVITY, LEVEL, VELOCITY, SIDEMOVE, SCENESHIFT, OFFSET, VOFFSET, JUMP, LEFT, RIGHT,DEAD, DIRECTION, BUTTONPRESS, BG, BG2
    global SCENESHIFT, door_rect, BUTTONPRESS, DEAD, DIRECTION, VELOCITY, JUMP, BG, RIGHT, player_rect, SCREEN_WIDTH

    LEVEL = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if SCENESHIFT == False:
            screen.blit(bg_image, bg_image_rect)
            screen.blit(bg_image1, bg_image1_rect)

            if LEVEL == 1:
                level1()
            elif LEVEL == 2:
                level2()
            elif LEVEL == 3:
                level3()
            elif LEVEL == 4:
                level4()
            
        if SCENESHIFT == True:
            if BG:
                screen.blit(bg_image, bg_image_rect)
                screen.blit(bg_image1, bg_image1_rect)
                bg_image_rect.x = bg_image_rect.x - 10
                bg_image1_rect.x = bg_image_rect.x + SCREEN_WIDTH
                player_rect.x = PLAYER_POS[0]
                player_rect.y = PLAYER_POS[1] - 50
                if bg_image1_rect.x == 0:
                    SCENESHIFT = False
                    door_rect = door.get_rect(bottomleft=DOOR_POS)
                    BUTTONPRESS = False
                    bg_image_rect.x = bg_image1_rect.x + SCREEN_WIDTH
                    BG = False
                    LEVEL += 1
            else:
                screen.blit(bg_image, bg_image_rect)
                screen.blit(bg_image1, bg_image1_rect)
        
                bg_image1_rect.x = bg_image1_rect.x - 10
                bg_image_rect.x = bg_image1_rect.x + SCREEN_WIDTH
                player_rect.x = player_rect.x - 10
                player_rect.x = PLAYER_POS[0]
                player_rect.y = PLAYER_POS[1] - 50
                if bg_image_rect.x == 0:
                    SCENESHIFT = False
                    door_rect = door.get_rect(bottomleft=DOOR_POS)
                    BUTTONPRESS = False
                    bg_image1_rect.x = bg_image_rect.x + SCREEN_WIDTH
                    BG = True
                    LEVEL += 1



        pygame.display.update()

        clock.tick(60)

if __name__ == '__main__':
    play()


