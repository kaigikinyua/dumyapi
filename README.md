# Dummy Data Generator

![Screenshot](./assets/dummy_logo_64x64.png)

## What is it?

Well it's in the name. Get random dummy data to your front end without 
the need of putting together a backend. A little json data is enough.

## Data Provided.
The dummy api provides a selected variety of dummy data to help you develop a ui prototype 
fast and easy.

*   Dummy User [Email ,First and lastname ,Phone ,Password ,Profile Picture]

*   Dummy Reviews [Username ,Review ,Time review posted ,Likes & Dislikes]

*   Dummy Products [Product name ,Price ,1 Picture ,Weight ,Shipping Cost]

*   Dummy Blog Posts [Author ,Date published ,Likes ,Dislikes ,Views ,Blog Title ,Blog body]

## Dummy Data Language (DDL)

    The DDL is a simple language that enables you to generate random data from a json like syntax.
    Since most developers have json syntax at their fingertips it is much easy to use and it offers more flexibility than the generic data provided.

### General Syntax

*   {'dummy_username':username} - Enables you to get an object which has a key by 'dummy_username' and the value of a       username. Note username without single quotes is a ddl variable

*   {'dummy_product_list':[ 'name':productName,'price':int...10]}. This will return an array of 10 objects{'name':'pname',    'price':100} and the key of this array will be 'dummy_product_list'

*   {'dummy_users':[ username...10]}. The response for this will be a list of usernames whose key is 'dummy_user'

### DDL Variables
1.  User Related variables -> [ userName,firstName,lastName,phoneNumber,email,password,profilePic,addr]
2.  Product Related variables -> [ productName,review,productImage]
3.  Text Related variables -> [ title,par]