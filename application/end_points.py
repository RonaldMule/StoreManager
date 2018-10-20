from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {
        'id':1,
       
        'name': 'phones, computers',
        'quantity avaliable': '122 boxes',
        'category': 'computer',
        'price': 2000
      
    },
    {
      'id':1,
      'name': 'phones, computers',
      'quantity_avaliable': '122 boxes',
      'category': 'computer',
      'price': 12000
     
    }
    
]

sales = [
    {
        'id':1,
        'Name': 'phones',
        'category': 'computer',
        'price': 30000,
        'Sold By': 'Ronald Mulyowa'
        
    },
    {
         
        'id':2,
        'Name': 'phones',
        'category': 'computer',
        'price': 30000,
        'Sold By': 'Ronald Mulyowa'
       
    
    }
    
]

@app.route('/api/v1/products', methods = ['GET'])
def get_Allproduct():
    return jsonify({'product': products}), 201
       

@app.route('/api/v1/products/<int:productId>', methods = ['GET'])
#""" [geting a single product] """
def get_product(productId):
    product = [product_item for product_item in products if product_item['id'] == productId ]
    return jsonify({'product_item': product[0]}), 201 

@app.route('/api/v1/products', methods = ['POST'])
def create_product():
    """allowing admin to post products"""
    product = {
            'id': products[-1]['id'] +1,
            'name': request.json['name'],
            'quantity_avaliable':request.json['quantity_avaliable'],
            'category':request.json['category'],
            'price': request.json['price']
          
    }  
    products.append(product) 
    return jsonify({'product': product}), 201 


@app.route('/api/v1/sales', methods = ['GET'])
#""" fetch all sales records """
def get_sales():
    return jsonify({'sales': sales})


@app.route('/api/v1/sales/<int:saleId>', methods = ['GET'])
#""" fetch a single sale record  """
def get_a_sale(saleId):
    sale = [sold_item for sold_item in sales if sold_item['id'] == saleId]
    return jsonify({'product_item': sale[0]})


@app.route('/api/v1/sales', methods = ['POST'])
#"""Creating a sale order"""
def create_sale():
    cart = {
            'id': sales[-1]['id'] +1,
            'name': request.json['name'],
            'category':request.json['category'],
            'price': request.json['price'],
            'sold_by': request.json['sold_by']
          
    }  
    sales.append(cart) 
    return jsonify({'cart': cart}), 201 


if __name__ == '__main__':
    app.run(debug=True)


