class Fibo(object):
    def __init__(self):
        self.Fibo_number = list()
        self.Fibo_number[0:1] = 1, 1

    def cal(self, Input_number):
        for Input_number in range(2, Input_number):
            temp = self.Fibo_number[Input_number - 1] + self.Fibo_number[Input_number - 2]
            self.Fibo_number.append(temp)

    def __str__(self):
        return "{}".format(self.Fibo_number[self.cal.Input_number])

fibo1 = Fibo.cal(6)
print(fibo1)
