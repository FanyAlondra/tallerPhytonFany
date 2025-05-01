import mariadb
def connectar_y_conssultar():
    try:
        conexion=mariadb.connect(
            host="localhost",
            database="Almacen",
            user="root",
            password="",
            port=3306
        )
        print(type(conexion))
        print("conexion a la base de datos del servidor Ounus")

        cursor= conexion.cursor()
        consulta ="select * from usuarios"
        cursor.execute (consulta)

        resultado =cursor.fetchall()
        print("resultado ", type(resultado))
        print("Datos de la tabla:")
        for fila in resultado:

            print(f"ID:{fila[0]}, Nombre de usuario: {fila[1]}, correo electronico: {fila[2]},contraseña: {fila[3]},id_rol {fila[4]} ")

        cursor = conexion.cursor()
        consulta = "SELECT * FROM roles"
        cursor.execute(consulta)

        resultados = cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla Roles: ")
        for fila in resultados:
            print(f"| ID_Rol: {fila[0]} | Nombre del Rol: {fila[1]}")


    except mariadb.Error as e:
        print(f"Error al conectar la base de datos: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor. close()
            print("conexion cerrada. ")



if __name__ == '__main__':
    connectar_y_conssultar()