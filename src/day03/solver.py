from utils.file import read_file
import re


def create_dir_dict():
    answer = dict()
    answer["U"] = (0, -1)
    answer["D"] = (0, 1)
    answer["L"] = (-1, 0)
    answer["R"] = (1, 0)
    return answer


def create_wire_from_string(wire, dirs=create_dir_dict()):
    x = y = 0
    dist = 1
    answer = dict()
    for wire_part in wire.split(","):
        m = re.search('([DLRU])([0-9]*)', wire_part)
        dx, dy = dirs[m.group(1)]
        for i in range(int(m.group(2))):
            c = (x + dx, y + dy)
            if c not in answer.keys():
                answer[c] = dist
            x += dx
            y += dy
            dist += 1

    return answer


def create_wire(file):
    wire = dict()
    for i, val in enumerate(read_file("day03/{}".format(file)).splitlines()):
        wire[i] = create_wire_from_string(val)

    return wire


def get_intersections(wire1, wire2):
    return wire1.intersection(wire2)


def calc_manhattan_distance(t):
    return abs(t[0]) + abs(t[1])


def a(wires):
    return min(list(map(calc_manhattan_distance, get_intersections(set(wires[0].keys()), set(wires[1].keys())))))


def b(wires):
    r = dict()
    for c in get_intersections(set(wires[0].keys()), set(wires[1].keys())):
        r[c] = wires[0][c] + wires[1][c]

    return min(r.values())


def main():
    wires = create_wire("in.txt")
    print(a(wires))
    print(b(wires))


main()
