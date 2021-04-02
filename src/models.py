#rename to views.py

"""
Various actions that can be processed by the backend
Serialization of data to be consumed by user requests
"""
import os
from utils import JsonFile,Messages
from gen import UserGen,Blogs,List
from mydb import UserDataBase
class GenericDataConfigs:
    cacheRoot="./static/genericdata/"

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
        elif(action=="usersAuth"):
            ##add userfullprofile,userauth,userreview
            #return GenericData.usersAuth(number)
            return {"usersAuth":GenericData.fetchCache(GenericDataConfigs.cacheRoot+"user_auth.json","userAuth",number)}
        elif(action=="userProfiles"):
            #return GenericData.usersProfiles(number)
            return {"usersProfiles":GenericData.fetchCache(GenericDataConfigs.cacheRoot+"user_profiles.json","profiles",number)}

        elif(action=='fullproduct'):
            pass

        elif(action=='productList'):
            return {"productList":GenericData.fetchCache(GenericDataConfigs.cacheRoot+"products.json","productList",number)}

        elif(action=="reviews"):
            #return GenericData.usersReviews(number)
            return {"reviews":GenericData.fetchCache(GenericDataConfigs.cacheRoot+"reviews.json","reviews",number)}
        elif(action=="bloglist"):
            #return GenericData.bloglist(number)
            return {"blogsnippets":GenericData.fetchCache(GenericDataConfigs.cacheRoot+"BlogListSnippets.json","blogSnippets",number)}

        elif(action=="blog"):
            return GenericData.randomBlog()
        elif(action=="list"):
            ##country list,and normal list
            return GenericData.noramlList(number)
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
    def fetchCache(filepath=None,key=None,number=1):
        data=JsonFile.loadData(filepath)
        if(data!=None and len(data)>0):
            if(key==None):
                return data
            else:
                if(len(data[key])<number):
                    diff=number-len(data[key])
                    data=data[key]
                    while(diff>0):
                        data+=data[0:number]
                        diff=diff-number
                    return data
                else:
                    return data[key][0:number]
        else:
            #add to logs filepath,key,number of datapoints requested
            return False

    # @staticmethod
    # def usersAuth(number):
    #     users=JsonFile.loadData("./genericdata/user_auth.json")
    #     if(users!={} and users!=False):
    #         return users["usersAuth"][0:number]
    #     else:
    #         return User.random_users(number)

    # @staticmethod
    # def usersProfiles(number):
    #     #add local storage for users profile
    #     users=JsonFile.loadData('')
    #     return User.random_users_profiles(number)

    # @staticmethod
    # def usersReviews(number):
    #     return UserReview.random_reviews(number)
    # @staticmethod
    # def bloglist(number):
    #     return Blogs.blogSnippets(number)
    # @staticmethod
    # def randomBlog():
    #     return Blogs.randomBlog()
    # @staticmethod
    # def nestedList(number):
    #     return List.nested_list(number)
    # @staticmethod
    # def noramlList(number):
    #     return List.simple_list(number)

# class MyDBActions:
#     @staticmethod
#     def createDB(dbname):
#         pass
#     @staticmethod
#     def populateDB(dbname):
#         pass
#     @staticmethod
#     def fetchData(database):
#         pass
#     @staticmethod
#     def userDBConfgs(configs):
#         pass