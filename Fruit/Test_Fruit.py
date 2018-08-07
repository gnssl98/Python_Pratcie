from Fruit import Buyer
from Fruit import Seller


def test_fruit():
    buyer = Buyer(100000)
    seller = Seller(3000, 60)
    buyer.order(seller, 10000)
    assert buyer.num_apples == 2
    assert buyer.money == 91000
    assert seller.num_apples == 57
    assert seller.money == 9000
