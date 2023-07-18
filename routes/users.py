from flask import Blueprint, jsonify, request
from database.connection import create_connection
from utils.jwt import encode_jwt, decode_jwt

users_bp = Blueprint('users', __name__)

@users_bp.route('/user', methods=['POST'])
def adduser():
    try:
        data_postman = request.get_json()

        username = data_postman['username']
        password = data_postman['password']

        password_encode = encode_jwt(password)
        con = create_connection()
        cur = con.cursor()

        cur.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password_encode))
        con.commit()
        con.close()
        return jsonify({'message': 'Usuario creado correctamente'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@users_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        con = create_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        con.close()
        username_db = user[1]
        password_db = user[2]

        password_uncoded = decode_jwt(password_db)
        password_uncoded = password_uncoded['password']

        session = encode_jwt({'password': password_db, 'username': username_db})

        if username_db == username and password_uncoded == password:
            return session
        else:
            return jsonify({'message': 'Usuario o contraseña incorrectos'})

    except Exception as e:
        return jsonify({'message': str(e)}), 400
