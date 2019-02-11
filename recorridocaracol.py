def cargar_archivo(lab):
        return open(lab)

def moverDer(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col])
            moverDer(mat,fil,col+1,aux+1,tam)
        if(aux==tam):
            moverAba(mat,fil+1,col-1,0,tam-1)
    else:
        print("Final")

def moverAba(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col])
            moverAba(mat,fil+1,col,aux+1,tam)
        if(aux==tam):
            moverIzq(mat,fil-1,col-1,0,tam)
    else:
        print("Final")
def moverIzq(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col])
            moverIzq(mat,fil,col-1,aux+1,tam)
        if(aux==tam):
            moverArr(mat,fil-1,col+1,0,tam-1)
    else:
        print("Final")
        
def moverArr(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col])
            moverArr(mat,fil-1,col,aux+1,tam)
        if(aux==tam):
            moverDer(mat,fil+1,col+1,0,tam)
    else:
        print("Final")

def crear_matriz2(mat,lab):
    for x in cargar_archivo(lab):
        mat.append(x.strip().split())
    return mat

def resolver(lab):
    moverDer(crear_matriz2([],lab),0,0,0,len(crear_matriz2([],lab)))
    
          
resolver("arreglo.txt") 
