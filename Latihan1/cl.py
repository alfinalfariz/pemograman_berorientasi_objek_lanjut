# ALFIN DWI ALFARIZ
# 210511134
# R4 - D

class celcius:
    
    def __init__(self, celcius):
        self.celcius = celcius
        
    def fahrenhiet(self):
        return (self.celcius * 9 / 5) + 32
    
    def kelvin(self):
        return (self.celcius + 273.15)
    
    def reamur(self):
        return (self.celcius * 4/5)
    
celciusE = celcius(80)

print(f"Celcius Ke Fahrenheit: {celciusE.fahrenhiet()}")
print(f"Celcius Ke Kelvin: {celciusE.kelvin()}")
print(f"Celcius Ke Reamur: {celciusE.reamur()}")
    