class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "mengonggong")
class anjing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Guggggg!!!!")
AnjingA = anjing("dog", 2, "pitbul")
AnjingA.bergerak() # output: dog bergerak
AnjingA.bersuara() # output: Gog!