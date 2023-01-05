import pygame;
from sys import exit
from random import randint
pygame.init()

def Score():
    score=int(pygame.time.get_ticks()/1000)-start_time
    font_surface=font.render(f'{score}',False,(64,64,64))
    font_rect=font_surface.get_rect(center=(400,50))
    screen.blit(font_surface,font_rect)
    return score
def Multiple_obstacle(snail_rect_list):
     global Birds,bird_index,fly_image,Snails,snail_index,snail_image
     if snail_rect_list:
         for snailrect in snail_rect_list:
             snailrect.left-=4
             if snailrect.bottom==300:
              snail_index+=0.1
              snail_image=Snails[int(snail_index)%2]
              screen.blit(snail_image,snailrect)
             else:
              bird_index+=0.1
              fly_image=Birds[int(bird_index)%2]
              screen.blit(fly_image,snailrect)  
         snail_rect_list=[snailrect for snailrect in snail_rect_list if snailrect.left>-100]
         return snail_rect_list
     else:
         return []
def collision(snail_rect_list,player_rect):
    result=True
    if snail_rect_list:
        for snailrect in snail_rect_list:
            if player_rect.colliderect(snailrect):
                return False
    return result
def playerAnimation():
    global player_index,player_image,players
    if player_rect.bottom<300:
        screen.blit(player_jump,player_rect)
    else:
        player_index+=0.1
        player_image=players[int(player_index)%2]
        screen.blit(player_image,player_rect)
     
SCREEN_WIDTH=800
SCREEN_HIGHT=400
pygame.display.set_caption("First pygame")
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
clock=pygame.time.Clock()
#background
sky_image=pygame.image.load('graphics/Sky.png').convert()
ground_image=pygame.image.load('graphics/ground.png').convert()

#fonts
font=pygame.font.Font('font/Pixeltype.ttf',50)
gameover_font=font.render('Game Over',False,(64,64,64))
gameover_font_rect=gameover_font.get_rect(center=(400,50))

#obstacles
Snails=[]
snail_image1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_image2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_index=0
Snails.append(snail_image1)
Snails.append(snail_image2)
snail_image=Snails[snail_index]


#snail_rect=snail_image.get_rect(midbottom=(600,300))
snail_rect_list=[]
#bird animation
Birds=[]
fly1=pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly2=pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
Birds.append(fly1)
Birds.append(fly2)
bird_index=0
fly_image=Birds[bird_index]
#fly_rect=fly_image.get_rect()

#player animation
players=[]
player_walk1=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk2=pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_jump=pygame.image.load('graphics/Player/jump.png').convert_alpha()
players.append(player_walk1)
players.append(player_walk2)
player_index=0
player_image=players[player_index]

player_stand=pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_scaled=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand_scaled.get_rect(center=(400,200))
player_rect=player_image.get_rect(midbottom=(80,300))

#player falling and jumping
player_gravity=0
Game_Active=True

#Score time
start_time=0
Score_gameOver=0

#Timer

obstacle_timer=pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,1500)

while True:
    #nothing is here
    for event in pygame.event.get():
        
         if event.type==pygame.QUIT:
             pygame.quit()
             exit()
         if Game_Active:
            if event.type==pygame.KEYDOWN:
                print("KEY DOWN")
                player_gravity=-5
                if event.key==pygame.K_SPACE:
                    print('jump')
            if event.type==pygame.KEYUP:
                print("KEY UP")
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity=-5
            if event.type==obstacle_timer:
                if randint(0,2):
                    snail_rect_list.append(snail_image.get_rect(midbottom=(randint(900,1100),300)))
                else:
                    snail_rect_list.append(fly_image.get_rect(midbottom=(randint(900,1100),200)))
         if Game_Active==False:
            #print('dont know')
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    Game_Active=True
                    snail_rect_list=[]
                    start_time=int(pygame.time.get_ticks()/1000)
                    print('game activated')
                 
                    
    if Game_Active:   
        #screen.blit(test_surface,(200,100))
        screen.blit(sky_image,(0,0))
        screen.blit(ground_image,(0,300))
        #screen.blit(snail_image,snail_rect)
        #snail_rect.x-=3
        #if snail_rect.left<=-100:
            #snail_rect.left=800
        
        #snail movement
        snail_rect_list=Multiple_obstacle(snail_rect_list)
        
        Score_gameOver=Score()
        #player
        #screen.blit(player_image,player_rect)
        playerAnimation()
        #player_rect.left+=2
        if player_rect.left>=810:
            player_rect.left=-50
        if player_rect.bottom<=300:
            player_gravity+=0.1
            player_rect.bottom+=player_gravity
        if player_rect.bottom>=300:
            player_rect.bottom=300
            player_gravity=0

        #collision between player and the snail
        Game_Active=collision(snail_rect_list, player_rect)
        #if player_rect.colliderect(snail_rect):
            #collision=1
            #Game_Active=False
        #if collision:
        #  player_gravity-=0.1
        #  snail_rect.x+=3
        
        #keyboard input
        keys=pygame.key.get_pressed()
        #print(keys)
        if keys[pygame.K_u]:
            print("Jump")
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand_scaled,player_stand_rect)
        screen.blit(gameover_font,gameover_font_rect)
        gameover_score=font.render(f'Score:{Score_gameOver}',False,(64,64,64))
        gameover_score_rect=gameover_score.get_rect(center=(400,340))
        screen.blit(gameover_score,gameover_score_rect)
        
    pygame.display.update()
    clock.tick(60)
