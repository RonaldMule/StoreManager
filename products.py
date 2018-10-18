from flask import Flask, jsonify, request, abort

app = Flask(__name__)

products = [
    {
        'id':1,
       
        'name': u'phones, computers',
        'quantity avaliable': u'122 boxes',
        'category': u'computer',
        'price': u'2000',
        'done': False
    },
    {
      'id':1,
      'name': u'phones, computers',
      'quantity avaliable': u'122 boxes',
      'category': u'computer',
      'price': u'12000, 30000,182900',
      'done': False  
    }
    
]

@app.route('/api/v1.0/products', methods = ['GET'])
def get_Allproduct():
    return jsonify({'product': products})

#geting a single product
@app.route('/api/v1.0/products/<productId>', methods = ['GET'])
def get_product(productId):
  product = [product_item for product_item in products if product_item['productId'] == id]
  return jsonify({'product_item': product[0]}) 


#allowing admin to post products
@app.route('/api/v1.0/products', methods = ['POST'])
def creat_product():
    product = {
            'id': products[-1]['id'] +1,
            'name': request.json['name'],
            'quantity avaliable':request.json['quantity avaliable'],
            'category':request.json['category'],
            'price': request.json['price'],
            'done': False
    }  
    products.append(product) 
    return jsonify({'product': product}), 201 
   

   

if __name__ == '__main__':
    app.run(debug=True)
