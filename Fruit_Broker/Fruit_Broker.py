class Seller(object):
    def __init__(self, price_apple, num_apples):
        self.price_apple = price_apple
        self.num_apples = num_apples
        self.money = 0

    def cal(self, order_money):
        order_num_apples = order_money // self.price_apple
        if order_num_apples >= self.num_apples:
            sell_num_apples = self.num_apples
            self.num_apples = 0
            sell_num_apples
            return sell_num_apples
        else:
            return order_num_apples
            self.num_apples -= order_num_apples
            sell_money = order_num_apples * self.price_apple
            self.money += sell_money
            
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
   
    def select_cheap_seller(self):
        for i in self.sellers:
            if self.cheap_seller.price_apple > self.sellers[i].price_apple:
                self.cheap_seller = self.sellers[i]
        return self.cheap_seller
    
    def cal(self, order_money):
        sell_money = order_money // self.cheap_seller.price_apple
        self.commission = sell_money * 1.1
        if order_money < sell_money + self.commission:
            raise ValueError("Not enough Money")
        else:
            return sell_money, self.sell_fruit(order_money)
    
    def sell_fruit(self, order_money):
        cheap_seller = self.cheap_seller
        num_apples = cheap_seller.cal(order_money)
        order_num_apples = order_money // cheap_seller.price_apple
        if num_apples < order_num_apples:
            self.sellers.remove(cheap_seller)
            self.cheap_seller = select_cheap_seller(self)
            re_order_money = (order_num_apples - num_apples) * self.cheap_seller.price_apple
            self.cal(re_order_money)
        
        self.money += self.commission
        return num_apples  
    
    def __str__(self):
        return "-------------------------\nBroker\n----------------------\nCommision: {} \nMoney: {}".format(self.commission, self.money)


def main():
    sellers = [ Seller(3000, 60), Seller(5000, 50), Seller(2000, 30), Seller(1000, 10)]
    broker = Broker(sellers)
    buyer1 = Buyer(100000)
    buyer1.order(broker, 10000)
    print(broker.cheap_seller)
    print(broker)
    print(buyer1)

if __name__ == "__main__" :
    main()
