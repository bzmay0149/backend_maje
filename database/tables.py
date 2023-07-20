from database.connection import create_connection
import mysql.connector
from errno import errorcode

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
