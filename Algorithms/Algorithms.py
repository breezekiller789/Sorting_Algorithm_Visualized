#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from PyGameUtils import PyGameUtils
from PyGameUtils import Colors
import pygame

# To end recursion when user wanted to pause the program
END = -1


Array_Size = 150                                # 總共150筆資料
Array_Color = [Colors.Green] * (Array_Size+1)   # 每筆資料顏色先給綠色
Array = [0] * (Array_Size+1)                    # 一百五十筆資料，初始先給0


def Swap(i, j):
    tmp = Array[i]
    Array[i] = Array[j]
    Array[j] = tmp


def Event_Queue():
    # 讓使用者可以中途暫停
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return True


def ShellSort():
    Span = Array_Size
    Divider = 2
    while Span > 1:
        Span = math.ceil(Span / Divider)
        Have_Swapped = False
        while not Have_Swapped:
            i = 1
            Have_Swapped = False
            while i+Span < Array_Size+1:
                pygame.event.pump()
                Array_Color[i] = Colors.Red
                Array_Color[i+Span] = Colors.Red
                PyGameUtils.Refresh_Page()
                Array_Color[i] = Colors.Green
                Array_Color[i+Span] = Colors.Green
                if Array[i] > Array[i+Span]:
                    Array_Color[i] = Colors.Black
                    Array_Color[i+Span] = Colors.Black
                    PyGameUtils.Refresh_Page()
                    Array_Color[i] = Colors.Green
                    Array_Color[i+Span] = Colors.Green
                    Swap(i, i+Span)
                    Have_Swapped = True
                i += 1
                if Event_Queue():
                    return
            Have_Swapped = not Have_Swapped     # 每一回合必須要做到完全沒有Swap


def CountingSort():
    Range = PyGameUtils.Key_Range
    Output = [0 for i in range(Array_Size+1)]
    Start = [0 for i in range(Range+1)]
    Count = [0 for i in range(Range+1)]

    # 先算出每一個值的個數有多少個
    for idx in range(Array_Size+1):
        pygame.event.pump()
        Array_Color[idx] = Colors.Red
        PyGameUtils.Refresh_Page()
        Count[Array[idx]] += 1
        Array_Color[idx] = Colors.Green
        if Event_Queue():
            return

    Start[0] = 0
    # 算每一個鍵值的擺放起始位置。
    for idx in range(1, Range):
        Start[idx] = Start[idx-1] + Count[idx-1]

    # 從頭開始先拿鍵值，再去Start查表，看這個鍵值的起始位置在哪，就放在那邊，而
    # 這邊會用Output去接起來是因為，如果放回去原始Array的話全部都會被打亂，所以
    # 必須要先放在Output，這個迴圈做完就會是排序好的。
    for idx, num in enumerate(Array):
        pygame.event.pump()
        Output[Start[num]] = num
        Start[num] += 1

    # 把剛剛的Output放回去Array然後印出來
    for idx, num in enumerate(Output):
        pygame.event.pump()
        Array_Color[idx] = Colors.Red
        PyGameUtils.Refresh_Page()
        Array_Color[idx] = Colors.Green
        Array[idx] = num
        if Event_Queue():
            return


# quick sort，用遞迴解，會有if ... return END 是因為必須要讓使用者可以在中途暫停
# 一旦暫停就必須要一路回傳回去，所以才會這樣寫，不然其實不用這麼麻煩。
def QuickSort(p, n):
    if p < n:
        q = Partition(p, n)
        if q == END:
            return END
        if QuickSort(p, q-1) == END:
            return END
        if QuickSort(q+1, n) == END:
            return END


# i走在j後面，j會一直往後走，一旦j遇到比pivot小的，就讓i往後走一步，然後i, j對調
# Ref: 資料結構Quick Sort
def Partition(p, n):
    if p-n >= 2:
        idx = Middle_Of_Three(p, n)         # 避免worst case飆到n^2
        Pivot = Array[idx]
        Array_Color[idx] = Colors.Black
    else:
        Pivot = Array[n]
        Array_Color[n] = Colors.Black
    i = p - 1
    for j in range(p, n+1):
        pygame.event.pump()
        Array_Color[i] = Colors.Red     # 正在比較的兩筆換成紅色
        Array_Color[j] = Colors.Red     # 正在比較的兩筆換成紅色
        PyGameUtils.Refresh_Page()
        Array_Color[i] = Colors.Green   # 換回來
        Array_Color[j] = Colors.Green   # 換回來
        if Array[j] < Pivot:
            i += 1
            Swap(i, j)

        # 讓使用者可以中途暫停，這邊因為是遞迴，所以必須一直回傳END回去，這樣
        # 才會一直往回
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return END

    # 走到最後還要把pivot插回去，並且回傳插入的位置。
    i += 1
    tmp = Array[i]
    Array[i] = Array[n]
    Array[n] = tmp
    return i


def Middle_Of_Three(p, n):
    middle = (p+n)//2
    three = [Array[p], Array[n], Array[middle]]
    return sorted(three)[1]


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
                Swap(j+1, j)
                # tmp = Array[j+1]
                # Array[j+1] = Array[j]
                # Array[j] = tmp
            if Event_Queue():
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

            if Event_Queue():
                return

        if i != Min_Index:
            Swap(i, Min_Index)


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
            Array[j+1] = Array[j]           # Insert!!
            j -= 1
            if Event_Queue():
                return
        Array[j+1] = key
