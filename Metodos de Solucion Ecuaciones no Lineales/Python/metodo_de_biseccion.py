from math import *

def pol1(x):
    valor=-x**3+45*x**2-8663
    #print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor

def biseccion(f, a, b, tol, n):
    i=1
    while i<=n:
        print('a=:{:.14f}'.format(a))
        print('b=:{:.14f}'.format(b))
        print('fa=({:.14f}'.format(a)+")={:.5f}".format(f(a)))
        print('fb=({:.14f}'.format(b)+")={:.5f}".format(f(b)))
        p=a+(b-a)/2.0
        print('fc=({:.14f}'.format(p)+")={:.5f}".format(f(p)))
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

biseccion(pol1, 17.6, 18, 1e-3, 50)