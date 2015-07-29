# coding:utf-8
import math
def is_prime(num):
    if num%2!=0:
        for i in range(2,int(math.sqrt(num))):
            if num%i==0:
                # print i  打印出第一个
                return False
        return True
    return False

prime_set=[2]

def set_prime(start,end):
    flag=True
    for num in range(start,end+1):
        for smaller_prime in prime_set:
            if num%smaller_prime ==0:
                flag=False
                continue
        if flag:
            prime_set.append(num)
            print prime_set
    print "prime_set:",prime_set
    return prime_set

def get_prime(num):
    primes=[]
    def pick_prime(num,start=2):
        assert num>=2,'the number must bigger than 2 '
        if num==start:
            primes.append(num)
        else:
            pick_prime(num,int(math.sqrt(num)))
            pick_prime(int(math.sqrt(num)))

    '''
    if num<2:
        return None
    elif num==2:
        prime_set.append(2)
        return "prime_set:",prime_set
    else:
        start=int(math.sqrt(num))
        end=num
        get_prime(end,start):
            set_prime(start,end)
        # FIXME ,怎样把 start 和 end 递归？ 我忘记了
    '''




def test():
    print is_prime(98)
    print is_prime(7)
    print is_prime(1937)
    # set_prime(1,100)
    set_prime(2,2)

if __name__=='__main__':
    test()