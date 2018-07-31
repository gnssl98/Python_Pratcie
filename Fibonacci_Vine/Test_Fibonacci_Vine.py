from Fibonacci_Vine import Fibo

class Test_Fibo(Fibo):
    def test_cal(self, Input_number):
        Fibo_number = [1, 1]
        for Input_number in range(2, Input_number):
            cal_value = Fibo_number[Input_number-1] + Fibo_number[Input_number -2]
            Fibo_number.append(cal_value)
        return Fibo_number[Input_number]
    
    def test(self,Input_number):
        correct_fibonacci_num = self.test_cal(Input_number)  
        result = self.cal(Input_number) 
        assert correct_fibonacci_num == result, "Not Correct"

test1 = Test_Fibo()
test1.test(6)

