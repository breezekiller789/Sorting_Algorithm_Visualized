#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyGameUtils import PyGameUtils
from PyGameUtils import Colors
import pygame

# To end recursion when user wanted to pause the program
END = -1

Array_Size = 150    # 總共150筆資料
Array_Color = [Colors.Green] * (Array_Size+1)   # 每筆資料顏色先給綠色
Array = [0] * (Array_Size+1)        # 一百五十筆資料，初始先給0


# quick sort，用遞迴解。
def QuickSort(p, n):
    if p < n:
        q = Partition(p, n)
        if q == END:
            return END
        if QuickSort(p, q-1) == END:
            return END
        if QuickSort(q+1, n) == END:
            return END


def Partition(p, n):
    Pivot = Array[n]
    i = p - 1
    Array_Color[n] = Colors.Black
    for j in range(p, n+1):
        pygame.event.pump()
        Array_Color[i] = Colors.Red     # 正在比較的兩筆換成紅色
        Array_Color[j] = Colors.Red     # 正在比較的兩筆換成紅色
        PyGameUtils.Refresh_Page()
        Array_Color[i] = Colors.Green   # 換回來
        Array_Color[j] = Colors.Green   # 換回來
        if Array[j] < Pivot:
            i += 1
            tmp = Array[j]
            Array[j] = Array[i]
            Array[i] = tmp
        # 讓使用者可以中途暫停
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return END

    i += 1
    tmp = Array[i]
    Array[i] = Array[n]
    Array[n] = tmp
    return i


# Merge sort遞迴解
def MergeSort(l, r):
    mid = (l+r)//2
    if l < r:
        if MergeSort(l, mid) == END:
            return END
        if MergeSort(mid+1, r) == END:
            return END
        if Merge(l, mid, mid+1, r) == END:
            return END


# 因為MergeSort是遞迴，所以沒辦法中途讓使用者暫停ＱＱ。
def Merge(l, x1, x2, r):
    i = l
    j = x2
    temp = []
    while i <= x1 and j <= r:
        pygame.event.pump()
        Array_Color[i] = Colors.Red         # 正在比較的兩筆換成紅色
        Array_Color[j] = Colors.Red         # 正在比較的兩筆換成紅色
        PyGameUtils.Refresh_Page()
        Array_Color[i] = Colors.Green       # 換回來
        Array_Color[j] = Colors.Green       # 換回來
        if Array[i] < Array[j]:
            temp.append(Array[i])
            i += 1
        else:
            temp.append(Array[j])
            j += 1
        # 讓使用者可以中途暫停
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return END

    # 可能左半邊還有剩下，直接全部append到temp
    while i <= x1:
        pygame.event.pump()
        Array_Color[i] = Colors.Red
        PyGameUtils.Refresh_Page()
        Array_Color[i] = Colors.Green
        temp.append(Array[i])
        i += 1

    # 可能右半邊還有剩下，直接全部append到temp
    while j <= r:
        pygame.event.pump()
        Array_Color[j] = Colors.Red
        PyGameUtils.Refresh_Page()
        Array_Color[j] = Colors.Green
        temp.append(Array[j])
        j += 1

    # 走到這裡代表全部都排好放在temp，現在就是進去把它印出來。
    i = 0
    for idx in range(l, r+1):
        pygame.event.pump()
        Array[idx] = temp[i]
        i += 1
        Array_Color[idx] = Colors.Black
        PyGameUtils.Refresh_Page()
        Array_Color[idx] = Colors.Green
        # 讓使用者可以中途暫停
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return END


def BubbleSort():
    for i in range(1, Array_Size+1):
        for j in range(1, Array_Size+1-i):
            pygame.event.pump()
            Array_Color[j] = Colors.Red     # 把目前位置標記起來，用紅色標起來
            PyGameUtils.Refresh_Page()      # 畫面重刷
            Array_Color[j] = Colors.Green   # 顏色換回來
            if Array[j+1] > Array[j]:
                tmp = Array[j+1]
                Array[j+1] = Array[j]
                Array[j] = tmp
            # 讓使用者可以中途暫停
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return


def SelectionSort():
    for i in range(1, Array_Size):
        Min_Index = i
        for j in range(i+1, Array_Size+1):
            pygame.event.pump()
            Array_Color[j] = Colors.Red     # 把目前位置標記起來，用紅色標起來
            PyGameUtils.Refresh_Page()      # 畫面重刷
            Array_Color[j] = Colors.Green   # 顏色換回來
            # 這邊的邏輯跟原本的不一樣，因為陣列是倒著放的，所以大跟小要反過來。
            if Array[j] < Array[Min_Index]:
                Min_Index = j
            # 讓使用者可以中途暫停
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

        if i != Min_Index:
            tmp = Array[i]
            Array[i] = Array[Min_Index]
            Array[Min_Index] = tmp


def InsertionSort():
    for i in range(2, Array_Size+1):
        key = Array[i]
        Array_Color[i] = Colors.Red
        j = i-1
        while j > 0 and key < Array[j]:
            pygame.event.pump()
            Array_Color[j] = Colors.Red
            PyGameUtils.Refresh_Page()
            Array_Color[i] = Colors.Green
            Array_Color[j] = Colors.Green
            Array[j+1] = Array[j]       # Insert!!
            j -= 1
            # 讓使用者可以中途暫停
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
        Array[j+1] = key
