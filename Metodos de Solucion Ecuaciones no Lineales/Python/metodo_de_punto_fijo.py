def pol(x):
    valor=(x**2-8*x+25)/3
    #print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def puntofijo(f, p0, tol, n):
    i = 1
    while i <=n:
        p=f(p0)
        print("Iter = ", "%03d" % i, "; p = ", "%.5f" % p)
        if abs(p-p0) < tol:
            return 
        p0=p
        i+=1
    print('Iteraciones agotadas, error')
    return
print("Resultado 1: \n")
puntofijo(pol, 3.15, 10e-10, 100)
print("Resultado 2: \n")
puntofijo(pol, 3.25, 10e-10, 100)