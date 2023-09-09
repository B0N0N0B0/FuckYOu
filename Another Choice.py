import pygame

pygame.init()

ano_choicescreen_width = 900  # 가로 크기
ano_choicecreen_height = 250  # 세로 크기
ano_choicescreen = pygame.display.set_mode((ano_choicescreen_width, ano_choicecreen_height))

# FPS
clock = pygame.time.Clock()

# 폰트 설정
#font = pygame.font.Font(None, 36)

ano_character_choose = pygame.image.load("./Pictures/another character choose.png")

# 화면 타이틀 설정
pygame.display.set_caption("Choice")

# 이벤트 루프
running = True  # 게임이 진행 중인가를 확인하는 변수

while running:
    dt = clock.tick(50)  # 게임 화면의 초당 프레임 수를 설정

    #print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        
        if event.type == pygame.KEYDOWN:
            
                # 현재 마우스 커서의 위치를 가져온다
                #x, y = pygame.mouse.get_pos()

                #print(f"마우스 좌표: ({x}, {y})")

                if event.key == pygame.K_u:  # u키를 누르면
                    running = False
                if event.key == pygame.K_i:  # i키를 누르면
                    running = False
                if event.key == pygame.K_o:  # o키를 누르면
                    running = False
                if event.key == pygame.K_p:  # p키를 누르면
                    running = False
                if event.key == pygame.K_j:  # j키를 누르면
                    running = False
                if event.key == pygame.K_k:  # k키를 누르면
                    running = False
                if event.key == pygame.K_l:  # l키를 누르면
                    running = False
           
    ano_choicescreen.blit(ano_character_choose, (0, 0))

    pygame.display.flip()

    pygame.display.update()