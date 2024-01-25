#Paso1: Importal el paquetes o paquetes con los que voy analizar la informacion
import pandas as pd
from helpers.creacionTabla import crearTabla
#paso2: Sin importar la fuente (sql, xls, JSON, csv...)
#Crear una tabla tabulada que se llama dataframe
#Dataframe= Tabla con filas y columnas con toda la informacion sin importar cual va a ser la fuente
#columnas=atributos
#filas=valores


def analizarCanastaBasica():
    tabla=pd.read_csv("./data/bdcanasta.csv")   
    #print(tabla)
    crearTabla(tabla, "canastabasica")

#3. aplico filtros para limpiar y seleccionar datos
    #Mostrar los 5 primeros datos
    #print(tabla.head(20)) #Primeros n registros

    #Acceder a los ultimos registros de la tabla
    #print(tabla.tail())

    #Informacion basica 1cuantos datos, media, estandar, minimo, cuartibles o persetible:como se distribuye la informacion en franjas
    
    #print(tabla.describe())
    




