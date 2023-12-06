def run_part1():
    sum = 0
    with open("input/day6.input", "r") as filin:
        file = filin.read().splitlines()
        time_list = list(filter(len, file[0].replace(" ", "").split(":")[1].split(" ")))
        len_list = list(filter(len, file[1].replace(" ", "").split(":")[1].split(" ")))

        print(time_list)
        print(len_list)
        i = 0
        result = 1
        while i < len(time_list):
            v = 0
            ways = 0
            time = int(time_list[i])
            dist = int(len_list[i])
            while time > 0:
                if time * v > dist:
                    ways += 1
                time-=1
                v+=1
            result *= ways
            i+=1
        print(result)

def run_part2():
    sum = 0


if __name__ == '__main__':
    run_part1()
    run_part2()
