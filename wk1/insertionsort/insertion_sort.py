# Name: Brian Allison
# Date: 9/30/2017
# Course: CS325 Online
# Description: Assignment 1, InsertionSort


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
    j = i - 1
    while key < array[j]:
        array[i] = array[j]
        array[j] = key
        j = j - 1
    return array


array = [2, 1, 3, 9, 3]

new_array = insertion_sort(array)
print(new_array)
