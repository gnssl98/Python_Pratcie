class Fruit_Buyer(object):
    def __init__(self, money):
        self.money = money
        self.num_fruits = 0
        self.kind_fruit = 0
        self.change = 0

    def order(self, seller, kind_fruit, order_money):
        sell_money, num_fruits = seller.cal(kind_fruit, order_money)
        self.num_fruits += num_fruits
        self.kind_fruit = kind_fruit
        self.money -= sell_money
    
    def __str__(self):
        return "Buyer\nkind_fruit : {}\nnum_fruits : {}\nmoney_after_buy_fruits : {}\n--------------------------\n".format(self.kind_fruit, self.num_fruits, self.money)

class Fruit_Seller(object):
    def __init__(self, dict_fruits):
        self.fruits = dict_fruits
        self.change = 0
        self.money = 0
        self.kind_fruit = 0

    def cal(self, kind_fruit, order_money):
        price_fruit = self.fruits.get(kind_fruit)[1]
        num_fruits = order_money / price_fruit
        sell_money = num_fruits * price_fruit
        self.change = order_money - sell_money 
        self.money += sell_money
        self.fruits.get(kind_fruit)[0] -= num_fruits
        self.kind_fruit = kind_fruit
        return order_money, num_fruits

    def __str__(self):
        return "Seller\nkind_fruit : {}\nnum_fruits : {}\nmoney_after_sell_fruits : {}\n--------------------------\n".format(self.kind_fruit, self.fruits.get(self.kind_fruit)[0], self.money)




def main():
    dict_fruits = { 'apple' : [30, 1000], 'banna' : [10, 3000]}
    seller1 = Fruit_Seller(dict_fruits)
    buyer1 = Fruit_Buyer(100000)
    buyer1.order(seller1,'apple', 10000)
    print(seller1)
    print(buyer1)

if __name__ == "__main__":
    main()

