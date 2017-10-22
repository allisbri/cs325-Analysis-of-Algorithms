
# Brian Allison
# Description: Assignment 4: Denominations and change amount
# Course: CS325
# Date: 10/15/2017


# This class is used to track the amount and method associated
# with the use of a particular denomination of coin in the
# coin change problem
class Activity:
    def __init__(self, num, start, finish):
        self.num = num
        self.start = start
        self.finish = finish

    def __lt__(self, other):
        return self.start < other.start

    def ___le__(self, other):
        return self.start <= other.start

    def __eq__(self, other):
        return self.start == other.start

    def __ne__(self, other):
        return self.start != other.start

    def __gt__(self, other):
        return self.start > other.start

    def __ge__(self, other):
        return self.start >= other.start


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


def print_activities(array):
    for i in array:
        print("num: " + str(i.num) + " start: " + str(i.start) + ", finish: " + str(i.finish))


def activity_file_solve():
    file_in = open('act.txt', 'r')
    accum = 1
    for line in file_in:
        act_size = int(line)
        activity_array = []
        for i in range(0, act_size):
            line = next(file_in)
            array_string = line.split()
            # reference for below line to convert array of strings to ints:
            # https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
            array_int = [int(num_string) for num_string in array_string]
            act = Activity(*array_int)
            activity_array.append(act)
        sorted_array = merge_sort(activity_array)
        sorted_array = sorted_array[::-1]
        solved = activity_selector(sorted_array)
        print("Set " + str(accum))
        print("Number of activities selected = " + str(len(solved)))
        print("Activities: ", end='')
        for j in range(0, len(solved)):
            print(str(solved[j].num) + ' ', end='')
        print()
        accum += 1
    file_in.close()


def activity_selector(sorted_array):
    solution = [sorted_array[0]]
    current = solution[0]
    for i in range(1, len(sorted_array)):
        if current.start >= sorted_array[i].finish:
            solution.append(sorted_array[i])
            current = sorted_array[i]
    solution = solution[::-1]
    return solution


activity_file_solve()


