# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:46:30 2016

@author: goodwin
"""

f = open('QuickSort.txt')
int_array = list(map(int, f.read().splitlines()))
f.close()

def quicksort(arr):
    if len(arr) <= 1:
        return 0
    i = 1
    for j in range(1, len(arr)):
        if arr[j] < arr[0]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[0], arr[i-1] = arr[i-1], arr[0]
    print(arr, len(arr)-1)
    return quicksort(arr[0:i-1]) + quicksort(arr[i:]) + len(arr) - 1