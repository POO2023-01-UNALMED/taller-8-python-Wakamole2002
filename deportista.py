class Deportista:
    def __init__(self, años_practicando, deporte="Futbol"):
        self._deporte = deporte
        self._años_practicando = años_practicando

    # --------- getters and setters-------------
    def getDeporte(self):
        return self._deporte
    def setDeporte(self, deporte: str):
        self._deporte = deporte

    def getAñosPracticando(self):
        return self._años_practicando
    def setAñosPracticando(self, años_practicando):
        self._años_practicando = años_practicando
