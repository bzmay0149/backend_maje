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


@customers_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_customer(id):
    try:
        if not isinstance(id, int) or id <= 0:
            return {"message": "Invalid customer ID"}, 400

        with create_connection() as con, con.cursor() as cur:
            cur.execute("DELETE FROM customers WHERE idcustomer = %s", (id,))
            con.commit()

        return {"message": "Customer deleted successfully"}, 204
    except Exception as e:
        return {"message": "Error deleting customer"}, 500

@customers_bp.route("/update/<int:id>", methods=["PUT"])
def actualizar_cliente(cliente_id):
    # Aquí obtienes los datos enviados en la solicitud PUT
    datos_cliente = request.json()
    
    budget = datos_cliente['budget']
    accepted_budget = datos_cliente['accepted_budget']
    done = datos_cliente['done']
    invoiced = datos_cliente['invoiced']

    # Luego, puedes usar el cliente_id para identificar el cliente en la base de datos
    # y actualizar los campos correspondientes con los datos nuevos.
    # Puedes usar alguna librería ORM o el acceso directo a la base de datos, dependiendo de cómo estés manejando la conexión con la base de datos.

    # Ejemplo de cómo actualizar el cliente en una lista de clientes en memoria:
    
        
            cliente['budget'] = datos_cliente['budget']
            cliente['accepted_budget'] = datos_cliente['accepted_budget']
            cliente['done'] = datos_cliente['done']
            cliente['invoiced'] = datos_cliente['invoiced']

    # Aquí devuelves una respuesta, por ejemplo, un mensaje de éxito.
    return jsonify({'message': 'Cliente actualizado correctamente'})

# Si estás usando Flask en modo de desarrollo, puedes ejecutar tu aplicación con:
if __name__ == '__main__':
    app.run(debug=True)