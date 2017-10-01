# Name: Brian Allison
# Date: 9/30/2017
# Course: CS325 Online
# Description: Assignment 1, insertion_sort
import random
import time


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            array[j] = key
            j = j - 1
    return array


tot = 0
ave = 0
rand_array = []
# running time code was written based on canvas lecture for hw1 problem 5
file_out = open('insert_time.txt', 'w')
for k in range(0, 11000, 1000):
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
        insertion_sort(rand_array)
        end_time = time.time()

        elapsed_time = end_time - start_time
        tot = tot + elapsed_time
        file_out.write(str(elapsed_time) + ' , ')
        print(elapsed_time, end=' , ')

    ave = tot/3
    print("average: " + str(ave))
    file_out.write("average: " + str(ave) + '\n')

file_out.close()

