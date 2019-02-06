import numpy as np
from io import StringIO

pfile=open('arreglo','r')
data=pfile.read()
pfile.close()
data=np.genfromtxt(StringIO(data), delimiter  = ',' )

x= list(data.shape)
filas=x[0]
columnas=x[1]
sup=0
izq=0
der=columnas
inf=filas
numeros=[]

print(data)
print(filas)
print(columnas)

while sup < inf or izq < der :
    i=inf-1
    j=der-1

    while j>izq:
        numeros.append(data[i][j])
        j=j-1
    while i>sup:
        numeros.append(data[i][j])
        i=i-1
    while j<der-1:
        numeros.append(data[i][j])
        j=j+1
    while i<inf-1:
        numeros.append(data[i][j])
        i=i+1

    izq=izq+1
    sup=sup+1
    der=der-1
    inf=inf-1

print(numeros)
