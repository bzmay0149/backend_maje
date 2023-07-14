from database.connect_db import create_connection
from flask import request

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
        postalcode = postman['postalcode']
        budget = postman['budget']
        accepted_budget = postman['accepted_budget']
        term = postman['term']
        done = postman['done']
        invoiced = postman['invoiced']
        date = postman['date']
        
        cur.execute("INSERT INTO client (name, lastname, phone, email, address, city, province, postalcode, budget, accepted_budget, term, done, invoiced, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, lastname, phone, email, address, city, province, postalcode, budget, accepted_budget, term, done, invoiced, date))
        con.commit()
        con.close()
        return {'message': 'Client added successfully'}, 201
    
    except Exception as e:
        print(e)
        con.close()
        return {'message': 'Error adding client'}, 500
  

        
    



    