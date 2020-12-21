import itertools
import sys
from functools import reduce
from operator import mul
from math import gcd

from tqdm import tqdm

if __name__ == '__main__':

    def find_gcd(x, y):

        while (y):
            x, y = y, x % y

        return x



    ip="939\n7,13,x,x,59,x,31,19".split()
    ip=sys.stdin.read().split()
    ts=int(ip[0])
    print(ip)
    ids={i: int(k) for i, k in enumerate(ip[1].split(',')) if k.isnumeric()}
    print(ids)

    q = sorted(ids.items(), key=lambda k: -k[1])
    print(q[0])
    s = ids[0]
    # qs = 100000000000000
    # print([k*(qs//k) for j, k in ids.items()])

    print(reduce(mul, list(ids.values())[0:-1], 1))
    # ids=list(ids.items())[1:]
    print([(k, j, (1068781 + j)//k) for j, k in q])
    #
    # print((q[1]*5+q[0])%q[1])
    # 100000000000000
    #     52910000000
    o = ids.values()
    num1 = o[0]
    num2 = o[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(o)):
        gcd = find_gcd(gcd, o[i])
    print(gcd)
    exit()
    for i in itertools.count(start=s, step=s):
        f=True
        for j, k in ids:
            if (k-i) % k != j:
                f = False
                break

        if i % (s*10000000) == 0:
            print('step', i)

        if f:
            print(i)
            break

    exit(0)
    a=1068781
    ##1068781

    for j, k in list(ids.items())[1:]:
        print(k, k-a%k, j)
        if k-a%k != j:
            print('fail')
