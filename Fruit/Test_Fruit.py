from Fruit import Buyer
from Fruit import Seller

class test_fruit_buyer(object):
    def __init__(self):
        self.test_num_apples = 0
        self.test_money = 0

    def test(self):
        test_buyer = Buyer()
        test_num_after_apples = test_buyer.self.num_apples
        test_num_buy_apples = test_buyer.order.num_apples
        test_buy_money = test_buyer.order.money
        test_after_money = test_buyer.self.money

        self.test_num_apples += test_num_buy_apples
        self.test_money += test_buy_money

        assert self.test_num_apples == test_num_after_apples, "Not Correct Num of Apples"
        assert self.test_money == test_after_money, "Not Correct Money"

class test_fruit_seller(Seller):
    def __init__(self, num_apples):
        self.test_num_apples = num_apples
        self.test_money = 0

    def test(self):
        self.test_num_apples -= self.cal.num_apples
        test_sell_money = self.cal.money

        self.test_money += test_sell_money
        
        assert self.test_num_apples == self.num_apples, "Not Correct Num of Apples"
        assert self.test_money == self.money, "Not Correct Money"


test1_buyer = test_fruit_buyer()
test1_buyer.test
test1_seller = test_fruit_seller(60)
test1_seller.test

