class Fruit_Buyer(object):
    def __init__(self, have_money):
        self.have_money = have_money
        self.num_apples = 0

    def order(self, broker, order_money):
        total_sell_money, num_apples =broker.order(order_money)
        self.have_money -= total_sell_money
        self.num_apples += num_apples

    def __str__(self):
        return "Buyer\nhave_money : {}\nnum_apples:{}\n---------------------------------\n".format(self.have_money, self.num_apples)


class Fruit_Broker(object):
    def __init__(self, sellers):
        self.sellers = sellers
        self.cheap_seller = sellers[0]
        self.have_money = 0
        self.commission = 0

    def select_cheapest_seller(self):
        for seller in self.sellers:
            if self.cheap_seller.price_apple > seller.price_apple:
                self.cheap_seller = seller
                break

    def order(self, order_money):
        self.select_cheapest_seller()
        num_apples = order_money // self.cheap_seller.price_apple
        sell_money = self.cheap_seller.price_apple * num_apples
        self.commission = sell_money * 0.1
        total_sell_money = sell_money + self.commission
        total_sell_money = self.cal(total_sell_money, order_money, num_apples)
        seller_num_apples = self.cheap_seller.cal(sell_money, num_apples)
        self.distinct_seller_fruit(num_apples, seller_num_apples, order_money)
        self.commission = sell_money* 0.1
        self.have_money += self.commission
        return total_sell_money, num_apples

    def distinct_seller_fruit(self, num_apples, seller_num_apples, order_money):
        if seller_num_apples < num_apples:
            num_apples -= seller_num_apples
            order_money -= num_apples * seller_num_apples
            cheap_seller = self.cheap_seller
            if cheap_seller in self.sellers:
                self.sellers.remove(cheap_seller)
                return self.order(order_money)
        

    def cal(self, total_sell_money, order_money, num_apples):
        if total_sell_money > order_money :
            if self.cheap_seller.price_apple > order_money:
                raise ValueError("Not enough Money")
            else:
                for i in range(1, num_apples,1):
                    cal_money = i * self.cheap_seller.price_apple * 1.1
                    if cal_money > order_money :
                        total_sell_money = (i-1) * self.cheap_seller.price_apple * 1.1
                        break
        return total_sell_money

    def __str__(self):
        return "Broker\nhave_money : {}\ncommission : {}\n--------------------------------\n".format(self.have_money,self.commission)

class Fruit_Seller(object):
    def __init__(self, price_apple, num_apples):
        self.price_apple = price_apple
        self.num_apples = num_apples
        self.have_money = 0

    def cal(self, sell_money, num_apples):
        if self.num_apples == 0:
            return 0
        elif num_apples > self.num_apples:
            self.num_apples = 0 
            part_sell_money = self.num_apples * self.price_apple
            self.have_money += part_sell_money
            return self.num_apples
        else :
            self.num_apples -= num_apples
            self.have_money += sell_money
            return num_apples

    def __str__(self):
        return "Seller\nhave_money : {}\nnum_apples : {}\n-------------------------------------\n".format(self.have_money, self.num_apples)

def main():
    sellers = [ Fruit_Seller(2000, 10), Fruit_Seller(3000, 20), Fruit_Seller(1000, 5) ]
    broker = Fruit_Broker(sellers)
    buyer1 = Fruit_Buyer(10000)
    buyer1.order(broker,4000)
    print(broker.cheap_seller)
    print(broker)
    print(buyer1)
    buyer1.order(broker,2000)
    print(broker.cheap_seller)
    print(broker)
    print(buyer1)


if __name__ == "__main__":
    main()
