import sqlite3

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = sqlite3.connect("bd_usuario.db")
            print("Conexion esta  Correcta :")
            return conexion
        except sqlite3.Error as error:
            print("Error en la base de Datos :"+ error)
            return None

CConexion.ConexionBaseDeDatos()
