# coding:utf-8

def stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n - 1) + stairs(2)


def get_money(m):
    if m == 1:
        return 1
    if m == 2:
        return 2
        # return m/2+1
    if m == 5:
        return 4
        # retrum m/5+m/2+1
    if m == 10:
        return 11
        # return m/10+(m/5-1)*money(5)+m/2+1
    if m == 20:
        return 28
        # return m/20+(m/10-1)*money(10)+(m-5)……


def div_money(money):
    value = [1, 2, 5, 10, 20, 100]
    mod = [0, 0, 0, 0, 0, 0]
    my_count = 0
    for n in range(len(value)):
        mod[n] = money / value[n]
    for a in range(money / 1 + 1):
        for b in range((money - a * 1) / 2 + 1):
            for c in range(money / 5 + 1):
                for d in range(money / 10 + 1):
                    for e in range(money / 20 + 1):
                        for f in range(money / 50 + 1):
                            for g in range(money / 100 + 1):
                                if money is a * 1 + b * 2 + c + 5 + d * 10 + e * 20 + f * 50 + g * 100:
                                    my_count += 1
                                    print a * 1 + b * 2 + c + 5 + d * 10 + e * 20 + f * 50 + g * 100
                                    print "%d = %d*100 + %d*50 + %d*20 + %d*10 + %d*5 + %d*2 + %d *1." % (
                                        money, g, f, e, d, c, b, a)
                                else:
                                    continue

    print "my_count : ", my_count


def if_sum(n, n1, n2):
    if n < min(n1, n2):
        print "%d = ? * %d + ? * %d  " % (n, n1, n2)
        return False
    else:
        a1 = n / n1
        for i in range(a1 + 1):
            if (n - n1 * a1) % n2 == 0:
                a2 = (n - n1 * a1) / n2
                print "%d = %d * %d + %d * %d " % (n, n1, a1, n2, a2)
                return True
        print "%d = ? * %d + ? * %d  " % (n, n1, n2)
        return False


def test_Sum():
    print if_sum(10, 2, 5)
    print if_sum(7, 3, 5)
    print if_sum(9, 7, 2)
    print if_sum(122, 324, 45)


def show(n):
    print '%d 个阶梯，%d 种走法' % (n, stairs(n))


def test():
    show(1)
    show(2)
    show(3)
    show(4)
    show(5)
    show(10)


def test_money():
    div_money(10)
    div_money(8)
    div_money(1)
    div_money(2)
    div_money(5)
    div_money(10)
    div_money(20)
    div_money(50)
    div_money(23)
    # div_money(100)


if __name__ == "__main__":
    # test()
    test_money()
    # test_Sum()