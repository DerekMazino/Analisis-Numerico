from math import *
def pol(x):
    valor=round(x**3-3*x-2,5)
    print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def polprima(x):
    valor=round(3*x**2-3,5)
    print('fp('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def punto3(x):
    valor=round(1000*exp(x)+(435*(exp(x)-1))/x-1564,5)
    print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def punto3prima(x):
    valor=round(1000*exp(x)+435*((x*exp(x)-exp(x)+1)/x**2),5)
    print('fp('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor

def pol1(x):
    valor=round(x**2-x-3,5)
    print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def pol1prima(x):
    valor=round(2*x-1,5)
    print('fp('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor

def newton(f, fprima, p0, tol, n):
    i=1
    while i<=n:
        p=p0-f(p0)/fprima(p0)#Aplicando la formula
        print("Iter = ", "%03d" % i, "; p = ", "%.5f" % p)
        errorRelativo=round(abs(p-p0),5)
        print('Errror relativo es: ')
        print(errorRelativo)
        if errorRelativo<tol:
            return p
        p0=p
        i+=1
    print('Iteraciones acotadas: Error')
    return
#print('Respusta es: \n')
#newton(pol, polprima, 2.1, 10e-4, 7)
print('Resopuesta punto 3 Nuevo\n')
newton(punto3, punto3prima, 0.5, 10e-6, 11)
#print('Resopuesta punto 3222 \n')
#newton(pol1, pol1prima, 1.6, 10e-6, 11)     
