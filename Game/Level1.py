import pygame
import runners

def lev1():
    runners.screen.blit(runners.door, runners.door_rect)
    runners.screen.blit(runners.button, runners.button_rect)

    # Door open
    if runners.BUTTONPRESS:
        runners.doorOpen()

    # Wall
    for i in range(len(runners.WALL_POS)):
        if len(runners.WALL_POS) - 1 == i:
            runners.screen.blit(runners.vwall, runners.wall_rect[i])
        else:
            runners.screen.blit(runners.wall, runners.wall_rect[i])

    # Kata
    for i in range(len(runners.KATA_POS)):
        runners.screen.blit(runners.kata, runners.kata_rect[i])
    for i in range(len(runners.ULTAKATA_POS)):
        runners.screen.blit(runners.ultakata, runners.ultakata_rect[i])

    # Dead with Kata
    if not runners.DEAD:
        runners.DEAD = runners.kataDeath(runners.KATA_POS)
    if not runners.DEAD:
        runners.DEAD = runners.kataDeath(runners.ULTAKATA_POS)

    # Death Animation/Player Image Load
    if runners.DEAD:
        runners.player_dead_rect = runners.player_dead.get_rect(bottomleft=(runners.player_rect.left, runners.player_rect.bottom))
        runners.dead_image = runners.dead_img[runners.DIRECTION]
        runners.screen.blit(runners.dead_image, runners.player_dead_rect)
        runners.deathAnimation()
    else:
        runners.player_image = runners.players[int(runners.player_index) % 3 + 3 * runners.DIRECTION]
        runners.screen.blit(runners.player_image, runners.player_rect)

    # Vertical Movement
    runners.VELOCITY += runners.GRAVITY
    if runners.player_rect.bottom >= 450:
        runners.player_rect.bottom = 450
        runners.VELOCITY = 0
        runners.JUMP = True
    elif runners.player_rect.top < 0:
        runners.player_rect.top = 0
        runners.VELOCITY = 0
        runners.JUMP = False
    elif runners.player_rect.bottom >= runners.BUTTON_POS[1] - runners.BUTTON_SIZE[1] - runners.VOFFSET and runners.player_rect.bottom <= runners.BUTTON_POS[
        1] - runners.BUTTON_SIZE[1] + runners.VOFFSET and runners.player_rect.left >= runners.BUTTON_POS[0] - runners.PLAYER_SIZE[
        0] and runners.player_rect.right <= runners.BUTTON_POS[0] + runners.BUTTON_SIZE[0] + runners.PLAYER_SIZE[0] and runners.VELOCITY > 0:
        runners.player_rect.bottom = runners.BUTTON_POS[1] - runners.BUTTON_SIZE[1]
        runners.VELOCITY = 0
        runners.JUMP = True
        runners.BUTTONPRESS = True
    elif runners.player_rect.top >= runners.BUTTON_POS[1] - runners.VOFFSET and runners.player_rect.top <= runners.BUTTON_POS[
        1] + runners.VOFFSET and runners.player_rect.left >= runners.BUTTON_POS[0] - runners.PLAYER_SIZE[
        0] and runners.player_rect.right <= runners.BUTTON_POS[0] + runners.BUTTON_SIZE[0] + runners.PLAYER_SIZE[0] and runners.VELOCITY < 0:
        runners.player_rect.top = runners.BUTTON_POS[1]
        runners.VELOCITY = 0
    else:
        for i in range(len(runners.WALL_POS)):
            j = 0
            if len(runners.WALL_POS) - 1 == i:
                j = 1
            if runners.player_rect.bottom >= runners.WALL_POS[i][1] - runners.WALL_SIZE[(j + 1) % 2] - runners.VOFFSET and runners.player_rect.bottom <= \
                    runners.WALL_POS[i][
                        1] - runners.WALL_SIZE[(j + 1) % 2] + runners.VOFFSET and runners.player_rect.left >= runners.WALL_POS[i][0] - \
                    runners.PLAYER_SIZE[
                        0] and runners.player_rect.right <= runners.WALL_POS[i][0] + runners.WALL_SIZE[j] + runners.PLAYER_SIZE[
                0] and runners.VELOCITY > 0:
                runners.player_rect.bottom = runners.WALL_POS[i][1] - runners.WALL_SIZE[(j + 1) % 2]
                runners.VELOCITY = 0
                runners.JUMP = True
            elif runners.player_rect.top >= runners.WALL_POS[i][1] - runners.VOFFSET and runners.player_rect.top <= runners.WALL_POS[i][
                1] + runners.VOFFSET and runners.player_rect.left >= runners.WALL_POS[i][0] - runners.PLAYER_SIZE[
                0] and runners.player_rect.right <= runners.WALL_POS[i][0] + runners.WALL_SIZE[j] + runners.PLAYER_SIZE[0] and runners.VELOCITY < 0:
                runners.player_rect.top = runners.WALL_POS[i][1]
                runners.VELOCITY = 0
    runners.player_rect.bottom += runners.VELOCITY

    # Left Movement
    runners.LEFT = True
    if runners.player_rect.left <= 2:
        runners.player_rect.left = 2
        runners.LEFT = False
    elif ((runners.player_rect.top < runners.BUTTON_POS[1] - runners.BUTTON_SIZE[1] and runners.player_rect.bottom > runners.BUTTON_POS[1]) or (
            runners.player_rect.top < runners.BUTTON_POS[1] and runners.player_rect.top > runners.BUTTON_POS[1] - runners.BUTTON_SIZE[1]) or (
                  runners.player_rect.bottom > runners.BUTTON_POS[1] - runners.BUTTON_SIZE[1] and runners.player_rect.bottom < runners.BUTTON_POS[
              1])) and (
            runners.player_rect.left > runners.BUTTON_POS[0] + runners.BUTTON_SIZE[0] - runners.OFFSET and runners.player_rect.left < runners.BUTTON_POS[
        0] + runners.BUTTON_SIZE[0] + runners.OFFSET):
        runners.player_rect.left = runners.BUTTON_POS[0] + runners.BUTTON_SIZE[0]
        runners.LEFT = False
    for i in range(len(runners.WALL_POS)):
        j = 0
        if len(runners.WALL_POS) - 1 == i:
            j = 1
        if ((runners.player_rect.top < runners.WALL_POS[i][1] - runners.WALL_SIZE[(j + 1) % 2] and runners.player_rect.bottom > runners.WALL_POS[i][
            1]) or (runners.player_rect.top < runners.WALL_POS[i][1] and runners.player_rect.top > runners.WALL_POS[i][1] - runners.WALL_SIZE[
            (j + 1) % 2]) or (
                    runners.player_rect.bottom >runners.WALL_POS[i][1] - runners.WALL_SIZE[(j + 1) % 2] and runners.player_rect.bottom <
                    runners.WALL_POS[i][
                        1])) and (
                runners.player_rect.left > runners.WALL_POS[i][0] + runners.WALL_SIZE[j] - runners.OFFSET and runners.player_rect.left < runners.WALL_POS[i][
            0] + runners.WALL_SIZE[j] + runners.OFFSET):
            runners.player_rect.left = runners.WALL_POS[i][0] + runners.WALL_SIZE[j]
            runners.LEFT = False

    # Right Movement
    runners.RIGHT = True
    if runners.player_rect.right >= runners.SCREEN_WIDTH - 2:
        if (runners.player_rect.top >= runners.DOOR_POS[1] - runners.DOOR_SIZE[1] - runners.OFFSET and runners.player_rect.bottom <= runners.DOOR_POS[
            1] + runners.OFFSET) and runners.SCENESHIFT == False:
            runners.SCENESHIFT = True
        else:
            runners.player_rect.right = runners.SCREEN_WIDTH - 2
            runners.RIGHT = False

    elif ((runners.player_rect.top < runners.BUTTON_POS[1] - runners.BUTTON_SIZE[1] and runners.player_rect.bottom > runners.BUTTON_POS[
        1]) or (runners.player_rect.top < runners.BUTTON_POS[1] and runners.player_rect.top > runners.BUTTON_POS[1] - runners.BUTTON_SIZE[
        1]) or (runners.player_rect.bottom > runners.BUTTON_POS[1] - runners.BUTTON_SIZE[1] and runners.player_rect.bottom < runners.BUTTON_POS[
        1])) and (runners.player_rect.right > runners.BUTTON_POS[0] - runners.OFFSET and runners.player_rect.right < runners.BUTTON_POS[
        0] + runners.OFFSET):
        runners.player_rect.right = runners.BUTTON_POS[0]
        RIGHT = False
    elif ((runners.player_rect.top < runners.door_rect.bottom - runners.DOOR_SIZE[1] and runners.player_rect.bottom > runners.door_rect.bottom) or (
           runners.player_rect.top < runners.door_rect.bottom and runners.player_rect.top > runners.door_rect.bottom - runners.DOOR_SIZE[
        1]) or (runners.player_rect.bottom > runners.door_rect.bottom - runners.DOOR_SIZE[
        1] and runners.player_rect.bottom < runners.door_rect.bottom)) and (
            runners.player_rect.right > runners.DOOR_POS[0] - runners.OFFSET and runners.player_rect.right < runners.DOOR_POS[
        0] + runners.OFFSET):
        runners.player_rect.right = runners.DOOR_POS[0]
        runners.RIGHT = False

    for i in range(len(runners.WALL_POS)):
        j = 0
        if len(runners.WALL_POS) - 1 == i:
            j = 1
        if ((runners.player_rect.top < runners.WALL_POS[i][1] - runners.WALL_SIZE[(j + 1) % 2] and runners.player_rect.bottom > runners.WALL_POS[i][
            1]) or (runners.player_rect.top < runners.WALL_POS[i][1] and runners.player_rect.top > runners.WALL_POS[i][1] - runners.WALL_SIZE[
            (j + 1) % 2]) or (
                    runners.player_rect.bottom > runners.WALL_POS[i][1] - runners.WALL_SIZE[(j + 1) % 2] and runners.player_rect.bottom <
                    runners.WALL_POS[i][
                        1])) and (
                runners.player_rect.right > runners.WALL_POS[i][0] - runners.OFFSET and runners.player_rect.right < runners.WALL_POS[i][
            0] + runners.OFFSET):
            runners.player_rect.right = runners.WALL_POS[i][0]
            runners.RIGHT = False

    # Keys pressed
    keys = pygame.key.get_pressed()

    if runners.LEVEL:
        if not runners.DEAD:
            if keys[pygame.K_UP] and runners.JUMP:
                runners.VELOCITY = -5
                runners.player_rect.bottom -= 1
                runners.JUMP = False
            if keys[pygame.K_LEFT] and runners.LEFT:
                runners.DIRECTION = runners.LEFTDIRECTION
                runners.playerAnimation()
                runners.player_rect.left -= runners.SIDEMOVE
            if keys[pygame.K_RIGHT] and runners.RIGHT:
                runners.DIRECTION = runners.RIGHTDIRECTION
                runners.playerAnimation()
                runners.player_rect.left += runners.SIDEMOVE

