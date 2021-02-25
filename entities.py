from random import randrange

class UserTypes:
    @staticmethod
    def user_credentials():
        pass
    @staticmethod
    def user_financial():
        pass
    @staticmethod
    def user_comment():
        pass
    @staticmethod
    def user_review():
        pass


class Product:
    def __init__(self):
        pass
    def full_random_product(self):
        #pid,name,desc,price,shipping,images,weight,volume,reviews
        pass
    def display_product(self):
        #pid,name,price,pics
        pass

class Location:
    def __init__(self):
        pass
    def random_location(self):
        pass

class Text:
    @staticmethod
    def randomtext(lenght=100):
        pass

class Random:
    @staticmethod
    def genRandomInt(min,max):
        return randrange(min,max)

    @staticmethod
    def genRandomFloat(min,max):
        i=randrange(min,max)
        d=[10,100,1000,10000]
        return i/d[randrange(0,len(d))]


