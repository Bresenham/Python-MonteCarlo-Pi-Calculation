import math
def Halton(base,ix):
    r = 0
    f = 1.0 / base
    i = ix
    while(i > 0):
        r += f * (i%base)
        f /= base
        i = math.floor(i/base)
    return r