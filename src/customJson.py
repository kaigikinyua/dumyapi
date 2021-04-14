import re
import sys
from entities import User,Product,TextBlob,Blog
class CustomJson:
    def __init__(self,datastring):
        self.datastring=datastring

    def populateJson(self):
        arrays=Parser.filterArrays(self.datastring)
        datastringreplacements=[]
        for arr in arrays:
            var=arr.split('...')
            number=int(var[1][0:len(var[1])-1])
            arrObjects=Parser.filterObjects(arr)
            if(len(arrObjects)>0):
                rep=""
                while (number>0):
                    s="{"
                    for obj in arrObjects:
                        o=obj.split(":")
                        value=Parser.expandVariable(o[1])
                        if(obj==arrObjects[len(arrObjects)-1]):
                            s+="{k}:{v}".format(k=o[0],v=value)
                        else:
                            s+="{k}:{v},".format(k=o[0],v=value)
                    if(number==1):
                        s+="}"
                    else:
                        s+="},"
                    rep+=s
                    number=number-1
                datastringreplacements+=[{"variable":arr[1:len(arr)-1],"rep":rep}]
            else:
                rep=""
                variable=var[0][1:len(var[0])]
                while(number>0):
                    rep+=str(Parser.expandVariable(variable))
                    if(number>1):
                        rep+=","
                    number=number-1
                datastringreplacements+=[{"variable":arr[1:len(arr)-1],"rep":rep}]
        objects=Parser.filterObjects(self.datastring)
        for obj in objects:
            var=obj.split(":")
            rep=""
            rep=Parser.expandVariable(var[1])
            datastringreplacements+=[{"variable":obj,"rep":"{k}:{v}".format(k=var[0],v=rep)}]
        final_str=Parser.compileString(self.datastring,datastringreplacements)
        #return final_str
        return re.sub('"','',final_str)
class Parser:
    @staticmethod
    def filterArrays(datastring):
        #enable ddapi to 'extrapolate' array of objects ['name':$username]|<number of objects>
        return re.findall("\[[\w\d,':]*\.\.\.[\d]+\]",datastring)
    @staticmethod
    def filterObjects(datastring):
        return re.findall("['\w']+:[\w]+",datastring)
    @staticmethod
    def expandVariable(variable):
        return Variables.categorize(variable)

    @staticmethod
    def compileString(datastring,replacements):
        rString=datastring
        for replacement in replacements:
            x=re.sub(replacement["variable"],replacement["rep"],rString)
            rString=x
            #print(rString)
        return rString

class Variables:
    #Todo:-> Write tests to check * variables work
    #number [price,cords]
    #images: [profilepic,thumbnail,productimage]
    #user: [username,firstname,lastname,email,password,age]
    #textblob: [paragraph,title]
    #product: [productname,review]
    @staticmethod
    def categorize(variable):
        variables={
            "number":["int","cords"],
            "images":["profilepic","thumbnail","productimage"],
            "user":["username","firstname","lastname","email","password","age"],
            "textblob":["shortpar","longpar","title"],
            "product":["productname","review"]
            }
        categoryMenthods={
            "user":Variables.userCategory(variable)
        }
        for v in variables:
            for var in variables[v]:
                if(variable==var):
                    return categoryMenthods[v]

    @staticmethod
    def userCategory(variable):
        u=User()
        variabledata=None
        if(variable=="username"):
            f_name,lname=u.gen_username()
            variabledata="'{f} {l}'".format(f=f_name,l=lname)
        elif(variable=="firstname"):
            f_name,lname=u.gen_username()
            variabledata="'{s}'".format(s=f_name)
        elif(variable=="lastname"):
            f_name,lname=u.gen_username()
            variabledata="'{s}'".format(s=lname)
        elif(variable=="email"):
            f_name,lname=u.gen_username()
            variabledata="'{s}'".format(s=u.gen_email(f_name,lname))
        elif(variable=="password"):
            variabledata="'{s}'".format(s=u.gen_pass(8))
        else:
            pass
        return variabledata

    @staticmethod
    def numbers(variable):
        num=None
        if(variable=="int"):
            return randrange(0,10000)
        else:
            return "Unimplemented number {n}".format(n=variable)
    
    @staticmethod
    def images(variable):
        img_res=None
        if(variable=="profilepic"):
            pass
        elif(variable=="thumbnail"):
            pass
        elif(variable=="productimage"):
            pass
        else:
            pass

    @staticmethod
    def textBlob(variable):
        text=None
        if(variable=="longpar"):
            pass
        elif(variable=="shorpar"):
            pass
        elif(variable=="title"):
            pass
    @staticmethod
    def product(variable):
        product=None
        if(variable=="productname"):
            pass
        elif(variable=="review"):
            pass

if __name__=="__main__":
    #print(sys.argv)
    #print(Variables.categorize("lastname")) 
    datastring="{'firstname':firstname,'lastname':lastname,'email':email,'friends':['name':username,'email':email...2],'messages':[username...10]}"
    c=CustomJson(datastring)
    print(c.populateJson())