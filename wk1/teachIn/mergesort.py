# Name: Brian Allison
# Date: 9/30/2017
# Course: CS325 Online
# Description: Assignment 1, merge_sort


# sorts an array of ints in O(nlgn) time
def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        mid_split = len(array)/2
        left = merge_sort(array[:int(mid_split)])
        right = merge_sort(array[int(mid_split):])
        array = merge(left, right)
        return array


# helper function for merge_sort. Creates a single sorted array
# made up of the values of the two arrays that are passed in.
# The two arrays that are passed in must already be sorted.
def merge(left, right):
    s_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            s_array.append(left[i])
            i = i + 1
        else:
            s_array.append(right[j])
            j = j + 1

    # source: below if/else blocks created with help from https://www.youtube.com/watch?v=3aTfQvs-_hA&t=255s
    if len(left) <= i:
        s_array.extend(right[j:])
    else:
        s_array.extend(left[i:])
    return s_array


# sorts arrays of ints in a file called data.txt. Prints to a file called insert.out.
# each array in data.txt must start with the size, separated by a space, and continue with
# index values separated by spaces
def file_sort():
    file_in = open('data.txt', 'r')
    file_out = open('merge.out', 'w')
    for line in file_in:
        array_string = line.split()
        # drop first item(size) in array
        array_string = array_string[1:]
        # reference for below line to convert array of strings to ints:
        # https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
        array_int = [int(numeric_string) for numeric_string in array_string]
        sorted_array = merge_sort(array_int)
        for s in sorted_array:
            file_out.write(str(s))
            file_out.write(' ')
        file_out.write('\n')
    file_in.close()
    file_out.close()


file_sort()

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


array1 = [2, 4, 1, 9, 1, 3, 4, 3, 2]

array2 = merge_sort(array1)
print(array2)

'''

