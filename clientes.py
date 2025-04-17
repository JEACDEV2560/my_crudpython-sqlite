from my_conex import *

class CClientes:
    def mostrarClientes():
        try:
            cone= CConexion.ConexionBaseDeDatos()
            consulta=cone.cursor()
            consulta.execute("SELECT * FROM usuario;")
            miResultado= consulta.fetchall()
            cone.close()
            return miResultado
        except sqlite3.Error as error:
            print("Error al mostrar los Registro de Usuario: ", error)
            
