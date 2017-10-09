# Name: Brian Allison
# Date: 10/8/2017
# Course: CS325 Online
# Description: Assignment 1, insertion_sort


# sorts an array of ints in O(n^2) time
# below code was written with the hw2 pseudo code used as a reference
def stooge_sort(array):
    n = len(array)
    if n == 2 and array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
    elif n > 2:
        m = 2 * n % 3
        if r = 0:
            m =
        stooge_sort(array[:m])
        stooge_sort(array[n - m:n])
        stooge_sort(array[:m])

    return array


# sorts arrays of ints in a file called data.txt. Prints to a file called insert.out.
# each array in data.txt must start with the size, separated by a space, and continue with
# index values separated by spaces
def file_sort():
    file_in = open('data.txt', 'r')
    file_out = open('stooge.out', 'w')
    for line in file_in:
        array_string = line.split()
        array_string = array_string[1:]
        # reference for below line to convert array of strings to ints:
        # https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
        array_int = [int(numeric_string) for numeric_string in array_string]
        sorted_array = stooge_sort(array_int)
        for s in sorted_array:
            file_out.write(str(s))
            file_out.write(' ')
        file_out.write('\n')
    file_in.close()
    file_out.close()


file_sort()

