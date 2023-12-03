import re

red = 12
green = 13
blue = 14


def run_part1():
    sum = 0
    with open("input/day2.input", "r") as filin:
        words = filin.read()
        list_game = words.split("\n")
        for game in list_game:
            nextgame = False
            for word in game.split(":"):
                if re.search("Game", word):
                    numgame = int(word.split(" ")[1])
                else:
                    for color in word.split(";"):
                        for numCube in color.split(','):
                            if re.search('red', numCube):
                                if int(numCube.split(" ")[1]) > red:
                                    nextgame = True
                                    break
                            if re.search('green', numCube):
                                if int(numCube.split(" ")[1]) > green:
                                    nextgame = True
                                    break
                            if re.search('blue', numCube):
                                if int(numCube.split(" ")[1]) > blue:
                                    nextgame = True
                                    break
                    if nextgame:
                        break
                    else:
                        sum += numgame
        print('result part 1 : ' + str(sum))


def run_part2():
    sum = 0
    with open("input/day2.input", "r") as filin:
        words = filin.read()
        list_game = words.split("\n")
        for game in list_game:
            max_red = 0
            max_green = 0
            max_blue = 0
            total_game = 0
            for word in game.split(":"):
                if re.search("Game", word):
                    continue
                else:
                    for color in word.split(";"):
                        for numCube in color.split(','):
                            if re.search('red', numCube):
                                red_cube = int(numCube.split(" ")[1])
                                if red_cube > max_red:
                                    max_red = red_cube
                            if re.search('green', numCube):
                                green_cube = int(numCube.split(" ")[1])
                                if green_cube > max_green:
                                    max_green = green_cube
                            if re.search('blue', numCube):
                                blue_cube = int(numCube.split(" ")[1])
                                if blue_cube > max_blue:
                                    max_blue = blue_cube
                    total_game = max_red * max_green * max_blue
                sum += total_game
        print('result part 2 : ' + str(sum))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_part1()
    run_part2()
