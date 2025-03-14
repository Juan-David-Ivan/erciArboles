import psycopg2

def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="jardin",
        user="postgres",
        password="1234",
        host="192.168.86.128",
        port="5433"
    )
    return conn

def consultar_arboles():
    conn = connect()
    arboles = []
    try:
        cursor = conn.cursor()
        query = """
                SELECT *
                FROM arboles
                """
        cursor.execute(query)
        arboles = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener los árboles: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    print(arboles)
    return arboles

def insertar_arbol(nombre, tipo, altura_promedio, fecha_plantacion):
    """
    Inserta un nuevo árbol en la base de datos.

    Parámetros:
    - nombre (str): Nombre del árbol (ejemplo: "Pino").
    - tipo (str): Puede ser "Perenne" o "Caduca".
    - altura_promedio (int): Altura promedio del árbol en metros.
    - fecha_plantacion (str): Fecha en formato 'YYYY-MM-DD' de la plantación.
    """
    conn = connect()  # Conectar a la base de datos
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar consultas SQL

        # Consulta SQL para insertar un nuevo árbol en la tabla 'Arboles'
        query = """
        INSERT INTO Arboles (nombre, tipo, altura_promedio, fecha_plantacion)
        VALUES (%s, %s, %s, %s)
        """

        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (nombre, tipo, altura_promedio, fecha_plantacion))

        # Confirmar la transacción
        conn.commit()
        print("Árbol registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos

# Ejemplo de uso:
# insertar_arbol("Pino", "Perenne", 30, "2005-03-15")
