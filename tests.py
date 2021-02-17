"""
Tests
"""
import unittest
from gen import *
    
#code base tests
class GenTest(unittest.TestCase):
#User Generation
    def test_randomUserGeneration(self):
        users=User.random_users(10)
        self.assertEqual(len(users),10)

    def test_radomUserProfileGeneration(self):
        users=User.random_users_profiles(10)
        self.assertEqual(len(users),10)
#Users Reviews
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
