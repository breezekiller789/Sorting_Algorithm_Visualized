#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import pygame
from Algorithms import Algorithms as Algo
from . import Colors
from . import Fonts

pygame.init()

Width = 900      # 螢幕寬度
Height = 650     # 螢幕高度
Key_Range = 100     # 設定最大鍵值
algorithm = ""
screen = pygame.display.set_mode((Width, Height))   # 初始化螢幕

# 設定標題
pygame.display.set_caption("Merge Sort")


# 生產一個隨機的array
def Generate_Array():
    for i in range(1, Algo.Array_Size+1):
        # 都先設定青綠色
        Algo.Array_Color[i] = Colors.Green
        # 隨機產生input
        Algo.Array[i] = random.randrange(1, Key_Range)


# 刷新頁面
def Refresh_Page():
    '''
        Refresh the whole page including the input array and strings, algorithm
    '''
    screen.fill((255, 255, 255))
    Draw()
    pygame.display.update()
    pygame.time.delay(5)


# 畫出整個頁面，包含標題，注意事項等等。
def Draw():
    '''
    Draw the entire frame on the main page, including user info and instructions
    and array structures
    '''
    # 寫出畫面上的字，先用render來回傳一個Surface然後再用blit貼上去。
    nav1 = Fonts.FontTitleSmall.render("i: Insertion Sort.", True, (0, 0, 0))
    nav2 = Fonts.FontTitleSmall.render("s: SelectionSort.", True, (0, 0, 0))
    nav3 = Fonts.FontTitleSmall.render("b: BubbleSort.", True, (0, 0, 0))
    nav4 = Fonts.FontTitleSmall.render("m: MergeSort.", True, (0, 0, 0))
    nav5 = Fonts.FontTitleSmall.render("q: QuickSort.", True, (0, 0, 0))

    space_to_stop = Fonts.FontTitleSmall.render(
        "<space> to stop", True, (0, 0, 0))

    recreate = Fonts.FontTitleSmall.render(
        "<r> to recreate array", True, (0, 0, 0))

    Algo_Info = Fonts.FontTitleSmall.render(
        "Algorithm: "+algorithm, True, (0, 0, 0))

    # 貼上螢幕。
    screen.blit(nav1, (20, 10))
    screen.blit(nav2, (20, 40))
    screen.blit(nav3, (20, 70))
    screen.blit(nav4, (200, 10))
    screen.blit(nav5, (200, 40))
    screen.blit(Algo_Info, (600, 40))
    screen.blit(recreate, (600, 70))
    screen.blit(space_to_stop, (600, 10))

    Boundry_Width = int(Width/Algo.Array_Size)       # 每一個小格子的寬
    # Boundry_Height = int(Height/Array_Size)       # 每一個小格子的寬

    # 畫出分界線。
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (900, 100), 6)

    for i in range(1, Key_Range):
        pygame.draw.line(screen,                        # Surface
                         (200, 200, 200),               # Color
                         (0, i*Boundry_Width+100),      # Start_X_Axis
                         (900, i*Boundry_Width+100),    # Start_Y_Axis
                         1)                             # Width
    # 畫出所有陣列值，這邊是上下顛倒著印。
    for i in range(1, Algo.Array_Size+1):
        pygame.draw.line(
            screen,
            Algo.Array_Color[i],
            ((i-1)*Boundry_Width, 106),
            ((i-1)*Boundry_Width, 106+Algo.Array[i]*Boundry_Width),
            Boundry_Width)
