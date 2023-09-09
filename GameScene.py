###################################################
#                   Import Area                   #
###################################################

import pygame,math,random,sys,os

#########################################################
#                   Initializing Area                   #
#########################################################


pygame.init()

Gamescreenwidth = 1920  # 가로 크기
Gamescreenheight = 1080  # 세로 크기
Gamescreen = pygame.display.set_mode((Gamescreenwidth, Gamescreenheight))

# FPS
clock = pygame.time.Clock()

# 화면 타이틀 설정
pygame.display.set_caption("An Exact Angle")

# 배경 이미지 불러오기
Gamescene = pygame.image.load("./Pictures/etc/gameboard.png")

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()  # 현재 tick을 받아옴


######################################################
#                   ImageLoad Area                   #
######################################################


# ImageLoad , MadeBy B0N0N0B0
image = dict()  # image라는 변수를 딕셔너리로 정의

image_list_Team_1 = os.listdir("./Pictures/Team_1")  # image_list_Team_1라는 변수를 Team_1 폴더 속 파일 목록에서 리스트를 만듦
image_list_Team_2 = os.listdir("./Pictures/Team_2")
warning_list = os.listdir("./Pictures/warning")  # image_list_Team_2라는 변수를 Team_2 폴더 속 파일 목록에서 리스트를 만듦
image_list = image_list_Team_1 + image_list_Team_2

class ImageLoad:
    def __init__(self,path,Xpos,Ypos,cond): # cond ) 0 : wall , 1 : Team 1, 2 : Team 2  /  path는 파일 이름
        if cond == 0:
            self.image = pygame.image.load("./Pictures/walls/" + path)  # 이미지 로드 경로를 Pictures/walls 안에 있는 path 이미지로 로드
            self.type = "wall"
        elif cond == 1:
            self.image = pygame.image.load("./Pictures/Team_1/" + path)  # 이미지 로드 경로를 Pictures/Team_1 안에 있는 path 이미지로 로드
            self.angle = math.radians(45)
            self.type = "unit.Team_1"
        elif cond == 2:
            self.image = pygame.image.load("./Pictures/Team_2/" + path)  # 이미지 로드 경로를 Pictures/Team_2 안에 있는 path 이미지로 로드
            self.angle = math.radians(45)
            self.type = "unit.Team_2"
        elif cond == 3:
            self.image = pygame.image.load("./Pictures/etc/" + path)  # 이미지 로드 경로를 Pictures/etc 안에 있는 path 이미지로 로드
            self.type = "etc"
            self.display = False
        elif cond == 4:
            self.image = pygame.image.load("./Pictures/warning/" + path)  # 이미지 로드 경로를 Pictures/Team_2 안에 있는 path 이미지로 로드
            self.type = "warning"
            self.display = False
            self.blit_start = 0
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.pos = [Xpos,Ypos]
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.delta = [0,0]
        self.IsCreated = False
        if cond == 0: 
            self.hitbox = [self.Xpos,self.Ypos,self.width,self.height]
            self.hitbox_R = [self.Xpos,self.Ypos,self.Xpos+self.width,self.Ypos+self.height]
        elif cond == 1:
            self.hitbox = [self.Xpos+15,self.Ypos+15,self.width-30,self.height-30]
            self.hitbox_R = [self.Xpos+15,self.Ypos+15,self.Xpos+self.width-30,self.Ypos+self.height-30]
        elif cond == 2: 
            self.hitbox = [self.Xpos+15,self.Ypos+15,self.width-30,self.height-30]
            self.hitbox_R = [self.Xpos+15,self.Ypos+15,self.Xpos+self.width-30,self.Ypos+self.height-30]
        # elif cond == 3 : self.hitbox = [self.Xpos+15,self.Ypos+15,self.width-30,self.height-30]

image["Wall_1"] = ImageLoad("wall.PNG",
                            Gamescreenwidth/4,
                            Gamescreenheight/5,
                            0)


image["Wall_2"] = ImageLoad("wall2.PNG",
                            Gamescreenwidth-400,
                            Gamescreenheight-300,
                            0)


image["Wall_3"] = ImageLoad("wall3.PNG",
                            Gamescreenwidth-400,
                            Gamescreenheight-475,
                            0)


image["Choice_1"] = ImageLoad("character choose.png",
                            (Gamescreenwidth-900)/2,
                            (Gamescreenheight-250)/2+400,
                            3)

image["Choice_2"] = ImageLoad("another character choose.png",
                            (Gamescreenwidth-900)/2,
                            (Gamescreenheight-250)/2-400,
                            3)


image["Option"] = ImageLoad("gameoption.png",
                            Gamescreenwidth-(Gamescreenwidth/15),
                            (Gamescreenheight/15)/3,
                            3)

#image["test"] = ImageLoad("보노보노2.png",
                            #0,
                            #0,
                            #3)

image["OptionScene"] = ImageLoad("optionScene.png",
                                (Gamescreenwidth/2)-325,
                                (Gamescreenheight/2)-187,
                                3)

#image["test"] = ImageLoad("보노보노.png",
                            #0,
                            #0,
                            #3)

for img in image_list_Team_1:
    image[img] = ImageLoad(img,
                           100,
                           890,
                           1)

for img in image_list_Team_2:
    image[img] = ImageLoad(img,
                           10,
                           800,
                           2)
for img in warning_list:
    image[img] = ImageLoad(img,
                           550,
                           50,
                           4)

choice_pos_1 = [
    [526 , 887,623 , 1033], #
    [ 639 , 887, 749 , 1033], #
    [759 , 870 , 902 , 1056], #
    [904 , 869,1016 , 1033], #
    [1033 , 871,1155 , 1041 ], #
    [1169 , 874,1280 , 1038], #
    [1290 , 877 ,1400 , 1040 ]  #
]
choice_pos_2 = [
    [519 , 85 ,630 , 231], #
    [640 , 82,748 , 237], #
    [754 , 70,902 , 253], #
    [907 , 88,1016 , 238], #
    [1035 , 88,1151 , 235], #
    [1164 , 89,1279 , 234], #
    [1287 , 88,1401 , 234]  #
]

#####################################################
#                   Variable Area                   #
#####################################################


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

isWarning = []

# 파랑팀
character_1 = [image[img] for img in image_list_Team_1]
velocity_1 = [0, 0]
drag_force_1 = 20  # 움직일 때 받는 힘
drag_friction_1 = 0.05  # 움직일 때 받는 마찰

# 빨강팀
character_2 = [image[img] for img in image_list_Team_2]
velocity_2 = [0, 0]
drag_force_2 = 20  # 움직일 때 받는 힘
drag_friction_2 = 0.05  # 움직일 때 받는 마찰

is_click = bool()
mouse_click_pos = list()
pos_buffer = list()

charBlit_list = set(["Wall_1","Wall_2","Wall_3"])
Fix_list = ["Wall_1","Wall_2","Wall_3"]

ep = None
ip = None

_type = None

char_pos_1 = list()
char_pos_2 = list()

delta_pos = list()
org_pos = []

dragging = None

# # 충돌한 물체의 속도와 충돌 각도
cs = 17.5
ca = random.uniform(0, 2 * math.pi)  # 충돌 각도를 라디안으로 변경

new_velocity_x = cs * math.cos(ca)
new_velocity_y = ca * math.sin(ca)

# 이벤트 처리
running = False  # 게임이 진행 중인가를 확인하는 변수

mpos = []

#####################################################
#                   Function Area                   #
#####################################################



def show_hitbox(img):  # 각 캐릭터의 충돌 히트박스 구현
    ig = image[img]
    ig.hitbox = [ig.Xpos+15,ig.Ypos+15,ig.width-30,ig.height-30]
    ig.hitbox_rect = pygame.Rect(ig.Xpos+15,ig.Ypos+15,ig.width-30,ig.height-30)
    pygame.draw.rect(Gamescreen,BLACK,ig.hitbox,5)

def range_test(range,_pos):
    if _pos[0]>=range[0] and _pos[1]>=range[1] and _pos[0]<=range[2] and _pos[1]<=range[3]:
        return True
    else : False

def in_range(rg1,rg2): # [0,0,5,5] , [1,1,2,2] # return X true : 1 Y true : 2 Fasle 0
    if (rg1[0]<=rg2[0] and rg1[2]>=rg2[2]):
        return 1 # X True
    elif (rg1[1]<=rg2[1] and rg1[3]>=rg2[3]):
        return 2 # X True
    else : return 0 # False


def show_hitbox(img):
    ig = image[img]
    ig.hitbox = [ig.Xpos+15,ig.Ypos+15,ig.width-30,ig.height-30]
    pygame.draw.rect(Gamescreen,RED,ig.hitbox,5)

def show_hitbox(img):pygame.draw.rect(Gamescreen,RED,image[img].hitbox,5)

def update_hitbox(img):
    global image
    if image[img].type == "unit.Team_1" or image[img].type == "unit.Team_2":
        image[img].hitbox = [image[img].Xpos+15,image[img].Ypos+15,image[img].width-30,image[img].height-30]
        image[img].hitbox_R = [image[img].Xpos+15,image[img].Ypos+15,image[img].Xpos+image[img].width-30,image[img].Ypos+image[img].height-30]
    else: # image[img].type == "wall":
        image[img].hitbox = [image[img].Xpos,image[img].Ypos,image[img].width,image[img].height]
        image[img].hitbox_R = [image[img].Xpos,image[img].Ypos,image[img].Xpos+image[img].width,image[img].Ypos+image[img].height]


def hitbox_test(img,_pos):
    global pos_buffer
    hbch = image[img]
    hitbox = hbch.hitbox
    if _pos[0]>=hitbox[0] and _pos[1] >= hitbox[1] and \
    _pos[0]<=hitbox[0]+hitbox[2] and _pos[1]<=hitbox[1]+hitbox[3]:  
    # _pos의 x값이 히트박스의 x값보다 크고 _pos의 y값이 히트박스의 y값보다 크고
    # _pos의 x값이 해당 히트박스의 이미지의 가로에서 30을 뺀 값보다 작고
    # _pos의 y값이 해당 히트박스의 이미지의 세로에서 30을 뺀 값보다 작을 때

        pos_buffer = [_pos[0]-hbch.Xpos,_pos[1]-hbch.Ypos]
        return True
    else: return False

def Choice_DISPLAY():
    global image
    chc = ["Choice_1","Choice_2"]
    for choice in chc:
        if image[choice].display:
            blit(choice)
            img = image[choice]
            pygame.draw.rect(Gamescreen,BLACK,[img.Xpos-5,img.Ypos-5,\
                                            img.width+5,img.height+5],5)
            
def Choice_click(chc):
    global charBlit_list,_type
    # if chc == 1:
    if image["Choice_1"].display:
        if is_click:
            if range_test(choice_pos_1[0],mouse_click_pos):
                _type = 6
                image["Choice_1"].display = False
            elif range_test(choice_pos_1[1],mouse_click_pos):
                _type = 0
                image["Choice_1"].display = False
            elif range_test(choice_pos_1[2],mouse_click_pos):
                _type = 5
                image["Choice_1"].display = False
            elif range_test(choice_pos_1[3],mouse_click_pos):
                _type = 4
                image["Choice_1"].display = False
            elif range_test(choice_pos_1[4],mouse_click_pos):
                _type = 1
                image["Choice_1"].display = False
            elif range_test(choice_pos_1[5],mouse_click_pos):
                _type = 2
                image["Choice_1"].display = False
            elif range_test(choice_pos_1[6],mouse_click_pos):
                _type = 3
                image["Choice_1"].display = False
        elif event.key == pygame.K_q:  # q키를 누르면 병사 1
            _type = 6
            image["Choice_1"].display = False
        elif event.key == pygame.K_w:  # w키를 누르면 폭탄병 2
            _type = 0
            image["Choice_1"].display = False
        elif event.key == pygame.K_e:  # e키를 누르면 방어병 3
            _type = 5
            image["Choice_1"].display = False
        elif event.key == pygame.K_r:  # r키를 누르면 돌격병 4
            _type = 4
            image["Choice_1"].display = False
        elif event.key == pygame.K_a:  # a키를 누르면 의무관 5
            _type = 1
            image["Choice_1"].display = False
        elif event.key == pygame.K_s:  # s키를 누르면 기술자 6
            _type = 2
            image["Choice_1"].display = False
        elif event.key == pygame.K_d:  # d키를 누르면 왕 7
            _type = 3
            image["Choice_1"].display = False
            
        try:
            charBlit_list.add(image_list[_type])
        except : pass


    # elif chc == 2:
    if image["Choice_2"].display:
        if is_click:
            if range_test(choice_pos_2[0],mouse_click_pos):
                _type = 6 + 7
                image["Choice_2"].display = False
            elif range_test(choice_pos_2[1],mouse_click_pos):
                _type = 0 + 7
                image["Choice_2"].display = False
            elif range_test(choice_pos_2[2],mouse_click_pos):
                _type = 5 + 7
                image["Choice_2"].display = False
            elif range_test(choice_pos_2[3],mouse_click_pos):
                _type = 4 + 7
                image["Choice_2"].display = False
            elif range_test(choice_pos_2[4],mouse_click_pos):
                _type = 1 + 7
                image["Choice_2"].display = False
            elif range_test(choice_pos_2[5],mouse_click_pos):
                _type = 2 + 7
                image["Choice_2"].display = False
            elif range_test(choice_pos_2[6],mouse_click_pos):
                _type = 3 + 7
                image["Choice_2"].display = False
        elif event.key == pygame.K_u:  # u키를 누르면
            _type = 6 + 7
            image["Choice_2"].display = False
        elif event.key == pygame.K_i:  # i키를 누르면
            _type = 0 + 7
            image["Choice_2"].display = False
        elif event.key == pygame.K_o:  # o키를 누르면
            _type = 5 + 7
            image["Choice_2"].display = False
        elif event.key == pygame.K_p:  # p키를 누르면
            _type = 4 + 7
            image["Choice_2"].display = False
        elif event.key == pygame.K_j:  # j키를 누르면
            _type = 1 + 7
            image["Choice_2"].display = False
        elif event.key == pygame.K_k:  # k키를 누르면
            _type = 2 + 7
            image["Choice_2"].display = False
        elif event.key == pygame.K_l:  # l키를 누르면
            _type = 3 + 7
            image["Choice_2"].display = False
        try:charBlit_list.add(image_list[_type])
        except : pass

def img_vel():
    global image
    image[image_list[_type]].Xpos += velocity_1[0]
    image[image_list[_type]].Ypos += velocity_1[1]

def dragfunction(img : None ,type : int(),event : None):
    global isdrag_1,isdrag_2,drag_SP_1,drag_SP_2,ep,ip
    if image[img].Xpos <= event.pos[0] <= image[img].Xpos + image[img].width \
        and image[img].Ypos <= event.pos[1] <= image[img].Ypos + image[img].height:
        # click_chr = img

        if type==1 : isdrag_1 = True ; drag_SP_1 = event.pos
        else : isdrag_2 = True ; drag_SP_2 = event.pos
        
        ep = event.pos
        ip = [image[img].Xpos,image[img].Ypos]
'''
def Collision(img):
    ig = image[img]
    ig.hitbox_rect = pygame.Rect(ig.Xpos+15,ig.Ypos+15,ig.width-30,ig.height-30)
    if ig.hitbox_rect.colliderect(image["Wall_1"].rect) and \
        ig.hitbox_rect.colliderect(image["Wall_2"].rect) and \
        ig.hitbox_rect.colliderect(image["Wall_3".rect]):
        print("collision")
'''


def collision(_img,col_img):
    ig = image[_img].hitbox_R
    cg = image[col_img].hitbox_R
    # ig.hitbox = [ig.Xpos+15,ig.Ypos+15,ig.width-30,ig.height-30]
    # if ig.Xpos+15 >= Gamescreenwidth/4 or ig.Ypos+15 <= Gamescreenheight/5:
    if in_range(ig,cg) == 1:
        #print("X collision")
        image[col_img].delta[0] *= -1
    elif in_range(ig,cg) == 2 :
        #print("Y collision")
        image[col_img].delta[1] *= -1

# def collision(_img,col_img):
#     ig = image[_img].hitbox_R
#     cg = image[col_img].hitbox_R
#     # ig.hitbox = [ig.Xpos+15,ig.Ypos+15,ig.width-30,ig.height-30]
#     # if ig.Xpos+15 >= Gamescreenwidth/4 or ig.Ypos+15 <= Gamescreenheight/5:
#     if in_range(ig,cg) == 1:
#         print("X collision")
#         image[col_img].delta[0] *= -1
#     elif in_range(ig,cg) == 2 :
#         print("Y collision")
#         image[col_img].delta[1] *= -1
def collision(fix_img,col_img):
    rg1 = image[fix_img].hitbox_R
    rg2 = image[col_img].hitbox_R
    
    if not(not rg1[0]<=rg2[0]<=rg1[2] and not rg1[0]<=rg2[2]<=rg1[2]) and not(not rg1[1]<=rg2[1]<=rg1[3] and not rg1[1]<=rg2[3]<=rg1[3]):
        blit("test")

        
def teleport(img,pos):
    print(pos)
    image[img].Xpos = pos[0]
    image[img].Ypos = pos[1]


def blit(img : None) : Gamescreen.blit(image[img].image,(image[img].Xpos,image[img].Ypos))


######################################################
#                   MAIN GAME Area                   #
######################################################


#######################################################
#                   Debug Game Area                   #
#######################################################

debug = True

while debug:
    clock.tick(60)

    #########################################################
    #                   Pygame Event Area                   #
    #########################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            debug = False
        if event.type == pygame.KEYDOWN:
            if image["Choice_1"].display:
                if event.key == pygame.K_ESCAPE:
                    image["Choice_1"].display = False
                Choice_click(1)
            elif not image["Choice_2"].display:
                if event.key == pygame.K_1: # choice 1 임시 활성화 버튼
                    image["Choice_1"].display = True
            if image["Choice_2"].display:
                if event.key == pygame.K_ESCAPE:
                    image["Choice_2"].display = False
                Choice_click(2)
            elif not image["Choice_2"].display :
                if event.key == pygame.K_2: # choice 2 임시 활성화 버튼
                    image["Choice_2"].display = True
            
            if event.key == pygame.K_ESCAPE:
                debug = False
            elif event.key == pygame.K_1: # choice 1 임시 활성화 버튼
                    image["Choice_1"].display = True
            elif event.key == pygame.K_2: # choice 2 임시 활성화 버튼
                image["Choice_2"].display = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            is_click = True
            drag_start = pygame.time.get_ticks()

            if event.button == 1:  # 마우스 왼쪽 버튼을 눌렀을 때
                x, y = pygame.mouse.get_pos()

                #print(f"마우스 좌표: {x}, {y}")

                if 1793 <= event.pos[0] <= 1885 and 23 <= event.pos[1] <= 114:
                    blit("OptionScene")

            if image["Choice_1"].display : Choice_click(1)
            elif image["Choice_2"].display : Choice_click(2)

            for img in charBlit_list:
                update_hitbox(img=img)
                if hitbox_test(img,mouse_click_pos):
                    dragging = img
                    if org_pos == []:
                        org_pos = [image[img].Xpos,image[img].Ypos]
                    if mpos == []:
                        mpos = [event.pos[0]-image[img].Xpos,event.pos[1]-image[img].Ypos]
                    break

        if event.type == pygame.MOUSEBUTTONUP:  # 마우스 버튼을 뗐을 때
            mouse_click_pos = list()
            mpos = []
            dragging = None
            is_click = False
        if event.type == pygame.MOUSEMOTION:
            if dragging != None and not ( dragging in Fix_list):
                if (pygame.time.get_ticks()-drag_start) <= 100000:

                    image[dragging].delta = [(event.pos[0]-image[dragging].Xpos)/2,(event.pos[1]-image[dragging].Ypos)/2]
                    #print(image[dragging].delta)
                    image[dragging].Xpos += - pos_buffer[0]
                    image[dragging].Ypos += - pos_buffer[1]
                    # image[dragging].delta = [0,0]
            else : dragging = None

            image[dragging].delta = [(event.pos[0]-mpos[0]-image[dragging].Xpos),(event.pos[1]-mpos[1]-image[dragging].Ypos)]
        else : dragging = None ; org_pos = []


    ###########################################################
    #                   Pygame running Area                   #
    ###########################################################

    Gamescreen.fill((128,128,128))
    pygame.draw.rect(Gamescreen,WHITE,[1920/10,1080/10,1920/10*8,1080/10*8])
    pygame.draw.rect(Gamescreen,BLACK,[1920/10,1080/10,1920/10*8,1080/10*8],10)
    
    
    for img in charBlit_list:
        update_hitbox(img=img)
        if image[img].Xpos <0 or image[img].Xpos > 1920-image[img].width:
            if dragging != None:
                image["out_of_map.png"].blit_start = pygame.time.get_ticks()
                isWarning.append("out_of_map.png")
                dragging = None
                teleport(img=img,pos=org_pos)
                image[img].delta = [0,0]
            else:
                if image[img].Xpos <=2 : image[img].Xpos = 5
                else : image[img].Xpos = 1910-image[img].width
                image[img].delta[0] *= -1
        if image[img].Ypos <0 or image[img].Ypos > 1080-image[img].height:
            if dragging != None:
                image["out_of_map.png"].blit_start = pygame.time.get_ticks()
                isWarning.append("out_of_map.png")
                dragging = None
                teleport(img=img,pos=org_pos)
                image[img].delta = [0,0]
            else:
                if image[img].Ypos <=2 : image[img].Ypos = 5
                else : image[img].Ypos = 1070-image[img].height
                image[img].delta[1] *= -1
        if not (img in Fix_list) : 
            for fxi in charBlit_list: 
                if fxi != img:
                    collision(fxi,img)
                # print(img,fxi)
        image[img].Xpos += image[img].delta[0]
        image[img].Ypos += image[img].delta[1]



    # blit("Wall_1")
    # blit("Wall_2")
    # blit("Wall_3")
    blit("Option")
    

    Choice_DISPLAY()

    for img in charBlit_list:
        update_hitbox(img=img)
        blit(img=img)
        show_hitbox(img)


    if image["Choice_1"].display:
        for hb in choice_pos_1:
            pygame.draw.rect(Gamescreen,BLACK,[hb[0],hb[1],hb[2]-hb[0],hb[3]-hb[1]],5)
    if image["Choice_2"].display:
        for hb in choice_pos_2:
            pygame.draw.rect(Gamescreen,BLACK,[hb[0],hb[1],hb[2]-hb[0],hb[3]-hb[1]],5)
    
    if isWarning != []:
        # if 
        for warnImg in isWarning:
            if pygame.time.get_ticks() - image[warnImg].blit_start <= 2000:
                blit(warnImg)
            else : 
                image[warnImg].blit_start = 0
                isWarning.remove(warnImg)


    #print(charBlit_list)
    pygame.display.update()

    for img in charBlit_list:
        image[img].delta[0] *= 0.95
        image[img].delta[1] *= 0.95



######################################################
#                   Real Game Area                   #
######################################################


while running:
    clock.tick(80)  # 게임 화면의 초당 프레임 수를 설정
    
    #print("fps : " + str(clock.get_fps()))

#     isOpenpy = False  # Choice.py가 열려있는가?
#     isOpeningpy = False  # Another Choice.py가 열려있는가?


    #########################################################
    #                   Pygame Event Area                   #
    #########################################################


    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # esc를 눌렀을 때 게임을 종료시키기
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 마우스 왼쪽 버튼을 누를 때
                for img in image_list_Team_1 : dragfunction(img=img,type=1,event=event)
                for img in image_list_Team_2 : dragfunction(img=img,type=2,event=event)



        elif event.type == pygame.MOUSEBUTTONUP:
            delta_pos = [event.pos[0]-ep[0],event.pos[1]-ep[1]]
            isdrag_1 = False
            isdrag_2 = False
            ep = None
        elif event.type == pygame.MOUSEMOTION:
            if isdrag_1:
                image["bomb.png"].Xpos = -ep[0]+event.pos[0] + ip[0]
                image["bomb.png"].Ypos = -ep[1]+event.pos[1] + ip[1]
            if isdrag_2:
                pass
        
        
        elif event.type == pygame.MOUSEMOTION:  # 드래그 이벤트 처리
            if isdrag_1:
                isOpenpy_1 = True
                # 드래그한 방향과 거리를 계산하여 velocity 설정
                distance = max(1, pygame.math.Vector2(delta_pos[0], delta_pos[1]).length())
                velocity_1 = [drag_force_1 * delta_pos[0] / distance, drag_force_1 * delta_pos[1] / distance]
            
            
            if isdrag_2:
                isOpenpy_2 = True
                # 드래그한 방향과 거리를 계산하여 velocity 설정
                distance = max(1, pygame.math.Vector2(delta_pos[0], delta_pos[1]).length())
                velocity_2 = [drag_force_2 * delta_pos[0] / distance, drag_force_2 * delta_pos[1] / distance]

        Gamescreen.fill((0,0,0))
        blit(img="bomb.png")
        pygame.display.flip()    

    img_vel()

    velocity_1 = [int(velocity_1[0]*drag_friction_1),int(velocity_1[1]*drag_friction_1)]
    velocity_2 = [int(velocity_2[0]*drag_friction_2),int(velocity_2[1]*drag_friction_2)]


    char_pos_1 = [image[image_list_Team_1[_type]].Xpos,image[image_list_Team_1[_type]].Ypos]
    char_pos_2 = [image[image_list_Team_2[_type]].Xpos,image[image_list_Team_2[_type]].Ypos]
    
    # 해야될 것 : 가로벽, 세로벽 끝에 닿았을 때 튕겨나가게 하는 코드 작성하기. 
    # 이미지 크기 고려해서 튕겨나가는 코드 작성

    char_pos_1 = [image[image_list[_type]].Xpos,image[image_list[_type]].Ypos]
    char_pos_2 = [image[image_list[_type]].Xpos,image[image_list[_type]].Ypos]

    if char_pos_1[0] < 0 or char_pos_1[0] > 1920-image[image_list[_type]].width:
        velocity_1[0] *= -1
        if char_pos_1[0] <= 2:
            char_pos_1[0] = 5
        else:
            char_pos_1[0] = 1913-image[image_list_Team_1[_type]].width

    if char_pos_1[1] < 0 or char_pos_1[1] > 1080-image[image_list[_type]].height:
        velocity_1[1] *= -1
        if char_pos_1[1] <= 2:
            char_pos_1[1] = 5
        else:
            char_pos_1[1] = 1073-image[image_list[_type]].height

'''
                # 파랑팀
#                 if warrior_x_pos <= event.pos[0] <= warrior_x_pos + warrior_width \
#                     and warrior_y_pos <= event.pos[1] <= warrior_y_pos + warrior_height:
#                     isdrag = True
#                     drag_startpos = event.pos
#                 if bomb_x_pos <= event.pos[0] <= bomb_x_pos + bomb_width \
#                     and bomb_y_pos <= event.pos[1] <= bomb_y_pos + bomb_height:
#                     isdrag = True
#                     drag_startpos = event.pos
#                 if shield_x_pos <= event.pos[0] <= shield_x_pos + shield_width \
#                     and shield_y_pos <= event.pos[1] <= shield_y_pos + shield_height:
#                     isdrag = True
#                     drag_startpos = event.pos
#                 if rush_x_pos <= event.pos[0] <= rush_x_pos + rush_width \
#                     and rush_y_pos <= event.pos[1] <= rush_y_pos + rush_height:
#                     isdrag = True
#                     drag_startpos = event.pos
#                 if doctor_x_pos <= event.pos[0] <= doctor_x_pos + doctor_width \
#                     and doctor_y_pos <= event.pos[1] <= doctor_y_pos + doctor_height:
#                     isdrag = True
#                     drag_startpos = event.pos
#                 if engineer_x_pos <= event.pos[0] <= engineer_x_pos + engineer_width \
#                     and engineer_y_pos <= event.pos[1] <= engineer_y_pos + engineer_height:
#                     isdrag = True
#                     drag_startpos = event.pos
#                 if king_x_pos <= event.pos[0] <= king_x_pos + king_width \
#                     and king_y_pos <= event.pos[1] <= king_y_pos + king_height:
#                     isdrag = True
#                     drag_startpos = event.pos


#                 # 빨강팀
#                 if ano_warrior_xpos <= event.pos[0] <= ano_warrior_xpos + ano_warrior_width \
#                     and ano_warrior_ypos <= event.pos[1] <= ano_warrior_ypos + ano_warrior_height:
#                     isdragging = True
#                     dragging_startpos = event.pos
#                 if ano_bomb_xpos <= event.pos[0] <= ano_bomb_xpos + ano_bomb_width \
#                     and ano_bomb_ypos <= event.pos[1] <= ano_bomb_ypos + ano_bomb_height:
#                     isdragging = True
#                     dragging_startpos = event.pos
#                 if ano_shield_xpos <= event.pos[0] <= ano_shield_xpos + ano_shield_width \
#                     and ano_shield_ypos <= event.pos[1] <= ano_shield_ypos + ano_shield_height:
#                     isdragging = True
#                     dragging_startpos = event.pos
#                 if ano_rush_xpos <= event.pos[0] <= ano_rush_xpos + ano_rush_width \
#                     and ano_rush_ypos <= event.pos[1] <= ano_rush_ypos + ano_rush_height:
#                     isdragging = True
#                     dragging_startpos = event.pos
#                 if ano_doctor_xpos <= event.pos[0] <= ano_doctor_xpos + ano_doctor_width \
#                     and ano_doctor_ypos <= event.pos[1] <= ano_doctor_ypos + ano_doctor_height:
#                     isdragging = True
#                     dragging_startpos = event.pos
#                 if ano_engineer_xpos <= event.pos[0] <= ano_engineer_xpos + ano_engineer_width \
#                     and ano_engineer_ypos <= event.pos[1] <= ano_engineer_ypos + ano_engineer_height:
#                     isdragging = True
#                     dragging_startpos = event.pos
#                 if ano_king_xpos <= event.pos[0] <= ano_king_xpos + ano_king_width \
#                     and ano_king_ypos <= event.pos[1] <= ano_king_ypos + ano_king_height:
#                     isdragging = True
#                     dragging_startpos = event.pos
'''
                
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:  # 마우스 왼쪽 버튼을 떼었을 때
        #         isdrag_1,isdrag_2 = False

        #         if isdrag_1 == False and isOpeningpy and not isOpenpy:
        #             subprocess.Popen(["python", "./Pictures/Another Choice.py"])
        #             isOpeningpy = False
                    

        #         if isdrag_2 == False and not isOpeningpy and isOpenpy:
        #             subprocess.Popen(["python", ".Pictures/Choice.py"])
        #             isOpenpy = False

                #scripts_path = scripts[current_script_index]   
                #current_script_index = (current_script_index + 1) % len(scripts)
                #run_script(scripts_path)

    
               
    # 스프라이트 이동

'''
    # 파랑팀
#     warrior_x_pos += velocity[0]
#     warrior_y_pos += velocity[1]

#     bomb_x_pos += velocity[0]
#     bomb_y_pos += velocity[1]

#     shield_x_pos += velocity[0]
#     shield_y_pos += velocity[1]

#     rush_x_pos += velocity[0]
#     rush_y_pos += velocity[1]

#     doctor_x_pos += velocity[0]
#     doctor_y_pos += velocity[1]

#     engineer_x_pos += velocity[0]
#     engineer_y_pos += velocity[1]

#     king_x_pos += velocity[0]
#     king_y_pos += velocity[1]

#     # 빨강팀
#     ano_warrior_xpos += ano_velocity[0]
#     ano_warrior_ypos += ano_velocity[1]

#     ano_bomb_xpos += ano_velocity[0]
#     ano_bomb_ypos += ano_velocity[1]

#     ano_shield_xpos += ano_velocity[0]
#     ano_shield_ypos += ano_velocity[1]

#     ano_rush_xpos += ano_velocity[0]
#     ano_rush_ypos += ano_velocity[1]

#     ano_doctor_xpos += ano_velocity[0]
#     ano_doctor_ypos += ano_velocity[1]

#     ano_engineer_xpos += ano_velocity[0]
#     ano_engineer_ypos += ano_velocity[1]

#     ano_king_xpos += ano_velocity[0]
#     ano_king_ypos += ano_velocity[1]
    
#     # 서서히 멈추도록 velocity를 감소시킴

#     ano_velocity[0] *= (1 - dragging_friction)
#     ano_velocity[1] *= (1 - dragging_friction)
'''

    
#     # 캐릭터의 이동 방향 벡터 계산
#     #character_move = pygame.math.Vector2(character_x_pos + 100 / 2, character_y_pos + 100 / 2)
#     #another_chr_move = pygame.math.Vector2(another_chr_xpos + 100 / 2, another_chr_ypos + 100 / 2)


#     # 화면 끝에 닿으면 튕기기
#     # 가로벽에 닿았을 때

    

#     wall_1_rect = Wall_1.get_rect()
#     wall_1_rect.left = Wall_1_Xpos
#     wall_1_rect.top = Wall_1_Ypos

#     wall_2_rect = Wall_2.get_rect()
#     wall_2_rect.left = Wall_2_Xpos
#     wall_2_rect.top = Wall_2_Ypos

#     wall_3_rect = Wall_3.get_rect()
#     wall_3_rect.left = Wall_3_Xpos
#     wall_3_rect.top = Wall_3_Ypos
    
#     # 충돌 체크
#     # 파랑팀
#     warrior_rect = warrior.get_rect()
#     warrior_rect.left = warrior_x_pos
#     warrior_rect.top = warrior_y_pos

#     bomb_rect = bomb.get_rect()
#     bomb_rect.left = bomb_x_pos
#     bomb_rect.top = bomb_y_pos

#     shield_rect = shield.get_rect()
#     shield_rect.left = shield_x_pos
#     shield_rect.top = shield_y_pos

#     #rush_rect = rush.get_rect()
#     #rush_rect.left = rush_x_pos
#     #rush_rect.top = rush_y_pos

#     doctor_rect = doctor.get_rect()
#     doctor_rect.left = doctor_x_pos
#     doctor_rect.top = doctor_y_pos

#     engineer_rect = engineer.get_rect()
#     engineer_rect.left = engineer_x_pos
#     engineer_rect.top = engineer_y_pos

#     king_rect = king.get_rect()
#     king_rect.left = king_x_pos
#     king_rect.top = king_y_pos

#     # 빨강팀
#     ano_warrior_rect = ano_warrior.get_rect()
#     ano_warrior_rect.left = ano_warrior_xpos
#     ano_warrior_rect.top = ano_warrior_ypos

#     ano_bomb_rect = ano_bomb.get_rect()
#     ano_bomb_rect.left = ano_bomb_xpos
#     ano_bomb_rect.top = ano_bomb_ypos

#     ano_shield_rect = ano_shield.get_rect()
#     ano_shield_rect.left = ano_shield_xpos
#     ano_shield_rect.top = ano_shield_ypos

#     ano_rush_rect = ano_rush.get_rect()
#     ano_rush_rect.left = ano_rush_xpos
#     ano_rush_rect.top = ano_rush_ypos

#     ano_doctor_rect = ano_doctor.get_rect()
#     ano_doctor_rect.left = ano_doctor_xpos
#     ano_doctor_rect.top = ano_doctor_ypos

#     ano_engineer_rect = engineer.get_rect()
#     ano_engineer_rect.left = ano_engineer_xpos
#     ano_engineer_rect.top = ano_engineer_ypos

#     ano_king_rect = ano_king.get_rect()
#     ano_king_rect.left = ano_king_xpos
#     ano_king_rect.top = ano_king_ypos



#     # 충돌 체크
#     # 파랑팀
#     if warrior_rect.colliderect(wall_1_rect) or warrior_rect.colliderect(wall_2_rect) or warrior_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         warrior_angle = new_angle
#         velocity = [new_velocity_x, new_velocity_y]

    
#     # 충돌 체크
#     collided_obj = []

#     for obj in gameobjects:
#         if bomb_rect.colliderect(obj.rect) and obj != bomb_chr:
#             collided_obj.append(obj)
#     for obj in collided_obj:
#         gameobjects.remove(obj)
#     # 객체를 삭제한 후에 gameobjects 리스트에 업데이트해야 함
#     for obj in gameobjects:
#         obj_rect = obj.rect
#         obj.rect = obj.image.get_rect()
#         obj.rect.topleft = obj.rect.topleft
    

#     if shield_rect.colliderect(wall_1_rect) or shield_rect.colliderect(wall_2_rect) or shield_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         velocity = [0, 0]
    

#     #if rush_rect.colliderect(wall_1_rect) or rush_rect.colliderect(wall_2_rect) or rush_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         #rush_angle = new_angle
#         #velocity = [new_velocity_x, new_velocity_y]


#     if doctor_rect.colliderect(wall_1_rect) or doctor_rect.colliderect(wall_2_rect) or doctor_rect.colliderect(wall_3_rect): 
#         #print("충돌했어요")
#         doctor_angle = new_angle
#         velocity = [new_velocity_x, new_velocity_y]
    

#     if engineer_rect.colliderect(wall_1_rect) or engineer_rect.colliderect(wall_2_rect) or engineer_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         engineer_angle = new_angle
#         velocity = [new_velocity_x, new_velocity_y]
    

#     if king_rect.colliderect(wall_1_rect) or king_rect.colliderect(wall_2_rect) or king_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         king_angle = new_angle
#         velocity = [new_velocity_x, new_velocity_y]
    


#     # 빨강팀
#     if ano_warrior_rect.colliderect(wall_1_rect) or ano_warrior_rect.colliderect(wall_2_rect) or ano_warrior_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         ano_warrior_angle = new_angle
#         ano_velocity = [new_velocity_x, new_velocity_y]


#     # 충돌 체크
#     collided_obj = []

#     for obj in gameobjects:
#         if bomb_rect.colliderect(obj.rect) and obj != bomb_chr:
#             collided_obj.append(obj)
#     for obj in collided_obj:
#         gameobjects.remove(obj)
#     # 객체를 삭제한 후에 gameobjects 리스트에 업데이트해야 함
#     for obj in gameobjects:
#         obj_rect = obj.rect
#         obj.rect = obj.image.get_rect()
#         obj.rect.topleft = obj.rect.topleft
    


#     if ano_shield_rect.colliderect(wall_1_rect) or ano_shield_rect.colliderect(wall_2_rect) or ano_shield_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         ano_velocity = [0, 0]


#     if ano_rush_rect.colliderect(wall_1_rect) or ano_rush_rect.colliderect(wall_2_rect) or ano_rush_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         ano_rush_angle = new_angle
#         ano_velocity = [new_velocity_x, new_velocity_y]


#     if ano_doctor_rect.colliderect(wall_1_rect) or ano_doctor_rect.colliderect(wall_2_rect) or ano_doctor_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         ano_doctor_angle = new_angle
#         ano_velocity = [new_velocity_x, new_velocity_y]


#     if ano_engineer_rect.colliderect(wall_1_rect) or ano_engineer_rect.colliderect(wall_2_rect) or ano_engineer_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         ano_engineer_angle = new_angle
#         ano_velocity = [new_velocity_x, new_velocity_y]


#     if ano_king_rect.colliderect(wall_1_rect) or ano_king_rect.colliderect(wall_2_rect) or ano_king_rect.colliderect(wall_3_rect):
#         #print("충돌했어요")
#         ano_king_angle = new_angle
#         ano_velocity = [new_velocity_x, new_velocity_y]

#     '''
#     # 화면 경계를 벗어나지 않게 하기
#     if character_x_pos - character_width < 0:
#         character_x_pos = character_width
#     elif character_x_pos + character_width > Gamescreenwidth:
#         character_x_pos = Gamescreenwidth - character_width

#     if character_y_pos - character_height < 0:
#         character_y_pos = character_height
#     elif character_y_pos + character_height > Gamescreenheight:
#         character_y_pos = Gamescreenheight - character_height
#     '''

    # Gamescreen.blit(Gamescene, (0, 0))

    
#     Gamescreen.blit(Wall_1, (Wall_1_Xpos, Wall_1_Ypos))  # 첫 번째 벽 그리기
#     Gamescreen.blit(Wall_2, (Wall_2_Xpos, Wall_2_Ypos))  # 두 번째 벽 그리기
#     Gamescreen.blit(Wall_3, (Wall_3_Xpos, Wall_3_Ypos))  # 세 번째 벽 그리기

#     if warrior_created:
#         Gamescreen.blit(warrior, (warrior_x_pos, warrior_y_pos))
#         pygame.display.update()

#     if bomb_created:
#         Gamescreen.blit(bomb, (bomb_x_pos, bomb_y_pos))
#         pygame.display.update()

#     if shield_created:
#         Gamescreen.blit(shield, (shield_x_pos, shield_y_pos))
#         pygame.display.update()

#     if rush_created:
#         Gamescreen.blit(rush, (rush_x_pos, rush_y_pos))
#         pygame.display.update()

#     if doctor_created:
#         Gamescreen.blit(doctor, (doctor_x_pos, doctor_y_pos))
#         pygame.display.update()

#     if engineer_created:
#         Gamescreen.blit(engineer, (engineer_x_pos, engineer_y_pos))
#         pygame.display.update()

#     if king_created:
#         Gamescreen.blit(king, (king_x_pos, king_y_pos))
#         pygame.display.update()



#     if ano_warrior_created:
#         Gamescreen.blit(ano_warrior, (ano_warrior_xpos, ano_warrior_ypos))
#         pygame.display.update()

#     if ano_bomb_created:
#         Gamescreen.blit(ano_bomb, (ano_bomb_xpos, ano_bomb_ypos))
#         pygame.display.update()

#     if ano_shield_created:
#         Gamescreen.blit(ano_shield, (ano_shield_xpos, ano_shield_ypos))
#         pygame.display.update()

#     if ano_rush_created:
#         Gamescreen.blit(ano_rush, (ano_rush_xpos, ano_rush_ypos))
#         pygame.display.update()

#     if ano_doctor_created:
#         Gamescreen.blit(ano_doctor, (ano_doctor_xpos, ano_doctor_ypos))
#         pygame.display.update()

#     if ano_engineer_created:
#         Gamescreen.blit(ano_engineer, (ano_engineer_xpos, ano_engineer_ypos))
#         pygame.display.update()

#     if ano_king_created:
#         Gamescreen.blit(ano_king, (ano_king_xpos, ano_king_ypos))
#         pygame.display.update()


#     # 타이머 집어 넣기
#     # 경과 시간 계산
#     #elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
#     # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

#     #timer = game_font.render(str (int (total_time - elapsed_time)), True, (0, 0, 0))
#     # 출력할 글자, True, 글자 색상
#     #Gamescreen.blit(timer, (10, 10))

#     # 만약 시간이 0 이하이면 선택지 불러오기
#     #if total_time - elapsed_time <= 0:
#         #print("타임 아웃")
    

# pygame 종료
pygame.quit()
sys.exit()