"""
Various actions that can be processed by the backend
Serialization of data to be consumed by user requests
"""
import os
from utils import JsonFile,Messages
from gen import User,UserReview,Blogs,List
from mydb import UserDataBase
class GenericData:
    @staticmethod
    def listGenericDataFiles():
        raw_files=os.listdir("./static/genericdata/")
        files=[]
        for f in raw_files:
            x=f.split(".")
            files+=[x[0]]
        return files
    @staticmethod
    def genericDataActions(action,number):
        if(action=="show"):
            return GenericData.show()
        elif(action=="users"):
            return GenericData.users(number)
        elif(action=="userprofiles"):
            return GenericData.users_profiles(number)
        elif(action=="reviews"):
            return GenericData.usersReviews(number)
        elif(action=="bloglist"):
            return GenericData.bloglist(number)
        elif(action=="blog"):
            return GenericData.randomBlog()
        elif(action=="list"):
            return GenericData.noramlList(number)
        elif(action=="nestedlist"):
            return GenericData.nestedList(number)
        elif(action=="chat"):
            pass
        else:
            Messages.error("Unknown generic data {d}".format(d=action),log=True)
            return None

    @staticmethod
    def show():
        files=os.listdir("./genericdata")
        files_cleaned=[]
        for f in files:
            files_cleaned+=[f.split(".")[0]]
        return files_cleaned

    @staticmethod
    def users(number):
        users=JsonFile.loadData("./genericdata/users.json")
        if(users!={} and users!=False):
            return users
        else:
            return User.random_users(number)

    @staticmethod
    def users_profiles(number):
        #add local storage for users profile
        return User.random_users_profiles(number)

    @staticmethod
    def usersReviews(number):
        return UserReview.random_reviews(number)
    @staticmethod
    def bloglist(number):
        return Blogs.blogSnippets(number)
    @staticmethod
    def randomBlog():
        return Blogs.randomBlog()
    @staticmethod
    def nestedList(number):
        return List.nested_list(number)
    @staticmethod
    def noramlList(number):
        return List.simple_list(number)

class MyDBActions:
    @staticmethod
    def createDB(dbname):
        pass
    @staticmethod
    def populateDB(dbname):
        pass
    @staticmethod
    def fetchData(database):
        pass
    @staticmethod
    def userDBConfgs(configs):
        pass