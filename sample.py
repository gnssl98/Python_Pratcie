class Seller(object):
    def __init__(self, price_apple, num_apple):
        self.price_apple = price_apple
        self.num_apple = num_apple
        self.change = 0
        self.money = 0
        self.pay = 0
        self.num_apples = 0

    def cal(self, money):
        num_apples = money // self.price_apple
        self.num_apples += num_apples
        self.pay = num_apples * self.price_apple
        self.num(num_apples)
        if self.num_apples < 1 :
            print('Not enough Money')
        else:
            self.change = money - self.pay
            self.money += self.pay

    def num(self, apple_num):
        self.num_apple -= apple_num

    def main(self, money):
        print('---------------------\nSeller\n---------------------')
        self.cal(money)
        print('Money which seller give : {}\nNum of Apple : {}'.format(money, self.num_apple))
        print("change : {}\nMoney which after sell Apple : {}".format(self.change, self.money))

class Buyer(object):
    def __init__(self, money):
        self.money = money
        self.num_apples = 0

    def cal(self, seller):
        self.num_apples += seller.num_apples

    def order(self, seller, money):
       seller.main(money)
       self.cal(seller)
       print('---------------------\nBuyer\n---------------------')
       print('Money : {}\nMoney to buy apple : {}\nNum of apple : {}'.format(self.money, money, seller.num_apples))
       self.money -= seller.pay
       print('Money which after buy apple : {}'.format(self.money))




seller1 = Seller(3000, 50)
buyer1 = Buyer(300000)
buyer1.order(seller1, 10000)
buyer1.order(seller1, 5000)
