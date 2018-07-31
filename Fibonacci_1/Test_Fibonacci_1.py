from Fibonacci_1 import Fibo

class Test_Fibo(Fibo):
    def cal(self, Input_number):
        for Input_number in range(2, Input_number):
            cal_value = self.Fibo_number[Input_number -1 ] + self.Fibo_number[Input_number - 2]
            self.Fibo_number.append(cal_value)
        return self.Fibo_number 

ans = [ 1, 1, 2, 3, 5, 8 ]
nums = Test_Fibo()
result = nums.cal(6)
assert ans == result
