import math
class Fibo(object):
    def __init__(self):
        self.Fibo = 0


    def cal(self, Input_number):
        Vine1 = (1 + math.sqrt(5)) / 2
        Vine2 = (1 - math.sqrt(5)) / 2
        self.Fibo = ((Vine1 ** Input_number) - (Vine2 ** Input_number)) // (math.sqrt(5)) 
        return self.Fibo

    def __str__(self):
        return self.Fibo



fibo = Fibo()
result = fibo.cal(6)
print(result)

