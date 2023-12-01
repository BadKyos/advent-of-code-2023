import re


d = {'one':'on1e', 'two':'tw2o', 'three':'thre3e',
     'four':'fou4r', 'five':'fiv5e', 'six':'si6x',
     'seven':'seve7n', 'eight':'eigh8t', 'nine':'nin9e'}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum = 0
    with open("input/day1.input", "r") as filin:
        words = filin.read()
        for word in words.split('\n'):
            for k, v in d.items():
                word = word.replace(k, str(v))
            numList = re.findall('[0-9]{1}', word)
            word_num = numList[0]+''+numList[len(numList)-1]

            sum += int(word_num)

    print(sum)
