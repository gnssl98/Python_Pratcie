class Seller(object):
    def __init__(self, price_apple, num_apple):
        self.price_apple = price_apple
        self.num_apple = num_apple

    def cal(self, money):
        apple_num = money // self.price_apple
        pay = apple_num * self.price_apple
        self.num(apple_num)
        if apple_num < 1 :
            print('Not enough Money')
        else:
            self.change(money, apple_num, pay)
            self.pay(pay)

    def num(self, apple_num):
        self.num_apple -= apple_num

    def change(self, money, apple_num, total_money):
        change = money - (total_money)
        print('Change : {}'.format(change))

    def pay(self, pay):
        print('Pay: {}'.format(pay))


    def main(self, money):
        print('---------------------\nSeller\n---------------------')
        self.cal(money)
        print('Num of Apple : {}'.format(self.num_apple))

class Buyer(object):
    def __init__(self, money):
        self.money = money

    def order(self, seller, money):
       print('---------------------\nBuyer\n---------------------')
       print('Money : {}\nMoney to buy apple : {}\nTo Buy : {}\n'.format(self.money,money, seller))
       seller.main(money)


seller1 = Seller(3000, 50)
buyer1 = Buyer(300000)
buyer1.order(seller1, 10000)

seller2 = Seller(5000, 100)
buyer2 = Buyer(4000000)
buyer2.order(seller2, 10000)
