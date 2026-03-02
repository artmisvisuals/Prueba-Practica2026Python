from services import serviceplantilla as services

service = services.ServicePlantilla()

def dibujarPlantilla():
    print("Mostrar plantilla hospital")
    lista = service.getplantilla()
    for p in lista:
        print(f"Id Hospital: {p.idHospital} - Id Sala: {p.idSala} - Id Empleado: {p.idEmpleado} - {p.apellido} - {p.funcion} - {p.turno} - {p.salario}")

dibujarPlantilla()