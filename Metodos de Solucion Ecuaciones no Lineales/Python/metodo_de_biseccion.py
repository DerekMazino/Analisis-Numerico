from math import *

def biseccion(f, a, b, tol, n):
    i=1
    while i<=tol:
        p=a+(b-a)/2.0
        print("Iter = ", "%03d" % i, "; p = ", "%.5f" % p)
        if abs(f(p)) <= 1e-15 or (b-a)/2.0 < tol:
            return p
        i+=1
        if f(a)*f(p) > 0:
            a=p
        else:
            b=p
    print('Iteraciones agotadas, error')
    return
