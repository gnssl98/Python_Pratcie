class Seller(object):
    def __init__(self, apple_money, pocket):
        self.apple_money = apple_money
        self.pocket =pocket

    def cal(self):
        return self.pocket


class Buyer(object):
    def __init__(self, pocket, count, who, pay):
        self.pocket = pocket
        self.count  = count
        self.who = who
        self.pay = pay

    def pay(self):
        self.pay = self.count * self.who.apple_money
        self.who.cal = self.pay


seller1 = Seller(3000)
buyer1 = Buyer(300000, 10, seller1)
