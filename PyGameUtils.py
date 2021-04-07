#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import pygame

pygame.init()
pygame.font.init()

Width = 900      # 螢幕寬度
Height = 650     # 螢幕高度
Key_Range = 100  # 設定最大鍵值
algorithm = ""
screen = pygame.display.set_mode((Width, Height))   # 初始化螢幕

# 設定標題
pygame.display.set_caption("Merge Sort")
Array_Size = 150    # 總共150筆資料
Array_Color = [(0, 204, 102)] * (Array_Size+1)  # 每筆資料顏色先給綠色
Array = [0] * (Array_Size+1)        # 一百五十筆資料，初始先給0
Colors = [
    (0, 204, 102),  # 青綠色
    (255, 0, 0),    # 鮮紅色
    (0, 0, 0),      # 黑
    (255, 102, 0)   # 橘色
]

# 先設定字體
fnt1 = pygame.font.SysFont("arial", 20)
fnt2 = pygame.font.SysFont("arial", 30)


# 生產一個隨機的array
def Generate_Array():
    for i in range(1, Array_Size+1):
        Array_Color[i] = Colors[0]  # 都先設定青綠色
        Array[i] = random.randrange(1, Key_Range)       # 隨機產生input


def Refresh_Page():
    '''
        Refresh the whole page including the input array and strings, algorithm
    '''
    screen.fill((255, 255, 255))
    Draw()
    pygame.display.update()
    pygame.time.delay(5)


# 更新整個畫面。
def Draw():
    '''
    Draw the entire frame on the main page, including user info and instructions
    and array structures
    '''
    # 寫出畫面上的字，先用render來回傳一個Surface然後再用blit貼上去。
    nav1 = fnt1.render("i: Insertion Sort.", True, (0, 0, 0))
    nav2 = fnt1.render("s: SelectionSort.", True, (0, 0, 0))
    nav3 = fnt1.render("b: BubbleSort.", True, (0, 0, 0))
    nav4 = fnt1.render("m: MergeSort.", True, (0, 0, 0))
    nav5 = fnt1.render("q: QuickSort.", True, (0, 0, 0))
    space_to_stop = fnt1.render("<space> to stop", True, (0, 0, 0))
    recreate = fnt1.render("<r> to recreate array", True, (0, 0, 0))
    Algo_Info = fnt1.render("Algorithm: "+algorithm, True, (0, 0, 0))

    # 貼上螢幕。
    screen.blit(nav1, (20, 10))
    screen.blit(nav2, (20, 40))
    screen.blit(nav3, (20, 70))
    screen.blit(nav4, (200, 10))
    screen.blit(nav5, (200, 40))
    screen.blit(Algo_Info, (600, 40))
    screen.blit(recreate, (600, 70))
    screen.blit(space_to_stop, (600, 10))

    Boundry_Width = int(Width/Array_Size)       # 每一個小格子的寬
    # Boundry_Height = int(Height/Array_Size)       # 每一個小格子的寬

    # 畫出分界線。
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (900, 100), 6)

    for i in range(1, Key_Range):
        pygame.draw.line(screen,                        # Surface
                         (200, 200, 200),               # Color
                         (0, i*Boundry_Width+100),      # Start_X_Axis
                         (900, i*Boundry_Width+100),    # Start_Y_Axis
                         1)                             # Width
    for i in range(1, Array_Size+1):
        # print(i, Array[i])
        pygame.draw.line(screen,
                         Array_Color[i],
                         ((i-1)*Boundry_Width, 106),
                         ((i-1)*Boundry_Width, 106+Array[i]*Boundry_Width),
                         Boundry_Width)
