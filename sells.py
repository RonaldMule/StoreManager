
from flask import Flask, jsonify, request

app = Flask(__name__)

sales = [
    {
        'id':1,
        'Name': u'phones',
        'category': u'computer',
        'price': u'30000',
        'Sold By': u'Ronald Mulyowa',
        'done': False
    },
    {
         
        'id':2,
        'Name': u'phones',
        'category': u'computer',
        'price': u'30000',
        'Sold By': u'Ronald Mulyowa',
        'done': False
    
    }
    
]
#fetch all sells records
@app.route('/api/v1.0/sales', methods = ['GET'])
def get_sells():
    return jsonify({'sales': sales})


#fetch a single sale record
@app.route('/api/v1.0/sales/<saleId>', methods = ['GET'])
def get_task(task_id):
    sale = [sold_item for sold_item in sales if sold_item['sellId'] == id]
    return jsonify({'product_item': sale[0]})


#Creating a sale order
@app.route('/StoreManage/api/v1.0/sales', methods = ['POST'])
def creat_sale():
    cart = {
            'id': sales[-1]['id'] +1,
            'name': request.json['name'],
            'category':request.json['category'],
            'price': request.json['price'],
            'sold by': request.json['sold by'], 
            'done': False
    }  
    sales.append(cart) 
    return jsonify({'cart': cart}), 201 


if __name__ == '__main__':
    app.run(debug=True)
