def ecX(z, y):
    return (12+y-z)/15
def ecY(x, z):
    return (11+z-2*x)/8
def ecZ(x, y):
    return (3+x-y)/4

def jabobi(xf,yf,zf, p01,p02,p03, iter):
    p1=p01
    p2=p02
    p3=p03
    for i in range(iter):
        x=xf(p3,p2)
        y=yf(p1,p3)
        z=zf(p1,p2)
        print('iter = '+str(i)+'; x={:.5f}; y={:.5f}; z={:.5f}'.format(x,y,z))
        p1=x
        p2=y
        p3=z
jabobi(ecX, ecY, ecZ, 0, 0 ,0, 6)

    