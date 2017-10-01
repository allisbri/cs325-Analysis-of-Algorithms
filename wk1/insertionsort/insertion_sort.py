# Name: Brian Allison
# Date: 9/30/2017
# Course: CS325 Online
# Description: Assignment 1, InsertionSort


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            array[j] = key
            j = j - 1

    return array


def file_sort():
    file_in = open('data.txt', 'r')
    file_out = open()
    for line in file_in:
        array_string = line.split();
        array_string = array_string[1:]
        # reference for below line to convert array of strings to ints
        # https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
        array_int = [int(numeric_string) for numeric_string in array_string]
        print(insertion_sort(array_int))
    file_in.close()

fileOut = open('insert.out', 'w')
'''
array = [4, 2, 1]

new_array = insertion_sort(array)
print(new_array)
'''