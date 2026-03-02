import oracledb
from models import plantilla as models

class ServicePlantilla:
    def __init__(self):
        self.connection = oracledb.connect(user="system"
                                    , password="oracle"
                                    , dsn="localhost/freepdb1")
                

    def getplantilla(self):
        cursor = self.connection.cursor()
        sql = "select * from PLANTILLA"
        cursor.execute(sql)
        listaPlantilla = []
        for row in cursor:
            plantilla = models.Plantilla()
            plantilla.idHospital = row[0]
            plantilla.idSala = row[1]
            plantilla.idEmpleado = row[2]
            plantilla.apellido = row[3]
            plantilla.funcion = row[4]
            plantilla.turno = row[5]
            plantilla.salario = row[6]
            listaPlantilla.append(plantilla)
        cursor.close()
        return listaPlantilla
    
