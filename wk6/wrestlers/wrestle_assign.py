
# Brian Allison
# Description: Assignment 4, Activity Selection
# Course: CS325
# Date: 10/22/2017

import sys

# general: This class is used for activities that have a start and finish time.
# params: identification number, a start time, and a finish time
# conditions: Comparison operators for this class are overridden so that activities are compared by finish time
class Activity:
    def __init__(self, team_in, status_in):
        self.team = team_in
        self.status = status_in


# general: sorts an array of any type that works with comparison operators
# params: an array of any type that can utilize comparison operators
# return: sorted array in ascending order
def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        mid_split = len(array)/2
        left = merge_sort(array[:int(mid_split)])
        right = merge_sort(array[int(mid_split):])
        array = merge(left, right)
        return array


# general: helper function for merge_sort. Creates a single sorted array
# made up of the values of the two arrays that are passed in.
# params: two sorted arrays
# conditions: The two arrays that are passed in must already be sorted.
# return: sorted array
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


# general: Imports lists of activities from a file and provides an optimal scheduling solution for
# each list
# params: a list titled act.txt with the format of: number of activities on first line,
# on each proceeding line: activity id, activity start (int), activity finish (int)
# if there is more than one activity, continue with number of activities on next line, etc...
# return: nothing returned. prints solution details for each list to terminal
def wrestler_file_in():
    file_in = open(sys.argv[1], 'r')
    accum = 1
    try:  # prevents error message if txt file has any trailing white space after last line
        for line in file_in:
            w_size = int(line)
            w_array = []
            for i in range(0, w_size):
                w_name = next(file_in)
                w_array.append(w_name)
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
    except:  # prevents false error message if txt file has any trailing white space after last line
        print('')
    file_in.close()


# general: provides a solution for a sorted array of activities
# params: sorted array of activity objects
# return: array that is an optimal solution containing the highest possible amount of non-conflicting activities
# References: Followed lecture 3 from this week to help understand this problem
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


# everything below is used for testing purposes

# general: used to print an array of activities
# def print_activities(array):
#     for i in array:
#         print("num: " + str(i.num) + " start: " + str(i.start) + ", finish: " + str(i.finish))


