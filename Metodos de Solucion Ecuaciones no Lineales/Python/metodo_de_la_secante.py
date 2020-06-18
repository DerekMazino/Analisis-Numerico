def van_der_walls(x):
    valor=round(5*x**3-29.169*x**2+0.245*x-0.0652,5)
    print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def van_der_walls1(x):
    valor=round((5+0.245/x**2)*(x-0.0266)-28.721,5)
    print('f('+str(round(x,5))+')={:.5f}'.format(valor))
    return valor
def secante(f, p0, p1, tol, n): #Metodo de la secante
    i=2
    while i<=n:
        p=p1-(f(p1)*(p1-p0)/(f(p1)-f(p0)))
        print("Iter = ","%03d" % i, "; p = ", "%.5f" % p)
        errorRelativo=round(abs(p-p1),5)
        print('Errror relativo es: ')
        print(errorRelativo)
        if errorRelativo<tol:
            return p
        p0=p1
        p1=p
        i+=1
    print('Iteraciones agotadas. error')
    return
print('Respuesta es!: \n')
secante(van_der_walls1, 35, 30, 1e-5, 11)
