from pathlib import Path


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

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "Error":
            return 0
        return self.strbases.count(base)

    def count(self):
        dict = {"A": self.count_base("A"), "T": self.count_base("T"), "C": self.count_base("C"),
                "G": self.count_base("G")} #no se si hay que poner strbases
        if self.strbases == "NULL" or self.strbases == "Error":
            return "A:", 0, "T:", 0, "C:", 0, "G:", 0
        return dict
#Como se pone cuando es null

    def reverse(self):
        if self.strbases == "NULL":
            return self.strbases
        elif self.strbases == "Error":
            return self.strbases

        return self.strbases[::-1]

    def complement(self):
        if self.strbases == "NULL":
            return self.strbases
        elif self.strbases == "Error":
            return self.strbases

        dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
        complement_seq = ""
        for element in self.strbases:
            complement_seq = complement_seq + dict[element]
        return complement_seq

    def read_fasta(self, filename):
        #Read the file
        file_contents = Path(filename).read_text()
        #Remove the head
        body = file_contents.split('\n')[1:]
        #Store the sequence read from the file
        self.strbases = "".join(body)
        return self




