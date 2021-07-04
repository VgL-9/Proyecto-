import matplotlib.pyplot as plt
from numpy import mod

def listaComunasUsuario():
    with open("Datos\Datos.csv","r",encoding="utf-8") as f:
        comunasListadoUsuario= []
        for i in f.readlines():
            linea = i.split(",")
            if linea[2] != "Comuna" and len(linea[9])>0:
                comunaFormato = linea[2] + "(" + linea[3] + ")"
                comunasListadoUsuario.append(comunaFormato)
    menuComunas = str(comunasListadoUsuario)
    menuComunas = menuComunas.replace("'","").replace("[","").replace("]","")
    print(menuComunas)

def listaComunasValidacion():
    with open("Datos.csv","r",encoding="utf-8") as f:
        listaParaValidacionComunas = []
        for i in f.readlines():
            linea = i.split(",")
            if linea[2] != "Comuna" and len(linea[3])>0:
                listaParaValidacionComunas.append(linea[2])
                listaParaValidacionComunas.append(linea[3])
    return listaParaValidacionComunas