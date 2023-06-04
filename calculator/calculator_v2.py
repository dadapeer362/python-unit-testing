class CalculatorV2:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def calc_add(self):
        total = self.num1 + self.num2
        return total
    
    def calc_sub(self):
        total = self.num1 - self.num2
        return total