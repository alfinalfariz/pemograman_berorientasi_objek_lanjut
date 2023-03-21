class celcius:
    
    def __init__(self, celcius):
        self.celcius = celcius
        
    def fahrenhiet(self):
        return (self.celcius * 9 / 5) + 32
     
celciusE = celcius(75)

print(f"Celcius Ke Fahrenheit: {celciusE.fahrenhiet()}")
