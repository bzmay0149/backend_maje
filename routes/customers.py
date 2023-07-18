from flask import Blueprint, jsonify, request
from database.connection import create_connection

customers_bp = Blueprint("customers", __name__)


@customers_bp.route("/add", methods=["POST"])
def add_cliente():
    try:
        con = create_connection()
        cur = con.cursor()

        postman = request.get_json()

        name = postman["name"]
        lastname = postman["lastname"]
        phone = postman["phone"]
        email = postman["email"]
        address = postman["address"]
        city = postman["city"]
        province = postman["province"]
        postal_code = postman["postal_code"]
        budget = postman["budget"]
        accepted_budget = postman["accepted_budget"]
        done = postman["done"]
        invoiced = postman["invoiced"]
        date = postman["date"]

        cur.execute(
            "INSERT INTO customers (name, lastname, phone, email, address, city, province, postal_code, budget, accepted_budget,  done, invoiced, date) VALUES (%s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                name,
                lastname,
                phone,
                email,
                address,
                city,
                province,
                postal_code,
                budget,
                accepted_budget,
                done,
                invoiced,
                date,
            ),
        )
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
            "date": x[11],
            "done": x[12],
            "invoiced": x[13],
        }
        for x in data_cunstomers
    ]

    print(data)
    return data
