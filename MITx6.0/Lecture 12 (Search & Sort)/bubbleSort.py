# -*- coding: utf-8 -*-1

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        print(L)
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                #print('\n')
                #print(L)


test = [1, 5, 3, 8, 4, 2, 9, 6]
