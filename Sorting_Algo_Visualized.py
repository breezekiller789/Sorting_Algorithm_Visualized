#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import Algorithms
import PyGameUtils


def main():
    PyGameUtils.Generate_Array()
    running = True
    text = None
    while running:
        PyGameUtils.screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Algorithms.Generate_Array()
                if event.key == pygame.K_m:    # Do merge sort
                    PyGameUtils.algorithm = "MergeSort"
                    Algorithms.MergeSort(1, PyGameUtils.Array_Size)
                if event.key == pygame.K_b:
                    PyGameUtils.algorithm = "BubbleSort"
                    Algorithms.BubbleSort()
                if event.key == pygame.K_s:
                    PyGameUtils.algorithm = "SelectionSort"
                    Algorithms.SelectionSort()
                if event.key == pygame.K_i:
                    PyGameUtils.algorithm = "InsertionSort"
                    Algorithms.InsertionSort()
                if event.key == pygame.K_q:
                    PyGameUtils.algorithm = "QuickSort"
                    Algorithms.QuickSort(1, PyGameUtils.Array_Size)

        if text is not None:
            PyGameUtils.screen.blit(text, (370, 300))

        PyGameUtils.Draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
