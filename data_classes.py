class User:
    def __init__(self):
        self.user_schema_path="schemas/users_schema.json"
        self.dataset=JsonFile.loadData(self.user_schema_path)

    def gen_fulluser(self):
        fNameSize=len(self.dataset[0]["first"])#-1
        lNameSize=len(self.dataset[1]["last"])#-1
        f_name=dataset[0]["first"][randrange(0,fNameSize)]["name"]
        l_name=dataset[1]["last"][randrange(0,lNameSize)]["name"]
        user={
            "username":"{f} {l}".format(f=f_name,l=l_name),
            "firstname":f_name,"lastname":l_name,
            "email":self.gen_email(f_name,l_name),
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

"""   
    def random_users(self,number):
        uData=JsonFile.loadData("schemas/users_schema.json")
        male_names=uData["male"]
        female_names=uData["female"]
        Gen_Users=[]
        if(uData!=False and uData!={}): 
            for i in range(number):
                rand_gender=randrange(0,3)
                if(rand_gender==0):
                    user=User.gen_fulluser(male_names)
                else:
                    user=User.gen_fulluser(female_names)
                Gen_Users.append(user)
        else:
            print("Error while getting usernames and domains from ./schemas/users_schema.json")
            Messages.warning("Got {d} while loading user schema ".format(d=uData))
            Gen_Users=False
        return Gen_Users
    
    
    def random_users_profiles(self,number):
        rusers=User.random_users(number)
        rusersprofiles=[]
        if(rusers!=False):
            for user in rusers:
                rusersprofiles+=[
                    {
                        "firsname":user["firstname"],
                        "lastname":user["lastname"],
                        "email":user["email"],
                        "profile":"/images/one.png"
                    }
                ]
        return rusersprofiles

    
    def export_data(self,data):
        f=JsonFile.exportJson(filepath="./genericdata/users.json",data=data)
        if(f==False):
            Messages.error(message="Could not export users data to ./genericdata/users.json",log=True)
            Messages.error(message="Userdata -> {d}".format(d=data))
            return False
        else:
            return True
"""