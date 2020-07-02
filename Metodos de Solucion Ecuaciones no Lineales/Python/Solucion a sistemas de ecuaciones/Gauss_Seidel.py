def ecX(z, y):
    return (11+z-8*y)/2
def ecY(x, z):
    return (5*x+z-10)/12
def ecZ(x, y):
    return (3+x-y)/14

def gaussSidel(xf,yf,zf, p01,p02,p03, iter):
    #p1=p01
    p2=p02
    p3=p03
    for i in range(iter):
        x=xf(p3,p2)
        y=yf(x,p3)
        z=zf(x,y)
        print('iter = '+str(i)+'; x={:.5f}; y={:.5f}; z={:.5f}'.format(x,y,z))
        #p1=x
        p2=y
        p3=z
gaussSidel(ecX, ecY, ecZ, 0, 0 ,0, 6)

    