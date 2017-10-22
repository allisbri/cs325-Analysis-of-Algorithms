# Name: Brian Allison
# Date: 10/8/2017
# Course: CS325 Online
# Description: Assignment 2, stooge_sort

import time
import random


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
        if r != 0:
            m = 2 * n // 3 + 1
        else:
            m = 2 * n // 3
        fthird = stooge_sort(array[:int(m)])
        array = fthird + array[int(m):]
        lthird = stooge_sort(array[int(n - m):int(n)])
        array = array[:int(n - m)] + lthird
        fthird = stooge_sort(array[:int(m)])
        array = fthird + array[int(m):]

    return array


# below running time code was written based on canvas lecture for hw1 problem 5
tot = 0
ave = 0
rand_array = []

file_out = open('stooge_time.txt', 'w')
for k in range(0, 500, 50):
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
        stooge_sort(rand_array)
        end_time = time.time()

        elapsed_time = end_time - start_time
        tot = tot + elapsed_time
        file_out.write(str(elapsed_time) + ' , ')
        print(elapsed_time, end=' , ')

    ave = tot/3
    print("average: " + str(ave))
    file_out.write("average: " + str(ave) + '\n')

file_out.close()