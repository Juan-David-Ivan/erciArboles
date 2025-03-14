import psycopg2


def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="biblioteca",
        user="postgres",
        password="1234",
        host="192.168.86.128",
        port="5433"
    )
    return conn




def insertar_libro(titulo, isbn, autor, num_paginas, fecha_publicacion):
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
        INSERT INTO Libros (titulo, isbn, autor, num_paginas, fecha_publicacion)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (titulo,isbn,autor,num_paginas,fecha_publicacion))

        # Confirmar la transacción
        conn.commit()
        print("Libro registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos