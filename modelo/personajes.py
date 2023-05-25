class Personaje:
    def __init__(self, personaje_id, personaje_nombre, personaje_nivel, raza_id, estado_id, equipamiento_id, usuario_id):
        self.personaje_id = personaje_id
        self.personaje_nombre = personaje_nombre
        self.personaje_nivel = personaje_nivel
        self.raza_id = raza_id
        self.estado_id = estado_id
        self.equipamiento_id = equipamiento_id
        self.usuario_id = usuario_id

    def __str__(self):
        return """
        Personaje ID: {}
        Nombre personaje: {}
        Nivel: {}
        Raza ID: {}
        Estado ID: {}
        Equipamiento ID: {}
        Usuario ID: {}""".format(self.personaje_id, self.personaje_nombre, self.personaje_nivel, self.raza_id,
                                self.estado_id, self.equipamiento_id, self.usuario_id)


class Estado:
    def __init__(self, estado_id, estado_nombre):
        self.estado_id = estado_id
        self.estado_nombre = estado_nombre

    def __str__(self):
        return """
        Estado ID: {}
        Estado nombre: {}""".format(self.estado_id, self.estado_nombre)


class Equipamiento:
    def __init__(self, equipamiento_id, equipamiento_nombre):
        self.equipamiento_id = equipamiento_id
        self.equipamiento_nombre = equipamiento_nombre

    def __str__(self):
        return """
        Equipamiento ID: {}
        Equipamiento nombre: {}""".format(self.equipamiento_id, self.equipamiento_nombre)


if __name__ == "__main__":
    # Pruebas de construcción de objetos

    # Crear un objeto de la clase Estado
    estado = Estado(1, "Vivo")
    print(estado)

    # Crear un objeto de la clase Equipamiento
    equipamiento = Equipamiento(1, "Espada")
    print(equipamiento)

    # Crear un objeto de la clase Personaje
    personaje = Personaje(1, "Gandalf", 50, 2, 1, 1, 1)
    print(personaje)



    

