class Seq:
    """A class for representing a sequence objects"""
    def __init__(self, strbases="NULL"): #espera que le mandes una secuencia, al ponerle el null si está vacía no te da error
        if strbases== "NULL":
            self.strbases = "NULL"
            print("NULL Sequence created")
            return

        for element in strbases:
            list = ["A", "C", "G", "T"]
            if element not in list:
                self.strbases = "Error"  # nombre que le das dentro del objeto (self.) ahora queremos comprobar si es correcto antes de almacenarlo
                print("Invalid sequence")
                return

        self.strbases = strbases
        print("New sequence created!")


    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "Error":
            return 0
        return len(self.strbases)




