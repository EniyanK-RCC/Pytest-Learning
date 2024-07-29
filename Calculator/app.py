
class Calculator:
    def add(self, a, b):
        sum = int(a)+int(b)
        return sum
    
    def sub(self, a, b):
        diff = int(a)-int(b)
        return diff
    
    def mul(self, a, b):
        prod = int(a)*int(b)
        return prod
    
    def div(self, a, b):
        if b == 0:
            raise ValueError("Value cannot be divided by zero")
        quot = int(a)/int(b)
        return quot
    
