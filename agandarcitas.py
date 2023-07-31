from datetime import datetime, timedelta

class Cita:
    def __init__(self, medico, consultorio, fecha):
        self.medico = medico
        self.consultorio = consultorio
        self.fecha = fecha

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
        # Lógica para verificar la disponibilidad del horario del médico
        return True  # Supongamos que siempre está disponible

    def verificar_consultorio_disponible(self, consultorio, fecha):
        # Lógica para verificar la disponibilidad del consultorio en la fecha y hora especificadas
        return True  # Supongamos que siempre está disponible

    def eliminar_cita(self, cita):
        diferencia_tiempo = cita.fecha - datetime.now()
        if diferencia_tiempo.total_seconds() < 7200:
            print("No se puede eliminar la cita con menos de 2 horas de anticipación.")
            return
        self.citas_disponibles.remove(cita)
        print("Cita eliminada exitosamente.")

    def obtener_citas_disponibles(self):
        return self.citas_disponibles


def ingresar_fecha():
    while True:
        try:
            fecha_str = input("Ingrese la fecha de la cita (formato dd/mm/yyyy hh:mm): ")
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            return fecha
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")

def main():
    admin_citas = AdminCitas()

    while True:
        print("\n1. Agregar cita\n2. Eliminar cita\n3. Ver citas disponibles\n4. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            medico = input("Ingrese el nombre del médico: ")
            consultorio = input("Ingrese el número del consultorio: ")
            fecha = ingresar_fecha()

            cita = Cita(medico, consultorio, fecha)
            admin_citas.agregar_cita(cita)

        elif opcion == "2":
            medico = input("Ingrese el nombre del médico de la cita que desea eliminar: ")
            consultorio = input("Ingrese el número del consultorio de la cita que desea eliminar: ")
            fecha = ingresar_fecha()

            cita = Cita(medico, consultorio, fecha)
            admin_citas.eliminar_cita(cita)

        elif opcion == "3":
            citas_disponibles = admin_citas.obtener_citas_disponibles()
            if not citas_disponibles:
                print("No hay citas disponibles.")
            else:
                print("Citas disponibles:")
                for idx, cita in enumerate(citas_disponibles, start=1):
                    print(f"{idx}. Médico: {cita.medico}, Consultorio: {cita.consultorio}, Fecha: {cita.fecha}")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
