#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from PyGameUtils import PyGameUtils
from Algorithms.Algorithms import (
    InsertionSort,
    SelectionSort,
    BubbleSort,
    QuickSort,
    MergeSort
)
from Algorithms.Algorithms import Array_Size


def main():
    PyGameUtils.Generate_Array()
    running = True
    while running:
        PyGameUtils.screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    PyGameUtils.Generate_Array()
                if event.key == pygame.K_m:    # Do merge sort
                    PyGameUtils.algorithm = "MergeSort"
                    MergeSort(1, Array_Size)
                if event.key == pygame.K_b:
                    PyGameUtils.algorithm = "BubbleSort"
                    BubbleSort()
                if event.key == pygame.K_s:
                    PyGameUtils.algorithm = "SelectionSort"
                    SelectionSort()
                if event.key == pygame.K_i:
                    PyGameUtils.algorithm = "InsertionSort"
                    InsertionSort()
                if event.key == pygame.K_q:
                    PyGameUtils.algorithm = "QuickSort"
                    QuickSort(1, Array_Size)

        PyGameUtils.Draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
