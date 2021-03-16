"""
Tests
"""
import unittest
from entities import *
from gen import *

class EntitiesTest(unittest.TestCase):
    def test_user(self):
        u=User()
        user=u.gen_fulluser()
        Messages.success("\nPrinting generated user \n {l}\n".format(l=str(user)))
        self.assertNotEqual(user,None)
        self.assertEqual(type(user),type({}))

    def test_location(self):
        l=Location()
        addr=l.gen_address()
        cord=l.gen_cordinates()
        Messages.success("\nPrinting generated address \n {l}\n".format(l=str(addr)))
        Messages.success("\nPrinting generated coordinates \n {l}\n".format(l=str(cord)))
        self.assertEqual(type(addr),type({}))
        self.assertEqual(type(cord),type({}))

    def test_product(self):
        p=Product()
        full_prod=p.gen_fullProduct()
        prod_reviews=p.gen_productReviews(3)
        Messages.success("\nPrinting generated full product {l} \n".format(l=str(full_prod)))
        self.assertEqual(len(prod_reviews),3)
    
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
            self.assertNotEqual(par,None)
        lists=tB.gen_List(l=2)
        Messages.success("Printing generated list {l}".format(l=str(lists)))
        self.assertNotEqual(len(lists),0)

#code base tests
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

"""#Users Reviews
    def test_randomReviews(self):
        userReviews=UserReview.random_reviews(10)
        self.assertEqual(len(userReviews),10)
#Blogs
    def test_randomBlog(self):
        blog=Blogs.randomBlog()
        self.assertEqual(len(blog),9)
    def test_blogSnippets(self):
        blogSnippets=Blogs.blogSnippets(1)
        self.assertEqual(len(blogSnippets),1)
#lists
    def test_nestedList(self):
        l=List.nested_list(3)
        self.assertEqual(len(l),3)
    def test_simpleList(self):
        l=List.simple_list(3)
        self.assertEqual(len(l),3)
#products
    def test_products(self):
        specificPrdct=Products.getProductsInCategory("fashion")
        randomPrdct=Products.genRandomProductList()
        allPrdct=Products.getAllProductList()
        self.assertIsNotNone(specificPrdct)
        self.assertIsNotNone(randomPrdct)
        self.assertIsNotNone(allPrdct)

"""
class MyDBTest:
    pass

class ModelsTest:
    pass

class RequestTest:
    pass

class UtilityTest:
    pass

#resources
class SchemaTest:
    pass

class GenericDataTest:
    pass

if __name__=="__main__":
    unittest.main()
