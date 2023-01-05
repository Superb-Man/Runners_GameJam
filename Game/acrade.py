import pygame
from pygame.locals import *

pygame.init()

scrn_width=500
scrn_height=500

screen=pygame.display.set_mode((scrn_width,scrn_height))
pygame.display.set_caption('Acrade')

# vari
tile=100

# image
sun_img=pygame.image.load('img/sun.png')
bg=pygame.image.load('img/sky.png')

def draw_grid():
    for line in range(0,6):
        pygame.draw.line(screen,(255,255,255),(0,line*tile),(scrn_width, line*tile))
        pygame.draw.line(screen, (255, 255, 255), (line * tile,0), (line * tile, scrn_height))


class world():
     def __init__(self,data):
    #     self.tile_list=[]
    #      dirt_img=pygame.image.load('img/sun.png')
    #     row_count=0
    #     for row in data:
    #         col_count=0
    #         for t in row:
    #             if t==1:
    #                 img=pygame.transform.scale(dirt_img,(tile,tile))
    #                 img_rect=img.get_rect()
    #                 img_rect.x=col_count*tile
    #                 img_rect.y=row_count*tile
    #                 block=(img,img_rect)
    #                 self.tile_list.append(block)
    #             col_count+=1
    #         row_count += 1
        pass

world_data=[
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

# w=world(world_data)

run=True
while run:
    screen.blit(bg,(0,0))
    screen.blit(sun_img,(20,20))

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()
pygame.quit()
