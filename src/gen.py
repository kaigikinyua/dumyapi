"""
Generator functions for various generic data
"""
from random import randrange
import json
from entities import *
from utils import JsonFile,Messages
#Base generic data generators
class UserGen:
    @staticmethod
    def random_users(number):
        users=[]
        u=User()
        while number>0:
            users+=[u.gen_fulluser()]
            number-=1
        return users
    
    @staticmethod
    def random_users_profiles(number):
        users=[]
        u=User()
        while(number>0):
            users+=[u.gen_userProfile()]
            number-=1
        return users

    @staticmethod
    def random_users_login_cred(number):
        users=[]
        u=User()
        while(number>0):
            users+=[u.gen_userLogin()]
            number-=1
        return users

    @staticmethod
    def gen_user_reviews(number):
        users=[]
        u=User()
        while(number>0):
            users+=[u.gen_userReview()]
            number-=1
        return users

    @staticmethod
    def export_data(data):
        f=JsonFile.exportJson(filepath="./genericdata/users.json",data=data)
        if(f==False):
            Messages.error(message="Could not export users data to ./genericdata/users.json",log=True)
            Messages.error(message="Userdata -> {d}".format(d=data))
            return False
        else:
            return True

class Blogs:
    @staticmethod
    def blogSnippets(number):
        data=JsonFile.loadData("./schemas/blogs.json")
        snippets=[]
        if(data!=False and data!=None and data!={}):
            for blog in data["blogs"]:
                snippets+=[{
                    "title":blog["title"],
                    "author":blog["author"],
                    "likes":blog["likes"],
                    "dislikes":blog["dislikes"],
                    "views":blog["views"],
                    "date":blog["date"],
                    "thumb_nail":blog["thumb_nail"]
                }]
        else:
            Messages.error("Got {r} while retriving blog snippets".format(r=data))
            snippets=None
        return snippets

    @staticmethod
    def randomBlog():
        blog=Blogs.blogSnippets(1)
        if(blog!=None):
            paragraphs=JsonFile.loadData('./schemas/text_blobs.json')
            p=paragraphs["medium_par"]
            paragraphs=p[0:randrange(0,len(p))]
            blog[0]["paragraphs"]=paragraphs
            blog[0]["comments"]=UserReview.random_reviews(3)
        return blog[0]
    

class Products:
    @staticmethod
    def getProductsInCategory(category):
        product_data=JsonFile.loadData("./schemas/products.json")
        categories=product_data["categories"]
        if(category in categories):
            products=product_data["products"]
            for p in products:
                try:
                    return p[category]
                except KeyError:
                    del p
        else:
            msg="Could not find product category {c} in categories {cs}".format(c=category,cs=categories)
            Messages.error(msg)
        return None

    @staticmethod
    def genRandomProductList():
        product_data=JsonFile.loadData("./schemas/products.json")
        categories=product_data["categories"]
        c=categories[randrange(0,len(categories))]
        print(c)
        product_list=Products.getProductsInCategory(c)
        if(product_list==None):
            Messages.error("Could not find category {x} ".format(x=c))
            product_list=None
        return product_list

    @staticmethod
    def getAllProductList():
        product_data=JsonFile.loadData("./schemas/products.json")
        if (product_data["products"]!=None):
            return product_data["products"]
        else:
            return None

class List:
    @staticmethod
    def fetch_lists(obj_key):
        data=JsonFile.loadData('./schemas/text_blobs.json')
        if(data!=None and data!=False and data!={}):
            return data[obj_key]
        else:
            Messages.error("Could not load data")
            return False
    @staticmethod
    def nested_list(number):
        l=List.fetch_lists("nested_lists")
        if(l!=False):
            return l[0:number]
    @staticmethod
    def simple_list(number):
        l=List.fetch_lists("list")
        if(l!=False):
            return l[0:number]

class Analysis:
    @staticmethod
    def max_numberUniqUsers():
        users=JsonFile.loadData("schemas/users_schema.json")
        maleFirst=len(users["male"][0]["first"])
        maleLast=len(users["male"][1]["last"])
        maxNumMale=maleFirst*maleLast
        femaleFirst=len(users["female"][0]["first"])
        femaleLast=len(users["female"][1]["last"])
        maxNumFemale=femaleFirst*femaleLast
        maxUniqEmails=(maxNumMale+maxNumFemale)*len(users["emails"])
        #Messages.success("Number of uniq male names {n}".format(n=maxNumMale))
        #Messages.success("Number of uniq femamale names {n}".format(n=maxNumFemale))
        #Messages.success("Number of uniq emails {n}".format(n=maxUniqEmails))
        return {"male":maxNumMale,"female":maxNumFemale,"emails":maxUniqEmails}
if __name__=="__main__":
    #data=User.random_users(2)
    #User.export_data(data)
    #print(UserReview.random_reviews(100))
    #print(Products.getProductsInCategory("fashion"))
    #print(Products.genRandomProductList())
    #print(Products.getAllProductList())
    #Analysis.max_numberUniqUsers()
    pass