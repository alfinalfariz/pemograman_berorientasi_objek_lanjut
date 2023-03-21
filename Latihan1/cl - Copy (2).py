class celcius:
    
    def __init__(self, celcius):
        self.celcius = celcius
        
    def reamur(self):
        return (self.celcius * 4/5)
     
celciusE = celcius(60)

print(f"Celcius Ke Kelvin: {celciusE.reamur()}")
