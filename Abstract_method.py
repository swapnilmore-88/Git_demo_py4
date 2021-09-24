
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


class Flipkart(Ecommerce):

    def online_payment(self, amount):
        amount += 500
        return amount

    def cart(self, product):
        pass

class Myntra(Ecommerce):
    pass

f1 = Flipkart()
print(f1.online_payment(100))
# m1 = Myntra()
"by python second asdfsdfs"
# we cant create instance of abstract class
# e = Ecommerce()

"on python"