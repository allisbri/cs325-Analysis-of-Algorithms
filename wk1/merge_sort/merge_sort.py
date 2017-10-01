# Name: Brian Allison
# Date: 9/30/2017
# Course: CS325 Online
# Description: Assignment 1, merge_sort


def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        mid_split = len(array)/2
        print(array[:int(mid_split)])
        left = merge_sort(array[:int(mid_split)])
        right = merge_sort(array[int(mid_split):])
        array = merge(left, right)
        return array


def merge(left, right):
    s_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        print(s_array)
        if left[i] < right[j]:
            s_array.append(left[i])
            i = i + 1
        else:
            s_array.append(right[j])
            j = j + 1

    if len(left) <= i:
        s_array.append(right[j:])
    else:
        s_array.append(left[i:])
    return s_array

'''
recurrsive merge 

def merge2(left, right):
    if len(left) < 1:
        return right
    if len(right) < 1:
        return left
    if left[0] < right[0]:
        new_left = [left[0]] + [left[1:]]
        return merge2(new_left, right)
    else:
        new_right = [right[0]] + [left[1:]]
        return merge2(left, new_right)
'''

array1 = [2, 4, 1, 9, 1, 3, 4, 3, 2]

array2 = merge_sort(array1)
print(array2)



