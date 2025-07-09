from colorama import Fore,Style


import sqlite3
con = sqlite3.connect("inventario2.db")

cur = con.cursor()

def agregar_producto():
    print(Fore.RED + "\nAlta de producto\n" + Style.RESET_ALL)
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")

    if not nombre or not categoria:
        print(Fore.YELLOW + " El nombre y la categoría no pueden estar vacíos.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))

        if cantidad < 0 or precio < 0:
            print(Fore.YELLOW + " La cantidad y el precio no pueden ser negativos.")
            return

    except ValueError:
        print(Fore.YELLOW + " El precio o la cantidad deben ser números válidos.")
        return

    try:
        cur.execute(
           
              "INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)",
              (nombre, categoria, cantidad, precio))
              #f"INSERT INTO productos (nombre, categoria, cantidad, precio) "
           # f"VALUES ('{nombre}', '{categoria}', {cantidad}, {precio})"
        
        con.commit()
        print(Fore.GREEN + " Alta realizada exitosamente.")
    except sqlite3.Error as e:
        print(Fore.RED + f" Error al insertar en la base de datos: {e}")



def listar_productos():
   cur.execute('SELECT * FROM productos')
   productos = cur.fetchall()

   for producto in productos:
    print(Fore.RED +f"ID: {producto[0]}, Nombre: {producto[1]}, Categoria: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}")



def actualizar_producto():
    listar_productos()

    indice = int(input("Ingrese el ID del producto a actualizar: "))
    cur.execute("SELECT * FROM productos WHERE id = ?", (indice,))
    producto = cur.fetchone()

    if not producto:
        print(" No se encontró un producto con ese ID.")
        return

    print("\n¿Qué desea actualizar?")
    print("1. Nombre")
    print("2. Categoría")
    print("3. Cantidad")
    print("4. Precio")

    opcionActualizar = input("Seleccione una opción (1-4): ")

    if opcionActualizar == "1":
        nuevo_valor = input("Ingrese el nuevo nombre: ").strip()
        if nuevo_valor:
            cur.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nuevo_valor, indice))

    elif opcionActualizar == "2":
        nuevo_valor = input("Ingrese la nueva categoría: ").strip()
        if nuevo_valor:
            cur.execute("UPDATE productos SET categoria = ? WHERE id = ?", (nuevo_valor, indice))

    elif opcionActualizar == "3":
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        if nueva_cantidad >= 0:
            cur.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, indice))
        else:
            print(" La cantidad no puede ser negativa.")
            return

    elif opcionActualizar == "4":
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio >= 0:
            cur.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, indice))
        else:
            print(" El precio no puede ser negativo.")
            return

    else:
        print(" Opción inválida.")
        return

    con.commit()
    print(Fore.GREEN + "***** Producto actualizado correctamente.****")




def eliminar_producto():
    listar_productos()
    
    try:
        id = int(input("Ingrese el ID del producto a eliminar: "))
        
        # Verificamos si el producto existe antes de intentar eliminarlo
        cur.execute("SELECT * FROM productos WHERE id = ?", (id,))
        producto = cur.fetchone()

        if not producto:
            print(Fore.YELLOW + " No se encontró ningún producto con ese ID.")
            return

        cur.execute("DELETE FROM productos WHERE id = ?", (id,))
        con.commit()

        print(Fore.GREEN + "*** Producto eliminado correctamente.****")
        
        # Mostrar productos1 después de la eliminación
        listar_productos()

    except ValueError:
        print(Fore.YELLOW + " El ID debe ser un número.")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")


def buscar_producto_nombre():
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()

    cur.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    prod = cur.fetchone()

    if prod:
        print(Fore.GREEN + "\n Producto encontrado:" )
        print(Fore.GREEN + f"ID: {prod[0]}, Nombre: {prod[1]}, Categoría: {prod[2]}, Cantidad: {prod[3]}, Precio: ${prod[4]:.2f}")
    else:
        print(" ***Producto no encontrado.***")     


def reporte_stock_minimo():
    try:
        limite = int(input("Mostrar productos con cantidad menor o igual a: "))
        cur.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cur.fetchall()
        if productos:
            print(Fore.GREEN + f"\n--- Productos con stock ≤ {limite} ---")
            for prod in productos:
                print(f"ID: {prod[0]}, Nombre: {prod[1]}, Cantidad: {prod[3]}")
        else:
            print("No hay productos con ese nivel de stock.")
    except ValueError:
        print(" El valor debe ser numérico.")      


def menu():
    while True:
        print(Fore.CYAN + "\n===== MENÚ DE GESTIÓN DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar  producto por nombre")
        print("6. Reporte de stock mínimo")
        print("7. Salir")
        
        try:
            op = int(input("Seleccione una opción: "))
        except ValueError:
            print(" Debe ingresar un número.")
            continue

        if op == 1:
            agregar_producto()
        elif op == 2:
            listar_productos()
        elif op == 3:
            actualizar_producto()
        elif op == 4:
            eliminar_producto()
        elif op == 5:
            buscar_producto_nombre()
        elif op == 6:
            reporte_stock_minimo()
        elif op == 7:
            print("Gracias por usar el Sistema de Gestión de Productos. ¡Hasta luego!")
            break
        else:
            print("Error. Por favor ingrese un número del 1 al 7.")

menu()
con.close()

   

    

   

