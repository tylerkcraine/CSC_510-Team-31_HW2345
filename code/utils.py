# all util functions 

import math


def per(t,p):
    p = math.floor( ( (p or .5) * len(t)) + .5 )
    return t[max(1,min(len(t),p))]

# optional, we can just use round() function instead.
def rnd(x, places):
    mult = 10 ** (places or 2)
    return math.floor(x * mult + 0.5)/ mult

if __name__=="__main__":
    print (rnd(1.23445,2))




