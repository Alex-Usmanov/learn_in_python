# coding:utf-8

def stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n - 1) + stairs(2)


def show(n):
    print '%d 个阶梯，%d 种走法' % (n, stairs(n))


def test():
    show(1)
    show(2)
    show(3)
    show(4)
    show(5)
    show(10)


if __name__ == "__main__":
    test()
n -