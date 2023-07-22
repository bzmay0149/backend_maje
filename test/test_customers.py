import pytest
from database.connection import create_connection

def test_customers_table_columns():
    con = create_connection()
    cur = con.cursor()

    # Ejecutar una consulta para obtener el número de columnas en la tabla "customers"
    cur.execute("SHOW COLUMNS FROM customers")
    columns = cur.fetchall()

    # Verificar que la tabla "customers" tiene 15 columnas
    assert len(columns) == 15

    con.close()
    
    
    




def test_insert_customer():
    con = create_connection()
    cur = con.cursor()

    # Datos del nuevo cliente (sin la columna "term")
    new_customer = {
        "name": "John",
        "lastname": "Doe",
        "phone": "123456789",
        "email": "john@example.com",
        "address": "123 Main Street",
        "city": "New York",
        "province": "NY",
        "postal_code": 10001,
        "budget": "yes",
        "accepted_budget": "yes",
        "done": "no",
        "invoiced": "no"
    }

    # Realizar la inserción del nuevo cliente en la tabla "customers"
    try:
        cur.execute("""
            INSERT INTO customers (name, lastname, phone, email, address, city, province, postal_code, budget, accepted_budget, done, invoiced)
            VALUES (%(name)s, %(lastname)s, %(phone)s, %(email)s, %(address)s, %(city)s, %(province)s, %(postal_code)s, %(budget)s, %(accepted_budget)s, %(done)s, %(invoiced)s)
        """, new_customer)

        # Confirmar la transacción
        con.commit()
    except Exception as e:
        # Si hay algún error, deshacer la transacción
        con.rollback()
        raise e
    finally:
        con.close()

    # Verificar que el cliente fue insertado correctamente
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE name='John' AND lastname='Doe'")
    customer = cur.fetchone()
    con.close()

    assert customer is not None



  