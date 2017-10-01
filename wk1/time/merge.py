# Name: Brian Allison
# Date: 9/30/2017
# Course: CS325 Online
# Description: Assignment 1, merge_sort

import time
import random


def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        mid_split = len(array)/2
        left = merge_sort(array[:int(mid_split)])
        right = merge_sort(array[int(mid_split):])
        array = merge(left, right)
        return array


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


tot = 0
ave = 0
rand_array = []
# running time code was written based on canvas lecture for hw1 problem 5
file_out = open('merge_time.txt', 'w')
for k in range(0, 110000, 10000):
    file_out.write(str(k) + ' , ')
    print(k, end=' , ')
    tot = 0
    ave = 0

    for l in range(3):
        rand_array = []
        for m in range(k):
            random_number = random.randint(0, 1000)
            rand_array.append(random_number)

        start_time = time.time()
        merge_sort(rand_array)
        end_time = time.time()

        elapsed_time = end_time - start_time
        tot = tot + elapsed_time
        file_out.write(str(elapsed_time) + ' , ')
        print(elapsed_time, end=' , ')

    ave = tot/3
    print("average: " + str(ave))
    file_out.write("average: " + str(ave) + '\n')

file_out.close()



'''
    file_in = open('data.txt', 'r')
    
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

