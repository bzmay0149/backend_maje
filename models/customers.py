from database.connection import create_connection

con = create_connection()
cur = con.cursor()

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
con.close()
