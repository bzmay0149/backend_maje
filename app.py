from flask import Flask, request,jsonify
from errno import errorcode
import mysql.connector
import jwt
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
#coneccion a la base de datos

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="containers-us-west-79.railway.app",
            user="root",
            password="LxKHUTWgbrFrgyYW7gvq",
            database="railway",
            port="6899"
            # host="localhost",
            # user="root",
            # password="admin",
            # database="zurtek",
            # port="3306"
        )
        print("Connection established")
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

# creacion de las tables 
def create_tables():
    try:
        con = create_connection()
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS users (
            iduser INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )''')

        cur.execute('''CREATE TABLE IF NOT EXISTS customers (
            idcustomer INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            lastname VARCHAR(255),
            phone VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            address VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            province VARCHAR(255),
            postal_code INT,
            budget ENUM('yes','no') NOT NULL,
            accepted_budget ENUM('yes','no') NOT NULL,
            term DATETIME NOT NULL,
            done ENUM('yes','no') NOT NULL,
            invoiced ENUM('yes','no') NOT NULL
        )''')

        con.commit()
        
        print("Tables created successfully.")
    except Exception as e:
        print("Error creating tables:", str(e))
    finally:
        
            con.close()

# creacion de endpoint
@app.route('/add', methods=['POST'])
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
        postal_code = postman['postal_code']
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


#mostrando todos los clientes de forma desediente 
@app.route('/', methods=['GET'])
def get_customers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT *FROM customers ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)


#mostrar todos los clientes por budget enviado y de forma desediente 
@app.route('/budget/yes', methods=['GET'])
def get_customers_by_budget():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE budget = 'yes' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)

#mostrar todos los clientes por budget no enviado  y de forma desediente 
@app.route('/budget/no', methods=['GET'])
def get_customers_by_budget_no():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE budget = 'no' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)


#mostrar todos los clientes por budget aceptado  y de forma desediente
@app.route('/budget/aceptado/yes', methods=['GET'])
def get_customers_by_budget_send_yes():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE accepted_budget = 'yes' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)

#mostrar todos los clientes por budget no aceptado   y de forma desediente
 
@app.route('/budget/aceptado/no', methods=['GET'])
def get_customers_by_budget_send_no():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE accepted_budget = 'no' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)

#mostrad todos los cliente facturados 

@app.route('/facturado/yes', methods=['GET'])
def get_customers_by_invoiced():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE invoiced = 'yes' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)

#mostrar todos los clientes no facturados 
@app.route('/facturado/no', methods=['GET'])
def get_customers_by_invoiced_no():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE invoiced = 'no' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)

#mostrar todos los cliente por 

@app.route('/finalizado', methods=['GET'])
def get_customers_by_done():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE done = 'yes' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)

#mostrar todos los clientes no finaizados
@app.route('/finalizado/no', methods=['GET'])
def get_customers_by_done_no():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE done = 'no' ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    data = [{"name ":row[1],
             "lastname ":row[2],
             "phone ":row[3],
             "email ":row[4],
             "address ": row[5],
             "city " : row[6],
             "province " : row[7],
             "postal_code " : row[8],
             "budget ": row[9],
             "accepted_budget ":row[10],
             "done ":row[11],
             "invoiced " :row[12],
             "date " :row[13]}
            for row in data_cunstomers]
    return jsonify(data)


#crear usuario con jwt
@app.route('/user', methods=['POST'])
def adduser():
    try:
        data_postman = request.get_json()
    
        username = data_postman['username']
        password = data_postman['password']
        print (username)
        print (password)
        app.secret_key = "kishirika"
        
        payload = {
            'password': password
        }
        
        password_encode = jwt.encode(payload, app.secret_key, algorithm='HS256')
        print (password_encode)
        
        con = create_connection()
        cur = con.cursor()
        
        cur.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password_encode))
        con.commit()
        con.close()
        return jsonify({'message': 'Usuario creado correctamente'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
    
from flask import jsonify

@app.route('/login', methods=['POST'])
def login():
  
        username = request.json.get('username')
        password = request.json.get('password')
        
        print(username)
        print(password)
        return jsonify({'message': 'Usuario creado correctamente'}), 201


if __name__ == '__main__':
    app.run(debug=True)
    
    
                                                                                                                                    