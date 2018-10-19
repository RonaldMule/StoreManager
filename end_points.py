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

@app.route('/api/v1/products/<int:productId>', methods = ['GET'])
""" geting a single product """
def get_product(productId):
  product = [product_item for product_item in products if product_item['id'] == productId ]
  return jsonify({'product_item': product[0]}) 



if __name__ == '__main__':
    app.run(debug=True)