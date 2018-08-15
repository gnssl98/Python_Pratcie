class Fruit_Seller(object):
    def __init__(self, list_fruits):
        self.Fruits = list_fruits
        self.money = 0

    def sell_fruit(self, fruit, order_money):
        num_fruits = self.Fruits.get('fruit')
        
        
        


class Fruit_Buyer(object):
    def __init__(self, money):
        sefl.money = money
    
    def order(self, fruit, order_money):
        Fruit_Seller.sell_fruit(fruit, order_money)














list_fruits = { 'apple' : [30, 1000], 'orange' : [20, 2000], 'grape' : [40, 2000]}
seller1 = seller(list_fruits)
buyer = Buyer(100000)
buyer.order('orange', 3000)
