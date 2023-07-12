class medico:
    def __init__(self,nombre,id_medico,lugar_trabajo,telefono,correo):
        self.nombre=nombre
        self.id_medico=id_medico
        self.lugar_trabajo=lugar_trabajo
        self.telefono=telefono
        self.correo=correo
    def getnnombre(self):
        return self.nombre
    def setnombre(self,nombre):
        self.nombre=nombre
    def get_id_medico(self):
        return self.id_medico
    def set_id_medico(self,id_medico):
        self.id_medico=id_medico
    def getlugar_trabajp(self):
        return self.lugar_trabajo
    def setlugar_trabajo(self,lugar_trabajo):
        self.lugar_trabajo=lugar_trabajo
    def gettelefono(self):
        return self.telefono
    def settelefono(self,telefono):
        self.telefono=telefono    
    def getcorreo(self):
        return self.correo
    def setcorreo(self,correo):
        self.correo=correo    