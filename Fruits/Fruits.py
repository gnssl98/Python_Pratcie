class Fruit_Seller(object):
    def __init__(self, dict_fruits):
        self.Fruits = dict_fruits
        self.money = 0

    def sell_fruit(self, fruit, order_money):
        info_fruits = self.Fruits.get('fruit')
        order_nums_fruits = order_money // info_fruit[1]
        sell_money = order_nums_fruits * info_fruit[1]
        self.money += sell_money
        self.Fruits[fruit] -= [order_nums_fruits , 0]
        return sell_money, order_num_fruits
       
    def __str__(self):
        return "----------------------\nSeller\n-------------------Num of {} : {} ".format(fruit, num_fruits)
        


class Fruit_Buyer(object):
    def __init__(self, money):
        self.money = money
        self.info_fruits = []
    
    def order(self, fruit, order_money):
        sell_money , order_num_fruits = Fruit_Seller.sell_fruit(fruit, order_money)
        self.money += sell_money
        self.info_fruits = [{},{}].format(fruit, sell_money)




dict_fruits = { 'apple' : [30, 1000], 'orange' : [20, 2000], 'grape' : [40, 2000]}
seller1 = Fruit_Seller(dict_fruits)
buyer = Fruit_Buyer(100000)
buyer.order('orange', 3000)
