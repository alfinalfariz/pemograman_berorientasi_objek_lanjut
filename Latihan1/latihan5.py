class PesawatTerbang: 
    def __init__(self, maskapai, tujuan): 
        self.maskapai = maskapai 
        self.tujuan = tujuan 
 
    def info(self): 
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}") 
 
 
pesawatA = PesawatTerbang("Fly Emirates", "Dubai - Jakarta") 
pesawatA.info()