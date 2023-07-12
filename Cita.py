from Medico import *
from Paciente import*
class cita:
    def __init__(self,num_cita,fecha,dia,id_cita):
        self.num_cita=num_cita
        self.fecha=fecha
        self.dia=dia
        self.id_cita=id_cita
    def getnum_cita(self):
        return self.num_cita
    def setnum_cita(self,num_cita):
        self.num_cita=num_cita
    def getfecha(self):
        return self.fecha
    def setfecha(self,fecha):
        self.fecha=fecha
    def getdia(self):
        return self.dia
    def setdia(self,dia):
        self.dia=dia
    def getid_cita(self):
        return self.id_cita
    def setid_cita(self,id_cita):
        self.id_cita=id_cita    
