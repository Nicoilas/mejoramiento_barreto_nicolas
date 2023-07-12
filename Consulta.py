from Cita import *
class consulta:
    def __init__(self,id_consulta,cita_medica,enfermedad,diagnostico):
        self.id_consulta=id_consulta
        self.cita_medica=cita_medica
        self.enfermedad=enfermedad
        self.diagnostico=diagnostico
    def getid_consulta(self):
        return self.id_consulta
    def setid_consulta(self,id_consulta):
        self.id_consulta=id_consulta
    def getcita_medica(self):
        return self.cita_medica
    def setcita_medica(self,cita_medica):
        self.cita_medica=cita_medica
    def getemenfermedad(self):
        return self.enfermedad
    def setenfermedad(self,enfermedad):
        self.enfermedad=enfermedad
    def getdiagnostico(self):
        return self.diagnostico
    def setdiagnostico(self,diagnostico):
        self.diagnostico=diagnostico             