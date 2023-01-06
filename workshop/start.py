import pygame;
from sys import exit
from random import randint
pygame.init()


inix=0
iniy=0
endx=0
endy=0
vector=False
not_jump=False
cursor = True

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
_Mouse_drag = False

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
            # if _Mouse_drag == True :
            #     player_rect.x, player_rect.y = pygame.mouse.get_pos()

            # if event.type==pygame.MOUSEBUTTONUP:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity=-5
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity=5
            # if event.type==pygame.MOUSEBUTTONDOWN:
            #     #player_rect.x, player_rect.y = event.pos
            #     _Mouse_drag = True
            #     #player_rect.x, player_rect.y = pygame.mouse.get_pos()
            # if event.type == pygame.MOUSEBUTTONUP:
            #     _Mouse_drag = False ;

            if event.type ==  pygame.MOUSEBUTTONDOWN and vector==False:
                # vector=True
                print(vector)
                inix,iniy=pygame.mouse.get_pos()
                print(inix,iniy)


            if event.type == pygame.MOUSEBUTTONUP and vector == False:
                print(vector)
                endx,endy=event.pos
                if endy>=250:
                    endy=250
                print(endx,endy)
                if inix>=player_rect.left and inix<=player_rect.right and iniy<=player_rect.bottom and iniy>=player_rect.top:
                  vector = True


            if event.type==obstacle_timer:
                if randint(0,2):
                    snail_rect_list.append(snail_image.get_rect(midbottom=(randint(900,1100),300)))
                else:
                    snail_rect_list.append(fly_image.get_rect(midbottom=(randint(900,1100),200)))

         if Game_Active==False:
            #print('dont know')
            if event.type==pygame.KEYDOWN:
                Game_Active=True
                snail_rect_list=[]
                start_time=int(pygame.time.get_ticks()/1000)
                print('game activated')
                 
                    
    if Game_Active:   
        #screen.blit(test_surface,(200,100))
        screen.blit(sky_image,(0,0))
        screen.blit(ground_image,(0,300))
        
        #snail movement
        snail_rect_list=Multiple_obstacle(snail_rect_list)
        
        Score_gameOver=Score()
        #player
        playerAnimation()
        #player_rect.left+=2
        if player_rect.left==780:
            player_rect.left=780
        if player_rect.left==10:
            player_rect.left=20
        if player_rect.bottom<=80:
            player_rect.bottom=80
            if vector == False:
                player_gravity=player_gravity+1
        if player_rect.bottom<=300:
            if vector ==False :
                player_gravity+=0.1
                player_rect.bottom+=player_gravity
        if player_rect.bottom>=300:
            player_rect.bottom=300
            player_gravity=0
        if player_rect.x > endx - 10 and player_rect.x < endx + 10 and player_rect.y > endy - 50 and player_rect.y < endy + 50 and vector == True:
            vector = False
            player_gravity += 1
        if vector:
            player_gravity = 0
            if (player_rect.x < endx):
                player_rect.x = player_rect.x + 3
                pygame.time.delay(7)
            elif (player_rect.x > endx):
                player_rect.x = player_rect.x - 3
                pygame.time.delay(7)
            #if (player_rect.bottom < endy and player_rect.top>endy):

            if (player_rect.y > endy):
                print(player_rect.bottom,player_rect.top,endy)
                player_rect.y = player_rect.y - 1.5
                pygame.time.delay(7)
            elif (player_rect.y < endy):
                player_rect.y = player_rect.y + 1.5
                pygame.time.delay(7)

        #collision between player and the snail
        Game_Active=collision(snail_rect_list, player_rect)
        
        #keyboard input
        keys=pygame.key.get_pressed()
        #print(keys)
        # if(player_gravity==0):
        #     not_jump=False
        # if keys[pygame.K_UP] and not_jump==False:
        #     player_gravity = -5
        #     not_jump=True
        # if keys[pygame.K_DOWN] :
        #     player_gravity = 5
        # if keys[pygame.K_RIGHT] :
        #     player_rect.x+=2
        # if keys[pygame.K_LEFT] :
        #     player_rect.x-=2
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand_scaled,player_stand_rect)
        screen.blit(gameover_font,gameover_font_rect)
        gameover_score=font.render(f'Score:{Score_gameOver}',False,(64,64,64))
        gameover_score_rect=gameover_score.get_rect(center=(400,340))
        screen.blit(gameover_score,gameover_score_rect)
        
    pygame.display.update()
    clock.tick(60)
