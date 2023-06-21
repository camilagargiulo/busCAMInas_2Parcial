import sqlite3
from BM_celda import Celda
from BM_constantes import *

def crear_lista_celdas():
    lista = []
    for columna in range(CANTIDAD_X):
        for fila in range(CANTIDAD_Y):
            celda = Celda(columna, fila)
            lista.append(celda)
    return lista

def cambiar_flag(flag):
    if flag:
        flag = False
        print("bandera no")
    else:
        flag = True
        print("bandera si")
    return flag

def crear_tabla_ranking(path): #"2do Parcial/Limpio/BM_ranking.db" 
    with sqlite3.connect(path) as conexion:
        try:
            sentencia = ''' create table ranking
            (
            id integer primary key autoincrement,
            nombre text,
            score integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla ranking")    

        except sqlite3.OperationalError:
            print("La tabla ranking ya existe")

def devolver_lista_ranking(path):
    with sqlite3.connect(path) as conexion:
        cursor = conexion.execute("SELECT * FROM ranking ORDER BY score ASC")
        lista_ranking = [{"ID": 0, "nombre": "NOMBRE", "score": "TIEMPO"}]
        for fila in cursor:
            dict_jugador = {}
            dict_jugador["id"] = fila[0]
            dict_jugador["nombre"] = fila[1]
            dict_jugador["score"] = fila[2]
            lista_ranking.append(dict_jugador)
        return lista_ranking[0:10]


def guardar_score(path, ingreso, tiempo):
    nombre = ingreso
    score = tiempo
    with sqlite3.connect(path) as conexion:
            try:
                conexion.execute("INSERT INTO ranking(nombre,score) VALUES (?,?)", (nombre, score))
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")


