class paciente:
    def __init__(self,nombre,apellido,cita_medica):
        self.nombre=nombre
        self.apellido=apellido
        self.cita_medica=cita_medica
    def getnombre(self):
        return self.nombre
    def setnombre(self,nombre):
        self.nombre=nombre
    def getapellido(self):
        return self.apellido
    def setapellido(self,apellido):
        self.apellido=apellido
    def getcita_medica(self):
        return self.cita_medica
    def setcita_medica(self,cita_medica):
        self.cita_medica=cita_medica    