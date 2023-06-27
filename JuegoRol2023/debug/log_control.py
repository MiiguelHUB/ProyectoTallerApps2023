import logging as log
import os

log_folder = os.path.join('JuegoRol2023', 'log')  # Nombre de la carpeta de logs

# Crear la carpeta de logs si no existe
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_file = os.path.join(log_folder, 'debug.log')  # Ruta completa del archivo de logs


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler(log_file), # Pasamos la variable con la ruta como argumento
                    log.StreamHandler()
                ])


if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de critico')
    log.critical('Mensaje a nivel de critico')
