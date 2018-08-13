class Seller(object):
    def __init__(self, price_apple, num_apples):
        self.price_apple = price_apple
        self.num_apples = num_apples
        self.money = 0

    def cal(self, sell_money):
        order_num_apples = sell_money // self.price_apple
        if order_num_apples >= self.num_apples:
            sell_num_apples = self.num_apples
            self.num_apples = 0
            self.money += self.num_apples * self.price_apple 
            return sell_num_apples
        else:
            self.num_apples -= order_num_apples
            sell_money = order_num_apples * self.price_apple
            self.money += sell_money
            return order_num_apples
            
    def __str__(self):
        return "--------------------------\nSeller\n-----------------------\nNum of Apples :{}\nMoney :{} ".format(self.num_apples, self.money)
            

class Buyer(object):
    def __init__(self, money):
        self.money = money
        self.num_apples = 0

    def order(self, broker, order_money):
        sell_money, num_apples = broker.cal(order_money)
        self.money -= sell_money 
        self.num_apples += num_apples

    def __str__(self):
        return "----------------------\nBuyer\n-----------------------\nNum of Apples :{}\nMpney : {}".format(self.num_apples, self.money)
        

class Broker(object):
    def __init__(self, sellers):  
        self.sellers = sellers
        self.cheap_seller = sellers[0] 
        self.money = 0
        self.commision = 0
        self.change = 0
   
    def select_cheap_seller(self):
        for seller in self.sellers:
            if self.cheap_seller.price_apple > seller.price_apple:
                self.cheap_seller = seller
        return self.cheap_seller
    
    def cal(self, order_money):
        self.select_cheap_seller()
        num_apples = order_money // self.cheap_seller.price_apple
        sell_money = num_apples * self.cheap_seller.price_apple
        self.commission = sell_money * 0.1
        if num_apples == 0:
            raise ValueError("Not enough Money")
        elif order_money <= sell_money + self.commission:
            num_apples -= 1
            sell_money = num_apples * self.cheap_seller.price_apple
            self.commission = sell_money * 0.1
            return sell_money + self.commission, self.sell_fruit(sell_money, num_apples)
        else:
            return sell_money + self.commission, self.sell_fruit(sell_money, num_apples)
        self.change = order_money - sell_money - self.commission    
    
    def sell_fruit(self, sell_money, order_num_apples):
        cheap_seller = self.cheap_seller
        num_apples = cheap_seller.cal(sell_money)
        if num_apples < order_num_apples:
            if cheap_seller in self.sellers:
                self.sellers.remove(cheap_seller)
            self.cheap_seller = self.select_cheap_seller()
            re_order_money = (order_num_apples - num_apples) * self.cheap_seller.price_apple
            self.cal(re_order_money)
        
        self.money += self.commission
        return num_apples  
    
    def __str__(self):
        return "-------------------------\nBroker\n----------------------\nCommision: {} \nMoney: {}\nChange : {}".format(self.commission, self.money, self.change)


def main():
    sellers = [ Seller(3000, 60), Seller(5000, 50), Seller(2000, 30), Seller(1000, 10)]
    broker = Broker(sellers)
    buyer1 = Buyer(100000)
    buyer1.order(broker, 10000)
    print(broker.cheap_seller)
    print(broker)
    print(buyer1)
    buyer2 = Buyer(100000)
    buyer2.order(broker, 40000)
    print(broker.cheap_seller)
    print(broker)
    print(buyer2)


if __name__ == "__main__" :
    main()
