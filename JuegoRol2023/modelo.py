from debug.log_control import log


# Se crea un entidad base para optimizar los atributos de las clases ya que tanto id como nombre se repiten
# constamente en todos los objetos.

class EntidadBase:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}"


class Usuario(EntidadBase):
    def __init__(self, usuario_id, usuario_nombre, contrasena, gm_usuario):
        super().__init__(usuario_id, usuario_nombre)
        self._contrasena = contrasena
        self._gm_usuario = gm_usuario

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    @property
    def gm_usuario(self):
        return self._gm_usuario

    @gm_usuario.setter
    def gm_usuario(self, gm_usuario):
        self._gm_usuario = gm_usuario

    def __str__(self):
        return f"{super().__str__()}, GM: {self._gm_usuario}"
    

class Raza(EntidadBase):
    def __init__(self, raza_id, raza_nombre):
        super().__init__(raza_id, raza_nombre)


class Equipamiento(EntidadBase):
    def __init__(self, equipamiento_id, equipamiento_nombre):
        super().__init__(equipamiento_id, equipamiento_nombre)


class Habilidad(EntidadBase):
    def __init__(self, habilidad_id, habilidad_nombre, habilidad_detalle, raza_id):
        super().__init__(habilidad_id, habilidad_nombre)
        self._habilidad_detalle = habilidad_detalle
        self._raza_id = raza_id

    @property
    def habilidad_detalle(self):
        return self._habilidad_detalle

    @habilidad_detalle.setter
    def habilidad_detalle(self, habilidad_detalle):
        self._habilidad_detalle = habilidad_detalle

    @property
    def raza_id(self):
        return self._raza_id

    @raza_id.setter
    def raza_id(self, raza_id):
        self._raza_id = raza_id

    def __str__(self):
        return f"{super().__str__()}, Detalle: {self._habilidad_detalle}, Raza ID: {self._raza_id}"


class Poder(EntidadBase):
    def __init__(self, poder_id, poder_nombre, poder_detalle, raza_id):
        super().__init__(poder_id, poder_nombre)
        self._poder_detalle = poder_detalle
        self._raza_id = raza_id

    @property
    def poder_detalle(self):
        return self._poder_detalle

    @poder_detalle.setter
    def poder_detalle(self, poder_detalle):
        self._poder_detalle = poder_detalle

    @property
    def raza_id(self):
        return self._raza_id

    @raza_id.setter
    def raza_id(self, raza_id):
        self._raza_id = raza_id

    def __str__(self):
        return f"{super().__str__()}, Detalle: {self._poder_detalle}, Raza ID: {self._raza_id}"


class Personaje(EntidadBase):
    def __init__(self, personaje_id, personaje_nombre, personaje_nivel, raza_id, estado_id, equipamiento_id, usuario_id):
        super().__init__(personaje_id, personaje_nombre)
        self._personaje_nivel = personaje_nivel
        self._raza_id = raza_id
        self._estado_id = estado_id
        self._equipamiento_id = equipamiento_id
        self._usuario_id = usuario_id

    @property
    def personaje_nivel(self):
        return self._personaje_nivel

    @personaje_nivel.setter
    def personaje_nivel(self, personaje_nivel):
        self._personaje_nivel = personaje_nivel

    @property
    def raza_id(self):
        return self._raza_id

    @raza_id.setter
    def raza_id(self, raza_id):
        self._raza_id = raza_id

    @property
    def estado_id(self):
        return self._estado_id

    @estado_id.setter
    def estado_id(self, estado_id):
        self._estado_id = estado_id

    @property
    def equipamiento_id(self):
        return self._equipamiento_id

    @equipamiento_id.setter
    def equipamiento_id(self, equipamiento_id):
        self._equipamiento_id = equipamiento_id

    @property
    def usuario_id(self):
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self._usuario_id = usuario_id

    def __str__(self):
        return f"{super().__str__()}, Nivel: {self._personaje_nivel}, Raza ID: {self._raza_id}, " \
               f"Estado ID: {self._estado_id}, Equipamiento ID: {self._equipamiento_id}, " \
               f"Usuario ID: {self._usuario_id}"


# Crear objetos y mostrarlos por consola
if __name__ == "__main__":
    
    log.debug("Creando objeto Usuario...")
    usuario = Usuario(1, "Mick", "1234", False)
    log.debug(usuario)

    log.debug("Creando objeto Raza...")
    raza = Raza(1, "Yordle")
    log.debug(raza)

    log.debug("Creando objeto Equipamiento...")
    equipamiento = Equipamiento(1, "Filo Infinito")
    log.debug(equipamiento)

    log.debug("Creando objeto Habilidad...")
    habilidad = Habilidad(1, "Voluntad Inquebrantable", "Aumenta su defensa con menos de 100 de vida", 1)
    log.debug(habilidad)

    log.debug("Creando objeto Poder...")
    poder = Poder(1, "Bola de Fuego", "Lanza una bola de fuego ardiente que quema al enemigo", 1)
    log.debug(poder)

    log.debug("Creando objeto Personaje...")
    personaje = Personaje(1, "Chogath", 10, 1, 1, 1, 1)
    log.debug(personaje)

    
   
    

