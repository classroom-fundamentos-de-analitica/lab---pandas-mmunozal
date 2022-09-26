"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    
    total_rows=len(tbl0.axes[0]) 
    return total_rows


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    total_cols=len(tbl0.axes[1])
    return total_cols


def pregunta_03():
  a=tbl0.iloc[:, 1]
  listaA=0
  listaB=0
  listaC=0
  listaD=0
  listaE=0
  for i in a:
    if i=='A':
      listaA= listaA + 1
    elif i=='B':
      listaB= listaB + 1
    elif i=='C':
      listaC= listaC + 1
    elif i=='D':
      listaD= listaD + 1
    else:
      listaE= listaE + 1
  ayuda={"A" : listaA,"B":listaB,"C":listaC,"D":listaD,"E":listaE}
  ayuda1 = pd.Series(ayuda)
  return ayuda1


def pregunta_04():
  return tbl0.groupby('_c1')['_c2'].mean()


def pregunta_05():
  a=tbl0.iloc[:, 1]
  b=tbl0.iloc[:, 2]
  listaA=[]
  listaB=[]
  listaC=[]
  listaD=[]
  listaE=[]
  for tupla in zip(a, b): #obtenemos la tupla en cada iteración
    if tupla[0]=="A":
      listaA.append(tupla[1])
    elif tupla[0]=="B":
      listaB.append(tupla[1])
    elif tupla[0]=="C":
      listaC.append(tupla[1])
    elif tupla[0]=="D":
      listaD.append(tupla[1])
    else:
      listaE.append(tupla[1])
  ayuda={"A":max(listaA),"B":max(listaB),"C":max(listaC),"D":max(listaD),"E":max(listaE)}
  ayuda1 = pd.Series(ayuda)
  return ayuda1


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    unicos=((tbl1['_c4'])).unique()
    mayus=[x.upper() for x in unicos]
    ordenar=sorted(mayus)
    return ordenar


def pregunta_07():
  a=tbl0.iloc[:, 1]
  b=tbl0.iloc[:, 2]
  listaA=[]
  listaB=[]
  listaC=[]
  listaD=[]
  listaE=[]
  for tupla in zip(a, b): #obtenemos la tupla en cada iteración
    if tupla[0]=="A":
      listaA.append(tupla[1])
    elif tupla[0]=="B":
      listaB.append(tupla[1])
    elif tupla[0]=="C":
      listaC.append(tupla[1])
    elif tupla[0]=="D":
      listaD.append(tupla[1])
    else:
      listaE.append(tupla[1])
  ayuda= {"A":sum(listaA),"B":sum(listaB),"C":sum(listaC),"D":sum(listaD),"E":sum(listaE)}
  ayuda1 = pd.Series(ayuda)
  return ayuda1
pregunta_07()


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    a=tbl0.iloc[:, 0]
    b=tbl0.iloc[:, 2]
    suma=[]
    for i in range(len(tbl0)):
      ayuda=a[i]
      ayuda1=b[i]
      sumar=int(ayuda+ayuda1)
      suma.append(sumar)
    tbl0["suma"]=suma
    return tbl0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    tbl0["year"] = tbl0['_c3'].map(lambda año: año[:4])
    return tbl0


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    tbl0['_c2'] = tbl0['_c2'].map(str)
    tabla = tbl0.pivot_table(values="_c2",index="_c1",aggfunc=sorted)
    tabla['_c2'] = tabla['_c2'].map(":".join)
    tabla.index.names = ['_c0']
    return tabla


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    tabla = tbl1.pivot_table(values="_c4",index="_c0",aggfunc=sorted)
    tabla['_c4'] = tabla['_c4'].map(",".join)
    tabla = tabla.reset_index()
    return tabla


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    tbl2['_c5b'] = tbl2['_c5b'].map(str)
    tbl2['_c5'] = tbl2['_c5a'] + ":" + tbl2['_c5b']
    tabla = tbl2.pivot_table(values="_c5",index="_c0",aggfunc=sorted)
    tabla['_c5'] = tabla['_c5'].map(",".join)
    tabla = tabla.reset_index()
    return tabla



def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    nuevaTabla = pd.merge(tbl2,tbl0,on="_c0")
    return nuevaTabla.groupby('_c1')['_c5b'].sum()
