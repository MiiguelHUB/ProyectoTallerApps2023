class User:
    def __init__(self, usuario_id, usuario_nombre, contrasena, gm_usuario):
        self.usuario_id= usuario_id
        self.usuario_nombre = usuario_nombre
        self.__contrasena = contrasena 
        self.gm_usuario = gm_usuario

    def __str__(self):
        return """
        ID Usuario: {}
        Nombre: {}
        ¿GM o usuario?: {}""".format(self.usuario_id, self.usuario_nombre, self.gm_usuario)

    def getPassword(self): 
        return self.__contrasena

"""caro=User('Carola', 'carolina@hotmail.com', 123, )
print(caro)""" 
#No muestra la password



