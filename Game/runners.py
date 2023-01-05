import pygame

BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
PLAYER_SIZE = (28, 37)
WALL_SIZE = (80, 20)

pygame.display.set_caption("Runners")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
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

player_rect = player_image.get_rect(midbottom = (PLAYER_SIZE[0]/2+0, 300))


wall = pygame.image.load('Assets/Images/ww.jpg').convert_alpha()
wall = pygame.transform.scale(wall, WALL_SIZE)
wall.set_colorkey(BLACK)


WALL_POS = [(0, WALL_SIZE[1]+300),
            (150, WALL_SIZE[1]+240),
            (275, WALL_SIZE[1]+335),
            (400, WALL_SIZE[1]+260),
            (550, WALL_SIZE[1]+150),
            (675, WALL_SIZE[1]+300),
            (500, 100)
            ]

wall_rect = []
for i in range(len(WALL_POS)):
    wall_rect.append(wall.get_rect(midbottom = WALL_POS[i]))


GRAVITY = 0.1
VELOCITY = 0
SIDEMOVE = 2
GAMESTATE = 0
OFFSET = 3
JUMP = True
LEFT = True
RIGHT = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if GAMESTATE == 0:
        screen.blit(bg_image, (0, 0))
        for i in range(len(WALL_POS)):
            screen.blit(wall, wall_rect[i])

        screen.blit(player_image, player_rect)


        VELOCITY += GRAVITY
        if player_rect.bottom >= 450:
            player_rect.bottom = 450
            VELOCITY = 0
            JUMP = True
        else:
            for i in range(len(WALL_POS)):
                if player_rect.bottom >= WALL_POS[i][1] - WALL_SIZE[1] and player_rect.bottom <= WALL_POS[i][
                    1] - WALL_SIZE[1] + 5 and player_rect.left >= WALL_POS[i][0] - WALL_SIZE[0] / 2 - PLAYER_SIZE[
                    0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[0] / 2 + PLAYER_SIZE[0] and VELOCITY > 0:
                    player_rect.bottom = WALL_POS[i][1] - WALL_SIZE[1]
                    VELOCITY = 0
                    JUMP = True
                elif player_rect.top >= WALL_POS[i][1] - 5 and player_rect.top <= WALL_POS[i][
                    1] and player_rect.left >= WALL_POS[i][0] - WALL_SIZE[0] / 2 - PLAYER_SIZE[
                    0] and player_rect.right <= WALL_POS[i][0] + WALL_SIZE[0] / 2 + PLAYER_SIZE[0] and VELOCITY < 0:
                    player_rect.top = WALL_POS[i][1]
                    VELOCITY = 0
        player_rect.bottom += VELOCITY

        LEFT = True
        if player_rect.left <= 2:
            player_rect.left = 2
            LEFT = False
        for i in range(len(WALL_POS)):
            if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[1] and player_rect.bottom > WALL_POS[i][
                1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
                1]) or (player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[1] and player_rect.bottom < WALL_POS[i][
                1])) and (player_rect.left > WALL_POS[i][0] + WALL_SIZE[0] / 2 - OFFSET and player_rect.left < WALL_POS[i][
                0] + WALL_SIZE[0] / 2 + OFFSET):
                player_rect.left = WALL_POS[i][0] + WALL_SIZE[0] / 2
                LEFT = False

        RIGHT = True
        if player_rect.right >= SCREEN_WIDTH-2:
            player_rect.right = SCREEN_WIDTH-2
            RIGHT = False
        for i in range(len(WALL_POS)):
            if ((player_rect.top < WALL_POS[i][1] - WALL_SIZE[1] and player_rect.bottom > WALL_POS[i][
                1]) or (player_rect.top < WALL_POS[i][1] and player_rect.top > WALL_POS[i][1] - WALL_SIZE[
                1]) or (player_rect.bottom > WALL_POS[i][1] - WALL_SIZE[1] and player_rect.bottom < WALL_POS[i][
                1])) and (player_rect.right > WALL_POS[i][0] - WALL_SIZE[0] / 2 - OFFSET and player_rect.right < WALL_POS[i][
                0] - WALL_SIZE[0] / 2 + OFFSET):
                player_rect.right = WALL_POS[i][0] - WALL_SIZE[0] / 2
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