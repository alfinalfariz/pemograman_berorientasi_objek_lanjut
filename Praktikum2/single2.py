class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang Makan.")
class mahasiswa(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim= nim
    def menjelaskan(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang memakan buah.")
mahasiswaA = mahasiswa("alfin", 35, "210511134")
mahasiswaA.berbicara() # Output: alfin sedang makan.
mahasiswaA.menjelaskan() # Output: alfin dengan NIM 210511012 sedang makan besar.