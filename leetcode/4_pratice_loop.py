def playnum(num):
    score = num * (10 ** (num - 1))
    for i in range(1, num):
        score += ((num - i) * (10 ** (2 * i)) + (num - i)) * (10 ** (num - i - 1))
        # print score
    return score


def play2num(num):
    if num > 0:
        if num % 2 == 1:
            return 1 - (num - 1) / 2
        else:
            return 1 - (num - 2) / 2 + num
    else:
        print "Don't joy me "