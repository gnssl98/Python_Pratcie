class Buyer(object):
    def __init__(self, money):
        self.money = money
        self.num_apples = 0
        self.change = 0

    def order(self, seller, order_money):
        money, num_apples, self.change = seller.cal(order_money)
        self.num_apples += num_apples
        self.money -= money

    def __str__(self):
        return "Buyer\n----------------------\nMoney : {}\nNum of apples : {}\nChange : {}".format(self.money, self.num_apples, self.change)


class Seller(object):
    def __init__(self, price_apple, num_apples):
        self.price_apple = price_apple
        self.num_apples = num_apples
        self.money = 0

    def cal(self, order_money):
        num_apples = order_money // self.price_apple
        if num_apples < 1 :
            raise  ValueError("Not enough Money")
        else :
            self.num_apples -= num_apples
            if self.num_apples < 0:
                raise ValueError("Not enough Apples")
            money = num_apples * self.price_apple
            self.money += money
            change = order_money - money
            return money, num_apples, change

    def __str__(self):
        return "-------------------------\nSeller\n-------------------------\nNum of Apples : {}\nMoney : {}".format(self.num_apples, self.money)

def main():
    seller1 = Seller(3000, 60)
    buyer1 = Buyer(100000)
    buyer1.order(seller1, 10000)
    print(buyer1)
    buyer1.order(seller1, 30000)
    print(buyer1)
    print(seller1)
    buyer1.order(seller1, 2000)
    print(seller1)
    print(buyer1)

if __name__ == "__main__":
    main()
