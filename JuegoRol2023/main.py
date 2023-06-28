import getpass
import time
from modelo import *
from usuarioDAO import *


def MenuLogin():

    login_menu = '''


    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //                                                                                                                   //
    //   ______   __   __  __    _  _______  _______  _______  __    _    __   __  _______  ___   _  _______  ______     //
    //  |      | |  | |  ||  |  | ||       ||       ||       ||  |  | |  |  |_|  ||   _   ||   | | ||       ||    _ |    //
    //  | | |   ||  |_|  ||       ||   | __ |   |___ |  | |  ||       |  |       ||       ||      _||   |___ |   |_||_   //
    //  | |_|   ||       ||  _    ||   ||  ||    ___||  |_|  ||  _    |  |       ||       ||     |_ |    ___||    __  |  //
    //  |       ||       || | |   ||   |_| ||   |___ |       || | |   |  | ||_|| ||   _   ||    _  ||   |___ |   |  | |  //
    //  |______| |_______||_|  |__||_______||_______||_______||_|  |__|  |_|   |_||__| |__||___| |_||_______||___|  |_|  //
    //                                                                                                                   //
    //                                                                                                                   //
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //                                                                                                                   //
    //                                                                                                                   //
    //                                                                                                                   //
    //                  ____ _ ____ _  _    _  _ ___                       _    ____ ____ _ _  _                         // 
    //                  [__  | | __ |\ |    |  | |__]                      |    |  | | __ | |\ |                         //
    //                  ___] | |__] | \|    |__| |                         |___ |__| |__] | | \|                         // 
    //                                                                                                                   //
    //                         Presiona 1                                         Presiona 2                             //
    //                                                                                                                   //
    //                                                  Exit Presiona 0                                                  //
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                                                                           
                                                                            
    '''

    for linea in login_menu.splitlines():
            print(linea)
            time.sleep(0.1)
            
class Menu:
    @staticmethod
    def mostrar_menu_principal():
        MenuLogin()
        while True:
            opcion = input("")

            if opcion == "1":
                Menu.crear_usuario()
            elif opcion == "2":
                Menu.iniciar_sesion() # Crear este metodo
            elif opcion == "3":
                print("Saliendo...")
                break
            else:
                print("Opcion invalida")

    @staticmethod
    def crear_usuario():
        while True:
            nombre = input("Ingrese el nombre de usuario: ")
            contrasena = getpass.getpass("Ingrese la contraseña: \n(No se mostrara en pantalla) ")
            contrasena_rep = getpass.getpass("Confirme su contraseña: \n(No se mostrara en pantalla) ")
            
            if contrasena == contrasena_rep: # Verificamos si ambas contraseñas son iguales

                # Crear el usuario con los datos proporcionados
                Usuario.insertar_usuario(nombre,contrasena, gm_usuario=False)

                print(f"Usuario {nombre} creado con exito")
                break
            else:
                print("Las contraseñas no son iguales")
    
    
    ''' De aca hacia abajo no revise       
    @staticmethod
    def crear_personaje(Usuario):
        nombre = input("Ingrese el nombre del personaje: ")
        raza_id = input("Ingrese el ID de la raza: ")
        estado_id = 1  # Vivo por defecto
        equipamiento_id = input("Ingrese el ID del equipamiento: ")

        # Crear el personaje con los datos proporcionados
        personaje = Usuario.crear_personaje(nombre, raza_id, estado_id, equipamiento_id)

        print("Personaje creado con exito")
        print("Resumen del personaje:")
        print(personaje)

        '''


         

    
    
    
    
    
    

if __name__ == "__main__":
    Menu.mostrar_menu_principal()
      