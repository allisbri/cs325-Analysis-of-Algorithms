
# Brian Allison
# Description: Assignment 3: Denominations and change amount
# Course: CS325
# Date: 10/15/2017

import random
import time


# This class is used to track the amount and method associated
# with the use of a particular denomination of coin in the
# coin change problem
class Coin:
    def __init__(self, num, op):
        self.num = num
        self.op = op


# Args: Array of coin denominations starting with 1
#       Int that is the amount we want to get to with the least amount of change
# Returns: A dictionary containing 'denom' - same array that was passed in,
#           'amount' - same amount that was passed in
#           'result_array' - array of number of each denom used
#           'min' - min number of coins needed
def min_coins(denom, amount):
    coins = []
    for col in range(0, amount + 1):
        for row in range(0, len(denom)):
            if col == 0:
                coins.append([])
                newcoin = Coin(0, 2)
                coins[row].append(newcoin)
            elif row == 0:
                newcoin = Coin(col, 0)
                coins[0].append(newcoin)
            elif denom[row] <= col:
                op0 = 1 + coins[row][col - denom[row]].num
                op1 = coins[row - 1][col].num
                if op0 <= op1:
                    newcoin = Coin(op0, 0)
                else:
                    newcoin = Coin(op1, 1)

                coins[row].append(newcoin)
            else:
                oneabove = coins[row - 1][col].num
                newcoin = Coin(oneabove, 1)
                coins[row].append(newcoin)

    return coins_info(denom, amount, coins)


# helper function of min_coins
def coins_info(denom, amount, coins_array):
    x = amount
    y = len(coins_array) - 1
    m = coins_array[y][x].num
    c = [0] * len(coins_array)

    while x > 0:
        if coins_array[y][x].op == 1:
            y = y - 1
        else:
            c[y] = c[y] + 1
            x = x - denom[y]

    return {'denom': denom, 'amount': amount, 'result_array': c, 'min': m}


file_out = open('amount_time.txt', 'w')
for k in range(11, 100011, 10011):
    file_out.write('amount, ' + str(k) + ' , ')
    print(k, end=' , ')
    tot = 0
    ave = 0

    for l in range(3):
        rand_denom = []
        rand_denom.append(1)

        randsamp = random.sample(range(2, k), 9)
        rand_denom = rand_denom + randsamp

        start_time = time.time()
        min_coins(rand_denom, k)
        end_time = time.time()

        elapsed_time = end_time - start_time
        tot = tot + elapsed_time
        file_out.write(str(elapsed_time) + ' , ')
        print(elapsed_time, end=' , ')

    ave = tot/3
    print("average: " + str(ave))
    file_out.write("average: " + str(ave) + '\n')

file_out.close()

file_out = open('denom_time.txt', 'w')
for k in range(10, 1000, 100):
    file_out.write('denom, ' + str(k) + ' , ')
    print(k, end=' , ')
    tot = 0
    ave = 0

    for l in range(3):
        rand_denom = []
        rand_denom.append(1)
        if (k >= 1010):
            randsamp = random.sample(range(2, 1011), k)

        randsamp = random.sample(range(2, 1011), k)
        rand_denom = rand_denom + randsamp

        start_time = time.time()
        min_coins(rand_denom, 1011)
        end_time = time.time()

        elapsed_time = end_time - start_time
        tot = tot + elapsed_time
        file_out.write(str(elapsed_time) + ' , ')
        print(elapsed_time, end=' , ')

    ave = tot/3
    print("average: " + str(ave))
    file_out.write("average: " + str(ave) + '\n')

file_out.close()

file_out = open('amount_denom_time.txt', 'w')
for k in range(20, 2010, 200):
    file_out.write('amount and denom, ' + str(k) + ' , ')
    print(k, end=' , ')
    tot = 0
    ave = 0

    for l in range(3):
        rand_denom = []
        rand_denom.append(1)

        randsamp = random.sample(range(2, k), k - 2)
        rand_denom = rand_denom + randsamp

        start_time = time.time()
        min_coins(rand_denom, k)
        end_time = time.time()

        elapsed_time = end_time - start_time
        tot = tot + elapsed_time
        file_out.write(str(elapsed_time) + ' , ')
        print(elapsed_time, end=' , ')

    ave = tot/3
    print("average: " + str(ave))
    file_out.write("average: " + str(ave) + '\n')

file_out.close()
