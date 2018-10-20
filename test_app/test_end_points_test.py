import unittest

import json

from application.end_points import app

import pytest
@pytest.fixture()
def client():
    test_client = app.test_client()
    return test_client
"""
def startUp(self):
    self.client = app.test_client()
    return test_client
    """
class  TestClass:   
    def test_get_Allproduct(self, client):
        response = client.get('/api/v1/products')
        assert response.status_code == 201    

    def test_create_product(self, client):
        response = client.get('/api/v1/products/1')
        assert response.status_code == 201
    def test_create_product(self, client):  
        response = client.post('/api/v1/products', content_type="application/json", data=json.dumps
        ({
         "name": "phones, computers",
         "quantity_avaliable": "122 boxes",
         "category": "computer",
         "price": 2000,
        "done": "False"
        })
        ) 
        assert response.status_code == 201

    def test_get_sales(self, client): 
        response = client.get('/api/v1/sales')
        assert response.status_code == 200    

    def test_get_a_sales(self, client):
        response = client.get('/api/v1/sales/1')
        assert response.status_code == 200    

    def test_create_sale(self, client):
        response = client.post('/api/v1/sales',  content_type="application/json", data=json.dumps
        ({
         "name": "phones, computers",
         "category": "computer",
         "price": 2000,
         "sold_by": "Mule santos", 
         "done": "False"
        })
        ) 
        assert response.status_code == 201     

               
