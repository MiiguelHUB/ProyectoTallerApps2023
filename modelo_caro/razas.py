class Raza:
    def __init__(self, raza_id, raza_nombre):
        self.raza_id=raza_id
        self.raza_nombre=raza_nombre
        
    def __str__(self):
        return """" 
        Raza ID: {} 
        Raza nombre: {}""".format(self.raza_id, self.raza_nombre)
    
class Habilidad:
    def __init__(self, habilidad_id, habilidad_nombre, habilidad_detalle, raza_id):
        self.habilidad_id=habilidad_id
        self.habilidad_nombre=habilidad_nombre
        self.habilidad_detalle=habilidad_detalle
        self.raza_id=raza_id
        
    def __str__(self):
        return """" 
        Habilidad ID: {} 
        Habilidad nombre: {}
        Habilidad detalle: {}
        Raza ID: {}""".format(self.habilidad_id, self.habilidad_nombre, self.habilidad_detalle, self.raza_id)

class Poder:
    def __init__(self, poder_id, poder_nombre, poder_detalle, raza_id):
        self.poder_id=poder_id
        self.poder_nombre=poder_nombre
        self.poder_detalle=poder_detalle
        self.raza_id=raza_id
        
    def __str__(self):
        return """" 
        Poder ID: {} 
        Poder nombre: {}
        Poder detalle: {}
        Raza ID: {}""".format(self.poder_id, self.poder_nombre, self.poder_detalle, self.raza_id)



