class Medico:
    def __init__(self, nombre, id_medico, lugar_trabajo, telefono, correo):
        self.nombre = nombre
        self.id_medico = id_medico
        self.lugar_trabajo = lugar_trabajo
        self.telefono = telefono
        self.correo = correo
        self.citas_agendadas = []

    def agregar_cita(self, paciente, fecha, hora, motivo):
        cita = {
            'paciente': paciente,
            'fecha': fecha,
            'hora': hora,
            'motivo': motivo
        }
        self.citas_agendadas.append(cita)

    def consultar_citas_agendadas(self):
        if len(self.citas_agendadas) == 0:
            print("No hay citas agendadas.")
        else:
            print("Citas agendadas:")
            for cita in self.citas_agendadas:
                print("Paciente:", cita['paciente'])
                print("Fecha:", cita['fecha'])
                print("Hora:", cita['hora'])
                print("Motivo:", cita['motivo'])
                print("")

    def consultar_dias_disponibles(self):
        dias_disponibles = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        for cita in self.citas_agendadas:
            dia = cita['fecha'].split('-')[0] 
            if dia in dias_disponibles:
                dias_disponibles.remove(dia)
        print("Días aún no agendados:")
        print(dias_disponibles)

medico = Medico("Dr. Juan Perez", "123456", "Hospital ABC", "1234567890", "drjuanperez@example.com")
medico.agregar_cita("Juanito", "10-07-2023", "09:00", "Consulta general")
medico.agregar_cita("Mariana", "12-07-2023", "15:30", "Control de embarazo")
medico.consultar_citas_agendadas()
medico.consultar_dias_disponibles()
