import flet as ft
import ddbb

def main(page: ft.Page):
    page.title = "Consultas"

    def cargar_Tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))),
                ft.DataCell(ft.Text(str(fila[1]))),
                ft.DataCell(ft.Text(str(fila[2]))),
                ft.DataCell(ft.Text(str(fila[3]))),
                ft.DataCell(ft.Text(str(fila[4]))),

            ]))
    def consultar_arboles():
        arboles = ddbb.consultar_arboles()
        cargar_Tabla(arboles)
        page.update()

    def consultar_arboles_por_nombre(nombre):
        conn = connect()
        arboles = []
        try:
            cursor = conn.cursor()
            query = """
                    SELECT *
                    FROM arboles
                    WHERE lower(nombre) = lower('%s')
                    """
            cursor.execute(query,(nombre,))
            arboles = cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener los árboles: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()
        print(arboles)
        return arboles

    def buscar_arboles(e):
        ddbb.consultar_arboles_por_nombre(nombre_tf.value)
        cargar_Tabla(lista_arboles)
        page.update()

    def volver(e):
        page.go("/consultas")

    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)

    tabla = ft.DataTable(bgcolor="yellow",
        columns=[
            ft.DataCell(ft.Text("ID")),
            ft.DataCell(ft.Text("NOMBRE")),
            ft.DataCell(ft.Text("TIPO")),
            ft.DataCell(ft.Text("ALTURA")),
            ft.DataCell(ft.Text("FECHA"))
        ]
    )
    nombre_tf = ft.TextField("Nombre",width=300)
    buscar_btn = ft.ElevatedButton("Buscar", width=300, on_click=consultar_arboles)
    columna_datos = ft.Column(
        controls=[
            ft.Text("Consultas", size=40),
            nombre_tf,
            buscar_btn,
            tabla,
            volver_btn
        ]
    )
    page.add(columna_datos)
    return  columna_datos

