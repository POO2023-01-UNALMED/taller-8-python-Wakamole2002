from persona import Persona
from deportista import Deportista
class Futbolista(Persona, Deportista):
    lista_futbolista = []
    def __init__(self, nombre, edad, altura, sexo, años_practicando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,años_practicando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.lista_futbolista.append(self)
    
    # --------- getters and setters ----------
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
    
    def __str__(self):
        return f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"
                