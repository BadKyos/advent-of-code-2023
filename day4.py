def run_part1():
    total = 0
    with (open("input/day4.input", "r") as filin):
        file = filin.read().splitlines()

        for line in file:
            score = 0
            card = line.split(":")[1].split("|")[0]
            result = line.split(":")[1].split("|")[1].split(' ')
            for jeu in list(filter(None, card.split(" "))):
                if jeu in result:

                    if score == 0:
                        score = 1
                    else:
                        score = score * 2

            total += score
        print("total : " + str(total))


def run_part2():
    total = 0
    with (open("input/day4.input", "r") as filin):
        file = filin.read().splitlines()
        list_card = {}
        for line in file:
            score = 0
            k = 1
            line = line.strip()
            card = line.split(":")[1].split("|")[0]
            result = line.split(":")[1].split("|")[1].split(' ')

            card_num = int(line.split(":")[0].replace('Card','').strip())
            if card_num in list_card.keys():
                list_card.update({card_num: list_card[card_num] + 1})
            else:
                list_card.update({card_num: 1})
            for jeu in list(filter(None, card.split(" "))):
                if jeu in result:
                    score += 1

            while k <= list_card[card_num]:
                k += 1
                i = 0
                while i < score:
                    i += 1
                    card_plus = card_num + i
                    if card_plus in list_card.keys():
                        list_card.update({card_plus: list_card[card_plus] + 1})
                    else:
                        list_card.update({card_plus: 1})

        total += sum(list_card.values())
        print("total : " + str(total))


if __name__ == '__main__':
    run_part1()
    run_part2()
