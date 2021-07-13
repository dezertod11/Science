import math


def x(fi):
    return math.atanh(fi)
def bin_search(fi_u, fi_d , x_i):
    u = fi_u
    d = fi_d
    # x_r = x(u)
    # x_l = x(d)
    fi_s = (u + d) / 2
    x_s = x(fi_s)
    while abs(x_s - x_i) > 0.05:
        fi_s = (u + d)/2
        x_s = x(fi_s)
        # print(x_s, fi_s )
        if x_s < x_i:
            # x_l = x_s
            d = fi_s
            print(x_s, fi_s, 1)
        else:
            # x_r = x_s
            u = fi_s
            print(x_s, fi_s,2)
    return fi_s

print(bin_search(fi_u = 0.999999, fi_d=-0.999999 , x_i=-5))