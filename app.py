from flask import Flask
from database.connect_db import create_connection
from models.create_table import create_tables
def create_app():
    app=Flask(__name__) 
    return app

app = create_app()




create_tables()



if __name__=="__main__":
    app.run(debug=True)