from flask import Flask
from database.connect_db import create_connection
def create_app():
    app=Flask(__name__) 
    return app

app = create_app()

create_connection()




if __name__=="__main__":
    app.run(debug=True)