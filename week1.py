# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:21:51 2016

@author: goodwin
"""
#import string

f = open('week1.txt')
intArray = list(map(int, f.read().splitlines()))
f.close()

def count(array):
    '''
input: unsorted array
output: sorted array, int # of inversions in original array
    '''
    length = len(array)
    if length <= 1:
        return (array, 0)
    else:
        A, a = count(array[0:length//2])
        B, b = count(array[length//2:])
        C, c = countSplit(A, B)
#        print(A,B,C,a,b,c)
    
        return (C, a + b + c)

def countSplit(left, right):
    '''
input: 2 sorted lists
output: combined sorted list, int # of split inversions
    '''
    i = 0
    j = 0
    inversions = 0
    combined = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            inversions += len(left[i:])
            j += 1
    if i == len(left):
        combined += right[j:]
    else:
        assert j == len(right)
        combined += left[i:]
#        inversions += len(left[i:])
#    print(combined)

    assert len(combined) == len(left) + len(right)
    return (combined, inversions)