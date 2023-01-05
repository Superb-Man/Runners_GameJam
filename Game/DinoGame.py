import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load("Assets/Dino/DinoRun1.png"),
           pygame.image.load("Assets/Dino/DinoRun2.png"), ]

BG = pygame.image.load("Assets/Other/Track.png")


class Dino:
    xPos = 80
    yPos = 300
    yVel = -3
    yAcc = 1

    def __init__(self):
        self.run_img = RUNNING

        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_index = 0

        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.xPos
        self.dino_rect.y = self.yPos

    def updatePlayer(self, userInput):
        if self.action == 0:
            
        else:



    def run(self):
        if self.step_index > 10:
            self.image = self.run_img[1]
        else:
            self.image = self.run_img[0]

        self.step_index += 1

    def jump(self,yVal):
        if self.step_index > 10:
            self.image = self.run_img[1]
        else:
            self.image = self.run_img[0]

        self.step_index += 1

    def draw(self, SCRN):
        SCRN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


def dinoGame():
    run = True
    clock = pygame.time.Clock()

    player = Dino()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP :
                player.jump(2)


        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed() ;
        #if userInput =
        player.draw(SCREEN)
        player.updatePlayer(userInput)

        clock.tick(60)
        pygame.display.set_caption('Chrome Dino')
        pygame.display.update()


dinoGame()
