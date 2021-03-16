import os
from random import randrange
from utils import JsonFile,Messages,RandomFigures

class User:
    def __init__(self):
        self.user_schema_path="./schemas/users_schema.json"
        self.dataset=JsonFile.loadData(self.user_schema_path)

    def gen_username(self):
        g=randrange(0,2)
        genders={0:"male",1:"female"}
        fNameSize=len(self.dataset[genders[g]][0]["first"])#-1
        lNameSize=len(self.dataset[genders[g]][1]["last"])#-1
        f_name=self.dataset[genders[g]][0]["first"][randrange(0,fNameSize)]["name"]
        l_name=self.dataset[genders[g]][1]["last"][randrange(0,lNameSize)]["name"]
        return f_name,l_name

    def gen_fulluser(self):
        f_name,l_name=self.gen_username()
        user={
            "username":"{f} {l}".format(f=f_name,l=l_name),
            "firstname":f_name,"lastname":l_name,
            "email":self.gen_email(f_name,l_name),
            "age":self.gen_age(),
            "password":self.gen_pass(8),
            "phone":self.gen_phone(10),
            "profile_pic":self.gen_profile(),
        }
        return user
    
    def gen_userLogin(self):
        u=self.gen_fulluser()
        return {
            "username":u["username"],
            "email":u["email"],
            "password":u["password"]
        }

    def gen_userProfile(self):
        u=self.gen_fulluser()
        return {
            "profile_pic":u["profile_pic"],
            "addess":self.gen_address(),
            "phone":u["phone"],
            "age":u["age"],
            "email":u["email"]
        }

    def gen_userReview(self):
        reviews=JsonFile.loadData("./schemas/reviews.json")
        u=self.gen_userProfile()
        posOrNeg=randrange(0,2)
        r=reviews["reviews"][posOrNeg]["users_reviews"]
        review=r[randrange(len(r))]
        return {
            "user":u,
            "review":review
        }

    def gen_pass(self,size):
        password=None
        characters=JsonFile.fetchField('schemas/users_schema.json','charcters')
        if(characters!=False):
            alpha=characters[0]["alpha"][0:randrange(0,len(characters[0]["alpha"]))]
            numbers=characters[1]["numbers"][0:randrange(0,len(characters[1]["numbers"]))]
            special=characters[2]["special"][0:randrange(len(characters[2]["special"]))]
            password=alpha+str(numbers)+special
        else:
            print("Error getting characters for passwords")
            print(characters)
            password=False
        return password

    def gen_email(self,f_name,l_name):
        domains=self.dataset["emails"]
        email=None
        if(domains!=False):
            d=domains[randrange(0,len(domains))]["domain"]
            email=f_name.lower()+l_name.lower()+d
            return email
        else:
            email=False
        return email
    
    def gen_phone(self,size):
        phone=""
        for i in range(size):
            phone+=(str(randrange(0,10)))
        phone="+"+str(phone)
        return phone
    
    def gen_age(self):
        return randrange(0,100)

    def gen_profile(self):
        profiles=os.listdir('./static/images/profiles/')
        rand_profile=randrange(0,len(profiles))
        return "/static/images/profiles/{i}".format(i=profiles[rand_profile])

    def gen_address(self):
        l=Location()
        return l.gen_address()

class Location:
    def __init__(self):
        pass
    
    def gen_address(self):
        self.data=JsonFile.loadData("./schemas/users_schema.json")
        addresses=self.data["address"]
        street=addresses[0]["streets"][randrange(0,len(addresses[0]["streets"]))]
        building=addresses[1]["building"][randrange(0,len(addresses[1]["building"]))]
        city=addresses[2]["city"][randrange(0,len(addresses[2]["city"]))]
        return "{b},{s},{c}".format(b=building,c=city,s=street)
    
    def gen_cordinates(self):
        x=randrange(0,3600)
        y=randrange(0,3600)
        Messages.warning("Location.gencordinates not complete")
        return {"longitude":float(x/100),"latitide":y/100}

class Product:
    def __init__(self):
        self.dataset=JsonFile.loadData("./schemas/reviews.json")
        self.productsList=JsonFile.loadData("./schemas/products.json")
    
    def gen_ProductName(self):
        return self.productsList[0]["names"][randrange(0,len(self.productsList[0]["names"]))]

    def gen_fullProduct(self):
        num_reviews=RandomFigures.randomFigure(0,5)
        product={
            "name":self.gen_ProductName(),
            "price":RandomFigures.randomFigure(1,300),
            "weight":RandomFigures.randomFigure(1,200),
            "numReviews":num_reviews,
            "reviews":self.gen_productReviews(num_reviews),
            "shipping":RandomFigures.randomFigure(10,100),
        }
        return product

    def gen_productReviews(self,number):
        reviews=[]
        u=User()
        for i in range(number):
            reviews+=[u.gen_userReview()]
        ##push reviews to array
        return reviews

class TextBlob:
    def __init__(self):
        self.data=JsonFile.loadData("./schemas/text_blobs.json")
    
    def gen_paragraph(self,size="m"):
        par={};dataset=[]
        size=size.lower()
        if(size=="m"):
            dataset=self.data["medium_par"]
        elif(size=="s"):
            dataset=self.data["short_par"]
        elif(size=="l"):
            dataset=self.data["long_par"]
        par=dataset[randrange(len(dataset))]
        return par

    def gen_List(self,l=10):
        list_data=JsonFile.loadData("./schemas/lists.json")
        countries=list_data[0]
        continents=list_data[1]
        pLanguages=list_data[2]
        lists=[continents,pLanguages,countries]
        for indexList in lists:
            if(l<len(indexList["list"])):
                return indexList["list"][0:l]
        #Messages.warning("Radomize the gen_List method")
        #return list_data["list"][0:l]

class Blog:
    def __init__(self):
        pass
    def random_Blog(self,paragraphs=10,reviews=10):
        par=[]
        sizes=['s','m','l']
        t=TextBlob()
        while paragraphs>0:
            r=randrange(0,len(sizes))
            par+=[t.gen_paragraph(sizes[r])]
            paragraphs-=1
        user=User()
        user_reviews=[]
        while(reviews>0):
            user_reviews+=[user.gen_userReview()]
            reviews-=1
        fname,lname=user.gen_username()
        return {
            "author":"{f} {l}".format(f=fname,l=lname),
            "published":"{dd}/{mm}/{yyyy}".format(dd=randrange(1,29),mm=randrange(1,13),yyyy=randrange(1992,2100)),
            "title":par[0]["title"],
            "paragraphs":par,
            "reviews":user_reviews,
            "likes":randrange(0,1000),
            "dislikes":randrange(0,100),
        }
        
if __name__=="__main__":
    #u=User()
    #print(u.gen_fulluser())
    #p=Product()
    #print(p.gen_fullProduct())
    b=Blog()
    print(b.random_Blog(10,10))