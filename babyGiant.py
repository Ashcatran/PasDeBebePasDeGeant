# coding: utf8
#!/usr/bin/env python3

import math
import time

# algo from http://defeo.lu/in420/Pas%20de%20b%C3%A9b%C3%A9%20et%20pas%20de%20g%C3%A9ant

#returns x**e mod n
def modPow(x, e, n):
    result = 1
    while e > 0:
        if e & 1:
            result = (result * x) % n
        e >>= 1
        x = x * x % n
    return result

if __name__ == '__main__':
    p = 101 #prime number, defines group Z/nZ
    g = 2
    a = 48 # we are looking for 0<=x < p-1 such as a = g**x mod p i.e. 57=3**100 mod 113
    m = int(math.ceil(math.sqrt(p)))
   # print('m', m)
    babySteps = {} # dicts in python have a search complexity of O(1)
    print("Computing " + str(m) +" baby steps...")
    for i in range(0, m):
       babySteps[modPow(g, i, p)] = i
    print("Done !")
    i = 0

   # print("===Baby Steps===")
   # for num in babySteps:
   #     print(num, babySteps[num])
    
    r = modPow(g, -m+p-1, p) # g**(-m+p-1)
    print("Computing giant steps...")
    found = False
    while found == False:
        d = a * modPow(r, i, p) % p
       # found = d in babySteps.itervalues()
        found = babySteps.has_key(d)
       # print(i, d)
        i += 1
       # time.sleep(1)
    print("Done !")
    i= i-1
    j=babySteps.get(d)
   # print(i, j)
    res = i*m +j
    print("The result is: " + str(res))



