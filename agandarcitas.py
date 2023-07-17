from datetime import datetime, timedelta

class AdminCitas:
    def __init__(self):
        self.citas_disponibles = []

    def agregar_cita(self, cita):
        mes_actual = datetime.now().month
        if cita.fecha.month != mes_actual:
            print("No se puede programar citas en meses pasados o futuros.")
            return
        horario_disponible = self.verificar_horario_disponible(cita.medico, cita.fecha.time())
        if not horario_disponible:
            print("El médico no tiene disponibilidad en ese horario.")
            return
        consultorio_disponible = self.verificar_consultorio_disponible(cita.consultorio, cita.fecha)
        if not consultorio_disponible:
            print("El consultorio no está disponible en esa fecha y hora.")
            return

        self.citas_disponibles.append(cita)
        print("Cita registrada exitosamente.")

    def verificar_horario_disponible(self, medico, hora):
        pass

    def verificar_consultorio_disponible(self, consultorio, fecha):
        pass

    def eliminar_cita(self, cita):
        diferencia_tiempo = cita.fecha - datetime.now()
        if diferencia_tiempo.total_seconds() < 7200: 
            print("No se puede eliminar la cita con menos de 2 horas de anticipación.")
            return
        self.citas_disponibles.remove(cita)
        print("Cita eliminada exitosamente.")

    def obtener_citas_disponibles(self):
        return self.citas_disponibles
