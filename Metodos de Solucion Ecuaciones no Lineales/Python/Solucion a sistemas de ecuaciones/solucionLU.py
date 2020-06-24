from math import *
from pprint import pprint

def lu(A):
    n=len(A)
    #Creación de matrices nulas
    L=[[0.0 for x in range(n)] for x in range(n)]
    U=[[0.0 for x in range(n)] for x in range(n)]
    