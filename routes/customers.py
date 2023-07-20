from flask import Blueprint, jsonify, request
from database.connection import create_connection

customers_bp = Blueprint("customers", __name__)


@customers_bp.route("/add", methods=["POST"])
def add_cliente():
    try:
        con = create_connection()
        cur = con.cursor()

        data = request.get_json()

        name = data.get("nombre")
        lastname = data.get("apellido")
        phone = data.get("numero_telefonico")
        email = data.get("correo")
        address = data.get("direccion")
        postal_code = data.get("codigo_postal")
        city = data.get("ciudad")
        province = data.get("provincia")
        date = data.get("fecha")
        description = data.get("descripcion")
        budget = data.get("presupuesto_enviado")
        accepted_budget = data.get("presupuesto_aceptado")
        done = data.get("realizado")
        invoiced = data.get("facturado")

        print(name, lastname, phone, email, address, city, province, description, postal_code, budget, accepted_budget, done, invoiced, date)

        query = """
        INSERT INTO customers (name, lastname, phone, email, address, city, province, postal_code, description, budget, accepted_budget, done, invoiced, date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cur.execute(query, (name, lastname, phone, email, address, city, province, postal_code, description, budget, accepted_budget, done, invoiced, date))
        con.commit()
        con.close()

        return {"message": "Client added successfully"}, 201

    except Exception as e:
        print(e)
        con.close()
        return {"message": "Error adding client"}, 500



@customers_bp.route("/", methods=["GET"])
def get_customers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT *FROM customers ORDER BY date DESC")
    data_cunstomers = cur.fetchall()
    print(data_cunstomers)

    data = [
        {
            "idcustomer": x[0],
            "name": x[1],
            "lastname": x[2],
            "phone": x[3],
            "email": x[4],
            "address": x[5],
            "city": x[6],
            "province": x[7],
            "postal_code": x[8],
            "budget": x[9],
            "accepted_budget": x[10],
            "date": x[13],
            "done": x[11],
            "invoiced": x[12],
            "description": x[14]
        }
        for x in data_cunstomers
    ]

    
    return data
