# Name: Brian Allison
# Date: 9/30/2017
# Course: CS325 Online
# Description: Assignment 1, insertion_sort


# sorts an array of ints in O(n^2) time
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            array[j] = key
            j = j - 1
    return array


# sorts arrays of ints in a file called data.txt. Prints to a file called insert.out.
# each array in data.txt must start with the size, separated by a space, and continue with
# index values separated by spaces
def file_sort():
    file_in = open('data.txt', 'r')
    file_out = open('insert.out', 'w')
    for line in file_in:
        array_string = line.split()
        array_string = array_string[1:]
        # reference for below line to convert array of strings to ints:
        # https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
        array_int = [int(numeric_string) for numeric_string in array_string]
        sorted_array = insertion_sort(array_int)
        for s in sorted_array:
            file_out.write(str(s))
            file_out.write(' ')
        file_out.write('\n')
    file_in.close()
    file_out.close()


file_sort()

