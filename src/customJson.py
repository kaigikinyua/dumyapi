import re
import sys
from entities import User,Product,TextBlob,Blog
class CustomJson:
    def __init__(self,datastring):
        self.datastring=datastring

    def populateJson():
        arrays=Parser.filterArrays(self.datastring)
        objects=Parser.filterObjects(self.datastring)
        datastringreplacements=[]
        for arr in arrays:
            var=arr.split('...')
            rep=Parser.expandVariables(var[1])
            datastringreplacements+=[{"variable":arr,"rep":rep}]
        for obj in objects:
            var=obj.split(":")
            rep=Parser.expandVariable(var[1])
            datastringreplacements+=[{"variable":obj,"rep":"{k}:{v}".format(k=var[0],v=rep)}]
        return Parser.compileString(self.datastring,datastringreplacements)

class Parser:
    @staticmethod
    def filterArrays(datastring):
        return re.findall('\.\.\.[\w\d]*',datastring)
    @staticmethod
    def filterObjects(datastring):
        return re.findall("['\w]+:[\w]+")
    @staticmethod
    def expandVariable(variable):
        exp=None
        if(variable=='username'):
            u=User()
            exp=u.gen_username()
        elif(variable=='firstname'):

    @staticmethod
    def compileString(datastring,replacements):
        rString=datastring
        for replacement in replacements:
            x=re.sub(replacement["variable"],replacement["rep"])
            rString=x
        return rString

class Variables:
    #number [price,cords]
    #images: [profilepic,thumbnail,productimage]
    #user: [username,firstname,lastname,email,password,age]
    #textblob: [paragraph,title]
    #product: [productname,review]
    @staticmethod
    def categorize(variable):
        variables={
            "number":["price","cords"],
            "images":["profilepic","thumbnail","productimage"],
            "user":["username","firstname","lastname","email","password","age"]
            "textblob":["paragraph","title"],
            "product":["productname","review"]
            }
        for v in variables:
            print(v)

if __name__=="__main__":
    print(sys.argv)
    Variables.categorize("name")

