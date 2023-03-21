class Kalkulator: 
    @staticmethod 
    def add(x, y): 
        return x + y 
     
    @staticmethod 
    def subtract(x, y): 
        return x - y 
     
    @staticmethod 
    def multiply(x, y): 
        return x * y 
     
    @staticmethod 
    def divide(x, y): 
        if y == 0: 
            raise ValueError('Tidak dapat membagi dengan nol.') 
        return x / y 
 
# Memanggil metode statis add() dan subtract() di dalam class Math 
print(Kalkulator.add(2, 9))       # Output: 11
print(Kalkulator.subtract(20, 2)) # Output: 18 
 
# Memanggil metode statis multiply() dan divide() di dalam class Math 
print(Kalkulator.multiply(9, 6))  # Output: 54 
print(Kalkulator.divide(11, 2))   # Output: 5.5