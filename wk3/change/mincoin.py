
# Brian Allison
# Description: Assignment 3: Denominations and change amount
# Course: CS325
# Date: 10/15/2017


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

# sends amounts and denominations to the min_coin function via amount.txt
# and prints the returned data to change.txt
def file_change():
    file_in = open('amount.txt', 'r')
    file_out = open('change.txt', 'w')
    for line in file_in:
        array_string = line.split()
        # reference for below line to convert array of strings to ints:
        # https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
        array_int = [int(numeric_string) for numeric_string in array_string]
        line = next(file_in)
        amount = line
        int_amount = int(amount)
        result = min_coins(array_int, int_amount)

        file_out.write(str(result['denom']))
        file_out.write('\n')
        file_out.write(str(result['amount']))
        file_out.write('\n')
        file_out.write(str(result['result_array']))
        file_out.write('\n')
        file_out.write(str(result['min']))
        file_out.write('\n')
    file_in.close()
    file_out.close()


file_change()






