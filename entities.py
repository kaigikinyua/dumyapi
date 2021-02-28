from random import randrange
from utils import JsonFile,Messages,RandomFigures
class User:
    def __init__(self):
        self.user_schema_path="./schemas/users_schema.json"
        self.dataset=JsonFile.loadData(self.user_schema_path)
    
    def gen_fulluser(self):
        g=randrange(0,2)
        genders={0:"male",1:"female"}

        fNameSize=len(self.dataset[genders[g]][0]["first"])#-1
        lNameSize=len(self.dataset[genders[g]][1]["last"])#-1
        f_name=self.dataset[genders[g]][0]["first"][randrange(0,fNameSize)]["name"]
        l_name=self.dataset[genders[g]][1]["last"][randrange(0,lNameSize)]["name"]
        user={
            "username":"{f} {l}".format(f=f_name,l=l_name),
            "firstname":f_name,"lastname":l_name,
            "email":self.gen_email(f_name,l_name),
            "age":self.gen_age(),
            "password":self.gen_pass(8),
            "phone":self.gen_phone(10),
            "profile":self.gen_profile(),
        }
        return user
    
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
        return "not yet implemented"

    def gen_address(self):
        return "not yet implemented"

class Location:
    def __init__(self):
        pass
    
    def gen_address(self):
        self.data=JsonFile.loadData("./schemas/users_schema.json")
        addresses=self.data["address"]
        street=addresses[0]["streets"][randrange(0,len(addresses[0]["streets"]))]
        building=addresses[1]["building"][randrange(0,len(addresses[1]["building"]))]
        city=addresses[2]["city"][randrange(0,len(addresses[2]["city"]))]
        return {"building":building,"street":street,"city":city}
    
    def gen_cordinates(self):
        x=randrange(0,3600)
        y=randrange(0,3600)
        Messages.warning("Location.gencordinates not complete")
        return {"longitude":float(x/100),"latitide":y/100}

class Product:
    def __init__(self):
        self.dataset=JsonFile.loadData("./schemas/reviews.json")
    def gen_fullProduct(self):
        num_reviews=RandomFigures.randomFigure(0,5)
        product={
            "name":"Random Product",
            "price":RandomFigures.randomFigure(1,300),
            "weight":RandomFigures.randomFigure(1,200),
            "numReviews":num_reviews,
            "reviews":self.gen_productReviews(num_reviews),
            "shipping":RandomFigures.randomFigure(10,100),
        }
        return product
    def gen_productReviews(self,number):
        reviews=[]
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
        return self.data["list"]

if __name__=="__main__":
    #u=User()
    #print(u.gen_fulluser())
    p=Product()
    print(p.gen_fullProduct())