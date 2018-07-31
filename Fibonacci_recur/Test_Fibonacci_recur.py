from Fibonacci_recur import Fibo

class Test_Fibo(Fibo):
    def test(self,Input_number):
        correct_fibonacci_seq = [1, 1, 2, 3, 5, 8]
        result = self.cal(Input_number) 
        assert correct_fibonacci_seq == result, "Not Correct"

test1 = Test_Fibo()
test1.test(6)

