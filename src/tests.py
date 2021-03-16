"""
Tests
"""
import unittest
from entities import *
from gen import *

class EntitiesTest(unittest.TestCase):
#user entity    
    def test_user(self):
        u=User()
        user=u.gen_fulluser()
        Messages.success("\nPrinting generated user \n {l}\n".format(l=str(user)))
        self.assertNotEqual(user,None)
        self.assertEqual(type(user),type({}))
#location entity
    def test_location(self):
        l=Location()
        addr=l.gen_address()
        cord=l.gen_cordinates()
        Messages.success("\nPrinting generated address \n {l}\n".format(l=str(addr)))
        Messages.success("\nPrinting generated coordinates \n {l}\n".format(l=str(cord)))
        self.assertEqual(type(addr),str)
        self.assertEqual(type(cord),type({}))
#product
    def test_product(self):
        p=Product()
        full_prod=p.gen_fullProduct()
        prod_reviews=p.gen_productReviews(3)
        Messages.success("\nPrinting generated full product {l} \n".format(l=str(full_prod)))
        self.assertEqual(len(prod_reviews),3)
#texb blob    
    def test_textBlob(self):
        tB=TextBlob()
        lP=tB.gen_paragraph(size="l")
        sP=tB.gen_paragraph(size="s")
        mP=tB.gen_paragraph(size="m")
        noParams=tB.gen_paragraph()
        upperCaseParam=tB.gen_paragraph(size="L")
        paragraphs=[lP,sP,mP,noParams,upperCaseParam]
        for par in paragraphs:
            self.assertEqual(type(par),type({}))
            self.assertGreater(len(par),0)
        lists=tB.gen_List(l=2)
        #Messages.success("Printing generated list {l}".format(l=str(lists)))
        #self.assertNotEqual(len(lists),0)
        self.assertGreater(len(lists),0)

class GenTest(unittest.TestCase):
#User Generation
    def test_randomUserGeneration(self):
        users=UserGen.random_users(10)
        self.assertEqual(len(users),10)

    def test_radomUserProfileGeneration(self):
        users=UserGen.random_users_profiles(10)
        self.assertEqual(len(users),10)

    def test_random_user_login_cred(self):
        users=UserGen.random_users_login_cred(10)
        self.assertEqual(len(users),10)
    
    def test_random_user_reviews(self):
        users=UserGen.gen_user_reviews(10)
        #Messages.success("\nPrinting generated reviews\n {l} \n".format(l=str(users)))
        self.assertEqual(len(users),10)

if __name__=="__main__":
    unittest.main()
