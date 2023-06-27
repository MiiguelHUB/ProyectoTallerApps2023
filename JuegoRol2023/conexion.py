from debug.log_control import log
import mysql.connector.pooling
import sys


class Conexion:
    _DATABASE = 'taller2023'
    _USERNAME = 'root'
    _PASSWORD = ''
    _DB_PORT = '3306'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name="my_pool",
                    pool_size=cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Creacion de pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_connection()
        log.debug(f'Conexion obtenida desde el pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        conexion.close()
        log.debug(f'Regresando la conexion al pool: {conexion}')

    
if __name__ == '__main__':
    # Obtener una conexión desde el pool
    conexion1 = Conexion.obtenerConexion()
    
    # Liberar la conexión y devolverla al pool
    Conexion.liberarConexion(conexion1) # Toma como argumento "conexion" de donde se genero la conexion y aplica el metodo para cerrarla
    
    
    
    
