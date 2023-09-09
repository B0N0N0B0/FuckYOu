import pygame
import sys
import random

pygame.init()

# 화면 크기 설정
screen_width = 1920  # 가로 크기
screen_height = 1080  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("마우스 좌표 출력")

# FPS
clock = pygame.time.Clock()

# 이벤트 루프
running = True  # 게임이 진행 중인가를 확인하는 변수


img = pygame.image.load("./Pictures/Team_1/bomb.png")
width = img.get_rect()[2]
height = img.get_rect()[3]

#Wall_1 = pygame.image.load("./Pictures/walls/wall.PNG")

#Wall_1_size = Wall_1.get_rect().size
#Wall_1_width = Wall_1_size[0]
#Wall_1_height = Wall_1_size[1]
#Wall_1_Xpos = screen_width / 4  # Gamescreenwidth의 4분의 1 
#Wall_1_Ypos = screen_height / 5  # Gamescreenwidth의 5분의 1 
img_1 = pygame.image.load("./Pictures/Team_1/shield.png")

doxx,dox,doyy,doy= 0,0,0,0
xpos,ypos = 0,0
_xpos,_ypos = 0,0
movx = 0
movy = 0

while running:
    clock.tick(60)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE:
                running = False
                sys.exit()
            if event.key == pygame.K_d:
                xpos = 35
                movx = 1
            elif event.key == pygame.K_a:
                xpos = -35
                movx = 1
            elif event.key == pygame.K_w:
                ypos = -50
                movy = 1
            elif event.key == pygame.K_s:
                ypos = 50
                movy = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                doxx=1
            elif event.key == pygame.K_a:
                dox=1
            elif event.key == pygame.K_w:
                doyy = 1
            elif event.key == pygame.K_s:
                doy = 1
    if _xpos < 0 or _xpos > 1920-width:
        xpos *= -1
        if _xpos < 0:
            _xpos = 5
        else:
            _xpos = 1920-width - 5
    if _ypos < 0 or _ypos > 1080-height:
        ypos *= -1
        if _ypos < 0:
            _ypos = 5
        else:
            _ypos = 1080 - height -5
    if dox == 1:
        xpos *= 0.95
    if doy == 1:
        ypos *= 0.95
    if doxx == 1:
        xpos *= 0.95
    if doyy == 1:
        ypos *= 0.95
    if abs(xpos) <= 1 :
        xpos = 0
        if dox == 1:
            dox = 0
        elif doxx == 1:
            doxx = 0
    if abs(ypos) <= 1:
        ypos = 0
        if doy == 1:
            doy = 0
        elif doyy == 1:
            doyy = 0
    
    screen.fill((255,255,255))

    #screen.blit(Wall_1, (Wall_1_Xpos, Wall_1_Ypos))

    screen.blit(img,(_xpos,_ypos))
    screen.blit(img_1, (900, 500))
    _xpos += xpos
    _ypos += ypos
    # if movx == 1:
    #     xpos *= 0.95
    # if movy == 1:
    #     ypos *= 0.95

    pygame.display.update()  # 게임 화면을 다시 그리기

# pygame 종료
pygame.quit()
sys.exit()

# Test