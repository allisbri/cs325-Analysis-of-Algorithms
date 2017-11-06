
# Brian Allison
# Description: Assignment 5, Wrestler Team Assignment
# Course: CS325
# Date: 11/5/2017

import sys
import queue


# general: This class is used for wrestler objects that have a name and a team number
# params: team id number (int), name (string)
# conditions: team id should be either -1 (no team), 0 (babyface), 1 (heel)
class Wrestler:
    def __init__(self, name_in, team_in):
        self.name = name_in
        self.team = team_in


# general: Does a bfs of rmap, assigns the opposite team for rivals in wmap, if possible. If
# opposite teams are not possible, calls a print function to let the user know. If opposite teams
# are possible, calls a function that prints the team assignments.
# params: wmap: a dictionary containing wrestler objects, referenced by wrestler name. Contains a team variable that
#               represents the team the wrestler is on
#         rmap: a dictionary containing string type arrays of rivals, referenced by wrestler name. The map is used
#               to navigate graphs of rivals and assign wrestler objects in the wmap the appropriate team
# return: nothing returned. calls print functions to print solution details
def wrestler_bfs(wmap, rmap):
    for i in rmap:
        if wmap[i].team == -1:
            q = queue.Queue()
            q.put(i)
            wmap[i].team = 0
            while not q.empty():
                nextv = q.get()
                for j in rmap[nextv]:
                    if wmap[nextv].team == wmap[j].team:
                        print_no()
                        return
                    elif wmap[j].team == -1:
                        wmap[j].team = ((wmap[nextv].team - 1) * -1)
                        q.put(j)
    print_teams(wmap)


# general: Creates a map of wrestler objects and a map of wrestler rivalry arrays consistent with the
# rivals in the wrestler object map
# params: name of file with the wrestler information
# return: nothing returned. calls wrestler_bfs function, passing the maps to the function
def wrestler_file_in(file_name):
    file = open(file_name, 'r')
    w_size = int(file.readline().rstrip())
    wmap = {}
    rmap = {}
    for i in range(0, w_size):
        w_name = file.readline().rstrip()
        wrestler = Wrestler(w_name, -1)
        wmap[w_name] = wrestler

    r_size = int(file.readline().rstrip())
    for j in range(0, r_size):
        rline = file.readline().rstrip().split()
        if rline[0] in rmap:
            rmap[rline[0]].append(rline[1])
        else:
            rmap[rline[0]] = [rline[1]]
        if rline[1] in rmap:
            rmap[rline[1]].append(rline[0])
        else:
            rmap[rline[1]] = [rline[0]]

    file.close()
    wrestler_bfs(wmap, rmap)


# general: prints wrestler team results
def print_teams(w):
    babyfaces = []
    heels = []
    for i in w:
        if w[i].team == 0:
            babyfaces.append(i)
        else:
            heels.append(i)

    print('yes')
    print('Babyfaces: ' + ', '.join(babyfaces))
    print('Heels: ' + ', '.join(heels))


# general: informs user that teams cannot be assigned, due to shared rivals
def print_no():
    print('No. At least one rivalry is shared by a pair of rivals.')


wrestler_file_in(sys.argv[1])


# def print_maps(w, r):
#     for i in w:
#         print(w[i].name + ' ' + str(w[i].team))
#     print()
#
#     print(r)
