from utils import Messages,JsonFile
from gen import *
from entities import Blog
def export_decorator(function):
    def inner_function(*args,**kwargs):
        Messages.warning("Running {f}\n".format(f=function.__name__))
        data=function(*args)
        #print(data)
        if(data["data"]!=None and len(data["data"])!=0):
            #Messages.success("{f}\n".format(f=function.__name__))
            filePath=ExportDefaults.path+str(data["filename"])
            name=function.__name__
            n=name.split("_")
            JsonFile.exportJson(filePath,data["data"],fieldname=n[1])
            Messages.success("Sucess in exporting {f}\n".format(f=function.__name__))
        else:
            Messages.error("\a{f}\n".format(f=function.__name__))
        return function
    return inner_function

class ExportDefaults:
    path="./static/genericdata/"

class Export:
    @staticmethod
    @export_decorator
    def cache_profiles(number):
        #print(number)
        return {
            "filename":"user_profiles.json",
            "data":UserGen.random_users(number)
        }

    @staticmethod
    @export_decorator
    def cache_userAuth(number):
        return {
            "filename":"user_auth.json",
            "data":UserGen.random_users_profiles(number)
        }
    
    @staticmethod
    @export_decorator
    def cache_reviews(number):
        return {
            "filename":"reviews.json",
            "data":UserGen.gen_user_reviews(number)
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
    def cache_blogSnippets(number):
        return{
            "filename":"BlogListSnippets.json",
            "data":Blogs.blogSnippets(number)
        }

    @staticmethod
    @export_decorator
    def cache_productList(number):
        products=[]
        p=Product()
        while number>0:
            products+=[p.gen_fullProduct()]
            number-=1
        return {
            "filename":"products.json",
            "data":products
        }

    @staticmethod
    @export_decorator
    def cache_list(number):
        return{
            "filename":"simple_list.json",
            "data":List.simple_list(number)
        }

if __name__=="__main__":
    Export.cache_profiles(100)
    Export.cache_userAuth(100)
    Export.cache_reviews(50)
    Export.cache_blogs(1)
    Export.cache_blogSnippets(20)
    Export.cache_productList(20)
    Export.cache_list(1000)