"# StoreManager" 
 #API endpoints
 
 [![Build Status](https://travis-ci.org/RonaldMule/StoreManager.io.svg?branch=master)](https://travis-ci.org/RonaldMule/StoreManager.io)



 ##Required Features
~~~

    1. Store attendant can search and add products to buyer’s cart.
    2. Store attendant can see his/her sale records but can’t modify them.
    3. App should show available products, quantity and price.
    4. Store owner can see sales and can filter by attendants.
    5. Store owner can add, modify and delete products.
~~~ 
##Tools
~~~   

    • Server-Side Framework: <Flask Python Framework>
    • Linting Library: <Pylint, a Python Linting Library>
        • Style Guide: <PEP8 Style Guide>
    • Testing Framework: <PyTest, a Python Testing Framework>
 ~~~ 

|EndPoint                     |    Functionality                |        Notes           |
|-----------------------------|---------------------------------|------------------------|
|GET /products                | Fetch all products              |Get all available products.|
|GET /products/<productId>    |Fetch a single product record    | Get a specific product using the product’s id.|
|GET /sales                   |Fetch all sale records           |Get all sale records. This endpoint should be accessible to only the store owner/admin.|
|GET /sales/<saleId>          | Fetch a single sale record      | Get a specific sale record using the  
|      POST/PODUCTS           | Create a product                | Create a new product record.This point should be accessible to only the store owner/admin | 
 POST /sales                 | Create a sale order         | Create a sale record. This endpoint is accessible to only the store attendant.|

















