class Mahasiswa: 
    def __init__(self, nama, npm): 
        self.nama = nama 
        self.npm = npm 
 
    def info(self): 
        print(f"Nama: {self.nama}\nNPM: {self.npm}") 
 
mahasiswaB = Mahasiswa("Alfin", "21051113") 
mahasiswaB.info()