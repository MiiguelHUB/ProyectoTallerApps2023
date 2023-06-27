import mysql.connector
from debug.log_control import log 
from conexion import Conexion
from modelo import *

class Usuario:
    @classmethod
    def insertar_usuario(cls, nombre, contrasena, gm_usuario):
        try:
            connection = Conexion.obtenerConexion()
            cursor = connection.cursor()

            sql = "INSERT INTO usuarios (usuario_nombre, contrasena, GM_usuario) VALUES (%s, %s, %s)"
            values = (nombre, contrasena, gm_usuario)
            cursor.execute(sql, values)

            connection.commit()
            cursor.close()
            Conexion.liberarConexion(connection)
            print("Usuario insertado correctamente.")

        except mysql.connector.Error as error:
            print(f"Error al insertar el usuario: {error}")
            
    ''' Metodo exclusivo del GM

    @classmethod
    def obtener_usuarios(cls):
        try:
            connection = Conexion.obtenerConexion()
            cursor = connection.cursor()

            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)

            usuarios = cursor.fetchall()

            cursor.close()
            Conexion.liberarConexion(connection)

            return usuarios

        except mysql.connector.Error as error:
            print(f"Error al obtener los usuarios: {error}")
    
    '''
            
    @classmethod
    def crear_personaje(cls, nombre, raza_id, estado_id, equipamiento_id, usuario_id):
        try:
            connection = Conexion.obtenerConexion()
            cursor = connection.cursor()

            sql = "INSERT INTO personajes (personaje_nombre, personaje_nivel, raza_id, estado_id, equipamiento_id, usuario_id) " \
                "VALUES (%s, 1, %s, %s, %s, %s)"
            values = (nombre, raza_id, estado_id, equipamiento_id, usuario_id)
            cursor.execute(sql, values)

            personaje_id = cursor.lastrowid

            connection.commit()
            cursor.close()
            Conexion.liberarConexion(connection)

            # Crear y devolver el objeto Personaje
            nuevo_personaje = cls()

            # Comprobar si el personaje se creó correctamente
            if personaje_id:
                print("Personaje creado exitosamente:")
                print(nuevo_personaje)
            else:
                print("Error al crear el personaje.")

            return nuevo_personaje

        except mysql.connector.Error as error:
            print(f"Error al crear el personaje: {error}")

            
    
    @classmethod
    def listar_personajes_usuario(cls, usuario_id):
        try:
            connection = Conexion.obtenerConexion()
            cursor = connection.cursor()

            sql = "SELECT * FROM personajes WHERE usuario_id = %s"
            values = (usuario_id,)
            cursor.execute(sql, values)

            personajes = []
            for row in cursor.fetchall():
                personaje_id = row[0]
                personaje_nombre = row[1]
                personaje_nivel = row[2]
                raza_id = row[3]
                estado_id = row[4]
                equipamiento_id = row[5]
                usuario_id = row[6]

                personaje = Personaje(personaje_id, personaje_nombre, personaje_nivel, raza_id, estado_id, equipamiento_id, usuario_id)
                personajes.append(personaje)

            cursor.close()
            Conexion.liberarConexion(connection)

            return personajes

        except mysql.connector.Error as error:
            print(f"Error al listar los personajes del usuario: {error}")

    
    ''' Desde aca los metodos aun no entran en el primer sprint

    @classmethod
    def actualizar_usuario(cls, usuario_id, nombre, contrasena, gm_usuario):
        try:
            connection = Conexion.obtenerConexion()
            cursor = connection.cursor()

            sql = "UPDATE usuarios SET usuario_nombre = %s, contrasena = %s, GM_usuario = %s WHERE usuario_id = %s"
            values = (nombre, contrasena, gm_usuario, usuario_id)
            cursor.execute(sql, values)

            connection.commit()
            cursor.close()
            Conexion.liberarConexion(connection)
            print("Usuario actualizado correctamente.")

        except mysql.connector.Error as error:
            print(f"Error al actualizar el usuario: {error}")

    @classmethod
    def eliminar_usuario(cls, usuario_id):
        try:
            connection = Conexion.obtenerConexion()
            cursor = connection.cursor()

            sql = "DELETE FROM usuarios WHERE usuario_id = %s"
            values = (usuario_id,)
            cursor.execute(sql, values)

            connection.commit()
            cursor.close()
            Conexion.liberarConexion(connection)
            print("Usuario eliminado correctamente.")

        except mysql.connector.Error as error:
            print(f"Error al eliminar el usuario: {error}")
    '''


if __name__ == '__main__':
    # Ejemplos de uso
    
    # Insertar un nuevo usuario
    Usuario.insertar_usuario("user3", "1234", False)
    
    # Crear un nuevo personaje para el usuario
    personaje = Usuario.crear_personaje("Tulio", 1, 1, 1, 5)  # personaje_nombre, personaje_nivel, raza_id, estado_id, equipamiento_id, usuario_id
    print(personaje)


    # Obtener todos los personajes de un usuario
    personajes_usuario = Usuario.listar_personajes_usuario(5)
    for personaje in personajes_usuario:
        print(personaje)


