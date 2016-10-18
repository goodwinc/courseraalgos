# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:51:11 2016

@author: gchen
"""
f = open('QuickSort.txt')
int_array = list(map(int, f.read().splitlines()))
f.close()


def quicksort(arr, start, stop):
    if stop - start <= 1:
        return 0
    i = start + 1
    for j in range(start + 1, stop):
        if arr[j] < arr[start]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return quicksort(arr, start, i-1) + quicksort(arr, i, stop) + stop - start -1
    
def quicksort_last(arr, start, stop):
    if stop - start <= 1:
        return 0
    arr[stop - 1], arr[start] = arr[start], arr[stop - 1]
    i = start + 1
    for j in range(start + 1, stop):
        if arr[j] < arr[start]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return quicksort_last(arr, start, i-1) + quicksort_last(arr, i, stop) + stop - start -1
    
def quicksort_median(arr, start, stop):
    if stop - start <= 1:
        return 0
    mid_idx = (start + stop - 1) // 2
    if arr[mid_idx] < min(arr[start], arr[stop-1]):
        if arr[start] < arr[stop-1]:
            median_idx = start
        else:
            median_idx = stop - 1
    elif arr[mid_idx] > max(arr[start], arr[stop-1]):
        if arr[start] > arr[stop-1]:
            median_idx = start
        else:
            median_idx = stop - 1
    else:
        median_idx = mid_idx
    arr[median_idx], arr[start] = arr[start], arr[median_idx]
    i = start + 1
    for j in range(start + 1, stop):
        if arr[j] < arr[start]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return quicksort_median(arr, start, i-1) + quicksort_median(arr, i, stop) + stop - start -1
    