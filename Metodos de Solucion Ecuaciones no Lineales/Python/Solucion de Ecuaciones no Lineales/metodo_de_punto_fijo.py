def pol(x):
    valor=(x**2-8*x+25)/3
    #print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def pol1(x):
    valor=(11*x**3-141*x**2+556*x-546)/30
    #print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def pol3(x):
    valor=20/(x**2+2*x+10)
    #print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor

def pol4(x):
    valor=(15*x**2-66*x+80)**(1/3)
    #print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor 

def puntofijo(f, p0, tol, n):
    i = 1
    while i <=n:
        p=f(p0)
        print("Iter = ", "%03d" % i, "; p = ", "%.14f" % p)
        if abs(p-p0) < tol:
            return 
        p0=p
        i+=1
    print('Iteraciones agotadas, error')
    return
#print("Resultado 1: \n")
#puntofijo(pol, 3.15, 10e-10, 100)
#print("Resultado 2: \n")
#puntofijo(pol, 3.25, 10e-10, 100)
#print("Resultado 3: \n")
#puntofijo(pol1, 4.1, 10e-10, 100)
#print("Resultado 4: \n")
#puntofijo(pol1, 6.96, 10e-10, 100)
#print("Resultado 5: \n")
puntofijo(pol4, 9, 10e-10, 1000)