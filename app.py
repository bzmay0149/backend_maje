from flask import Flask
from flask_cors import CORS
from routes.customers import customers_bp
from routes.users import users_bp

app = Flask(__name__)
app.secret_key = "kishirika"
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

app.register_blueprint(customers_bp)
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)
