from utils import Messages,JsonFile
from gen import *
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
        return {
            "filename":"blogs.json",
            "data":"Test Export data"
        }

    @staticmethod
    @export_decorator
    def cache_products(number):
        return {
            "filename":"products.json",
            "data":"Test export data"
        }

if __name__=="__main__":
    Export.cache_users(10)
    Export.cache_blogs(15)
    Export.cache_products(20)