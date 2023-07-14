from flask import Flask, request
from database.connect_db import create_connection
from models.queries import add_cliente
from routes.post import *

app = Flask(__name__)


@app.route('/', methods=['POST'])
def add_cliente():
    try:
        con = create_connection()
        cur = con.cursor()
        
        postman = request.get_json()
        
        name = postman['name']
        lastname = postman['lastname']
        phone = postman['phone']
        email = postman['email']
        address = postman[ 'address']
        city = postman['city']
        province = postman['province']
        postal_code = postman['postalcode']
        budget = postman['budget']
        accepted_budget = postman['accepted_budget']
        done = postman['done']
        invoiced = postman['invoiced']
        date = postman['date']
        
        cur.execute("INSERT INTO customers (name, lastname, phone, email, address, city, province, postal_code, budget, accepted_budget,  done, invoiced, date) VALUES (%s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, lastname, phone, email, address, city, province, postal_code, budget, accepted_budget, done, invoiced, date))
        con.commit()
        con.close()
        return {'message': 'Client added successfully'}, 201
    
    except Exception as e:
        print(e)
        con.close()
        return {'message': 'Error adding client'}, 500
        print(e)
    pass

   
if __name__ == '__main__':
    app.run(debug=True)