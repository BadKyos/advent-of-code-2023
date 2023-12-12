import math
import re


def run_part1():
    with open("input/day8.input", "r") as filin:
        file = filin.read().splitlines()
        maps = {}
        start= "AAA"
        end = "ZZZ"
        i=0
        for line in enumerate(file):
            if line[0] == 0:
                dir_list = line[1]
                continue
            elif int(line[0]) > 1:
                road = line[1].split(" = ")
                next = road[1].replace("(", "").replace(")", "").split(", ")
                maps.update({road[0]: {"L": next[0], "R": next[1]}})

        while start != end:
            for dir in dir_list:
                i += 1
                start = maps[start][dir]
                if start == end:
                    break
        print(i)


def run_part2():
    with open("input/day8.input", "r") as filin:
        file = filin.read().splitlines()
        maps = {}
        start_pattern = "[A-Z]{2}A"
        end_pattern = "[A-Z]{2}Z"
        list_start = []
        list_result = []
        i = 0
        for line in enumerate(file):
            if line[0] == 0:
                dir_list = line[1]
                continue
            elif int(line[0]) > 1:
                road = line[1].split(" = ")
                if re.search(start_pattern, road[0]):
                    list_start.append(road[0])
                next = road[1].replace("(", "").replace(")", "").split(", ")
                maps.update({road[0]: {"L": next[0], "R": next[1]}})

        for start in list_start:
            i = 0
            while re.search(end_pattern, start) is None:
                for dir in dir_list:
                    i += 1
                    start = maps[start][dir]
                    if re.search(end_pattern, start):
                        break

            list_result.append(i)

        commun = 1
        for result in list_result:
            commun = math.lcm(commun, int(result))

        print(commun)


if __name__ == '__main__':
    run_part1()
    run_part2()
