import pygame
import pyautogui
import subprocess
import sys

pygame.init()

# 화면 크기 설정
screen_width = 1920  # 가로 크기
screen_height = 1080  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("마우스 좌표 출력")

# FPS
clock = pygame.time.Clock()
'''
# 게임 상태
class GameState:
    MAIN_MWNU = 0
    GAME_SCENE = 1

current_state = GameState.MAIN_MWNU  # 초기 상태를 메인 메뉴로 설정
'''

# 소리 파일
sound = "C:/Users/shk/Downloads/MP_Funk Groove.mp3"
pygame.mixer_music.load(sound)


# 화면 타이틀 설정
pygame.display.set_caption("SJ game")

# 배경 이미지 불러오기
background = pygame.image.load("./Pictures/etc/Gamestartscene.png")

# 이벤트 루프
running = True  # 게임이 진행 중인가를 확인하는 변수

while running:
    dt = clock.tick(100)  # 게임 화면의 초당 프레임 수를 설정

    screenWidth = pyautogui.size()
    screenHeight = pyautogui.size()

    #print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 마우스 왼쪽 버튼 클릭 시
                # 현재 마우스 커서의 위치를 가져온다
                x, y = pygame.mouse.get_pos()

                print(f"마우스 좌표: ({x}, {y})")

                # 특정 x좌표 범위와 y좌표 범위 안에 클릭한 마우스 커서의 위치 출력
                if 98 <= event.pos[0] <= 523 and 827 <= event.pos[1] <= 914:  # 나가기 버튼 활성화
                    running = False
                if 98 <= event.pos[0] <= 523 and 696 <= event.pos[1] <= 783: # 게임 시작 버튼 활성화
                    # 메인 메뉴에서 게임 화면으로 전환
                    #if current_state == GameState.MAIN_MWNU:
                     #   current_state = GameState.GAME_SCENE
                     
                    # 다른 py 파일 실행하기
                    subprocess.Popen(["python", "./.vscode/.vscode/GameScene.py"])

                    running = False
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # esc를 눌렀을 때 게임을 종료시키기
                running = False

    
    '''
    if current_state == GameState.MAIN_MWNU:
        screen.blit(background, (0, 0))  # 배경 그리기
    elif current_state == GameState.GAME_SCENE:
        screen.blit(GameScene, (0, 0))
    '''
    screen.blit(background, (0, 0))  # 배경 그리기

    #pygame.mixer_music.play()

    #pygame.time.delay(3000)

    
    pygame.display.flip()
    pygame.display.update()  # 게임 화면을 다시 그리기

#SOUND_thread = threading.Thread(target=SOUND)

#SOUND_thread.start()

#SOUND_thread.join()

# pygame 종료
pygame.quit()
sys.exit()
