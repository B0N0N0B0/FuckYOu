import pygame
import sys

def Team(Team : int()):
    if Team == 1:
        pygame.init()   
        choicescreen_width = 900  # 가로 크기
        choicecreen_height = 250  # 세로 크기
        choicescreen = pygame.display.set_mode((choicescreen_width, choicecreen_height))

        _type = int()

        # FPS
        clock = pygame.time.Clock()

        # 폰트 설정
        #font = pygame.font.Font(None, 36)

        character_choose = pygame.image.load("./Pictures/etc/character choose.png")

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

                        if event.key == pygame.K_q:  # q키를 누르면 병사 1
                            _type = 6
                            running = False
                        if event.key == pygame.K_w:  # w키를 누르면 폭탄병 2
                            _type = 0
                            running = False
                        if event.key == pygame.K_e:  # e키를 누르면 방어병 3
                            _type = 5
                            running = False
                        if event.key == pygame.K_r:  # r키를 누르면 돌격병 4
                            _type = 4
                            running = False
                        if event.key == pygame.K_a:  # a키를 누르면 의무관 5
                            _type = 1
                            running = False
                        if event.key == pygame.K_s:  # s키를 누르면 기술자 6
                            _type = 2
                            running = False
                        if event.key == pygame.K_d:  # d키를 누르면 왕 7
                            _type = 3
                            running = False
                
            choicescreen.blit(character_choose, (0, 0))

            pygame.display.flip()

            pygame.display.update()
        pygame.quit()
    

    if Team==2:
        pygame.init()

        ano_choicescreen_width = 900  # 가로 크기
        ano_choicecreen_height = 250  # 세로 크기
        ano_choicescreen = pygame.display.set_mode((ano_choicescreen_width, ano_choicecreen_height))

        # FPS
        clock = pygame.time.Clock()

        # 폰트 설정
        #font = pygame.font.Font(None, 36)

        ano_character_choose = pygame.image.load("./Pictures/etc/another character choose.png")

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
                            _type = 6
                            running = False
                        if event.key == pygame.K_i:  # i키를 누르면
                            _type = 0
                            running = False
                        if event.key == pygame.K_o:  # o키를 누르면
                            _type = 5
                            running = False
                        if event.key == pygame.K_p:  # p키를 누르면
                            _type = 4
                            running = False
                        if event.key == pygame.K_j:  # j키를 누르면
                            _type = 1
                            running = False
                        if event.key == pygame.K_k:  # k키를 누르면
                            _type = 2
                            running = False
                        if event.key == pygame.K_l:  # l키를 누르면
                            _type = 3
                            running = False
                
            ano_choicescreen.blit(ano_character_choose, (0, 0))

            pygame.display.flip()

            pygame.display.update()
        pygame.quit()

    return _type

# test
