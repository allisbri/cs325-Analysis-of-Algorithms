# Name: Brian Allison
# Date: 10/8/2017
# Course: CS325 Online
# Description: Assignment 2, stooge_sort


# sorts an array of ints in O(n^2.7) time
# below code was written with the hw2 pseudo code used as a reference
def stooge_sort(array):
    n = len(array)
    if n == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    elif n > 2:
        r = (2 * n) % 3
        print(r)
        if r != 0:
            m = 2 * n // 3 + 1
            print(m)
        else:
            m = 2 * n // 3
            print(m)
        # m = 2 * n // 3 + r + r % 3
        fthird = stooge_sort(array[:int(m)])
        array = fthird + array[int(m):]
        lthird = stooge_sort(array[int(n - m):int(n)])
        array = array[:int(n - m)] + lthird
        fthird = stooge_sort(array[:int(m)])
        array = fthird + array[int(m):]

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

