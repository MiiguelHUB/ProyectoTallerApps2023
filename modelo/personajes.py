class Personaje:
    def __init__(self, personaje_id, personaje_nombre, personaje_nivel, raza_id, estado_id, equipamiento_id, \
    usuario_id):
        self.personaje_id=personaje_id
        self.personaje_nombre=personaje_nombre
        self.personaje_nivel=personaje_nivel
        self.raza_id=raza_id
        self.estado_id=estado_id
        self.equipamiento_id=equipamiento_id
        self.usuario_id=usuario_id

    def __str___(self):
        return """
        Personaje ID: {}
        Nombre personaje: {}
        Nivel: {}
        raza ID: {}
        Estado ID: {}
        Equipamiento ID: {}
        usuario ID: {}""".format(self.personaje_id, self.personaje_nombre, self.personaje_nivel, self.raza_id, \
        self.estado_id, self.equipamiento_id, self.usuario_id)
    
class Estado:
    def __init__(self, estado_id, estado_nombre):
        self.estado_id=estado_id
        self.estado_nombre=estado_nombre
        
    def __str__(self):
        return """" 
        Estado ID: {} 
        Estado nombre: {}""".format(self.estado_id, self.estado_nombre)
    
class Equipamiento:
    def __init__(self, equipamiento_id, equipamiento_nombre):
        self.equipamiento_id=equipamiento_id
        self.equipamiento_nombre=equipamiento_nombre
        
    def __str__(self):
        return """" 
        Equipamiento ID: {} 
        Equipamiento nombre: {}""".format(self.equipamiento_id, self.equipamiento_nombre)
  
"""llorar=Conex('localhost', 'root', 'python_db', 3306)
cursor=llorar.getConex().cursor()
cursor.execute("SELECT * FROM Doctor")

for registro in cursor:
    print(registro)"""


    

