import sys

# general: This class is used for activities that have a start and finish time.
# params: identification number, a start time, and a finish time
# conditions: Comparison operators for this class are overridden so that activities are compared by finish time


class Wrestler:
    def __init__(self, name_in, team_in, status_in):
        self.name = name_in
        self.team = team_in
        self.status = status_in


def wrestler_bfs(wmap, rmap):
    for i in rmap:
        if wmap[i].team == -1:
            Q = [i]
            wmap[i].team = 0
            while Q:
                nextv = Q.pop(0)
                for j in rmap[nextv]:
                    if wmap[nextv].team == wmap[j].team:
                        return
                    elif wmap[j].team == -1:
                        wmap[j].team = ((wmap[nextv].team - 1) * -1)
                        Q.append(j)
    print_maps(wmap, rmap)


def wrestler_file_in(file_name):
    file = open(file_name, 'r')
    w_size = int(file.readline().rstrip())
    wmap = {}
    rmap = {}
    for i in range(0, w_size):
        w_name = file.readline().rstrip()
        wrestler = Wrestler(w_name, -1, 0)
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
    print_maps(wmap, rmap)
    wrestler_bfs(wmap, rmap)


def print_maps(w, r):
    for i in w:
        print(w[i].name + ' ' + str(w[i].team))
    print()

    print(r)


wrestler_file_in(sys.argv[1])
