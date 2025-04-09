class Hospital:
    def __init__(self):
        self.NombrePaciente: str = "panchito"
        self.nss: int = 1258
        self.enfermedad: str = "Gripa"

        def getNombrePaciente(self)->str:
            return self.enfermedad

        def getNss(self)->int:
            return self.nss

        @property
        def getEnfermedad(self)->str:
            return self.enfermedad

        def setNombrePaciente(self,nombre:str):
            self.NombrePaciente=nombre

        def setNss(self,nss:int):
            self.nss=nss

        #@setEnfermedad.setter
        def setEnfermedad(self,enfermedad:str):
            self.enfermedad=enfermedad


if __name__ == '__main__':

    hospital=Hospital()

    hospital.__NombrePaciente="juan"
     



