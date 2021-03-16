from utils import Messages,JsonFile
from gen import *
from entities import Blog
def export_decorator(function):
    def inner_function(*args,**kwargs):
        Messages.warning("Running {f}\n".format(f=function.__name__))
        data=function(*args)
        print(data)
        if(data["data"]!=None and len(data["data"])!=0):
            Messages.success("{f}\n".format(f=function.__name__))
            filePath=ExportDefaults.path+str(data["filename"])
            name=function.__name__
            n=name.split("_")
            JsonFile.exportJson(filePath,data["data"],fieldname=n[1])
        else:
            Messages.error("\a{f}\n".format(f=function.__name__))
        return function
    return inner_function

class ExportDefaults:
    path="./static/genericdata/"

class Export:
    @staticmethod
    @export_decorator
    def cache_users(number):
        print(number)
        return {
            "filename":"users.json",
            "data":UserGen.random_users(number)
        }

    @staticmethod
    @export_decorator
    def cache_blogs(number):
        blogs=[]
        b=Blog()
        while number>0:
            blogs+=[b.random_Blog()]
            number-=1
        return {
            "filename":"blogs.json",
            "data":blogs
        }

    @staticmethod
    @export_decorator
    def cache_products(number):
        products=[]
        p=Product()
        while number>0:
            products+=[p.gen_fullProduct()]
            number-=1
        return {
            "filename":"products.json",
            "data":products
        }
if __name__=="__main__":
    Export.cache_users(20)
    Export.cache_blogs(1)
    Export.cache_products(20)