
from abc import ABC, abstractmethod

class Ecommerce(ABC):

    @abstractmethod
    def online_payment(self,amount):
        amount += 200
        return amount


    @abstractmethod
    def cart(self, product):
        pass
    #
    # @abstractmethod
    # def delivery(self, address):
    #     pass

    def search_product(self):
        pass

    def give_rating(self):
        pass

"jus fun"
class Flipkart(Ecommerce):

    def online_payment(self, amount):
        amount += 500
        return amount

    def cart(self, product):
        pass
"to sheck 2"
class Myntra(Ecommerce):
    pass
"to check"
f1 = Flipkart()
print(f1.online_payment(100))
# m1 = Myntra()
<<<<<<< HEAD
"finally"
"to check from python"
# we cant create instance of abstract class
# e = Ecommerce()

"on python"
"sfsdfsd"


"for reset soft"