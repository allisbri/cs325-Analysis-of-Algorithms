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
            wmap[i].team == 0


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
    print_maps(wmap, rmap)

    file.close()


def print_maps(w, r):
    for i in w:
        print(i + " " + w[i].name)
    print()

    print(r)


wrestler_file_in(sys.argv[1])
