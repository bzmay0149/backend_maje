import mysql.connector
from errno import errorcode

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="containers-us-west-79.railway.app",
            user="root",
            password="LxKHUTWgbrFrgyYW7gvq",
            database="railway",
            port="6899"
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
