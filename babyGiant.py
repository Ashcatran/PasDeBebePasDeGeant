# coding: utf8
#!/usr/bin/env python3

import math

# algo from http://defeo.lu/in420/Pas%20de%20b%C3%A9b%C3%A9%20et%20pas%20de%20g%C3%A9ant

def modPow(x, e, n):
    result = 1
    while e > 0:
        if e & 1:
            result = (result * x) % n
        e >>= 1
        x = x * x % n
    return result

if __name__ == '__main__':
    p = 97 #prime number, defines group Z/nZ
    g = 17
    a = 3 # we are looking for 0<=x < p-1 such as a = g**x mod p
    m = math.ceil(math.sqrt(p))
    babySteps = {} # dicts in python have a search complexity of O(1)

    for i in range(0, m):
        babySteps[i] = modPow(g, i, p)
    i = 0

    for num in babySteps:
        print(num, babySteps[num])

    #while babySteps.get(modPow(a, i*m, p), True):
    #    pass
    print(i)

