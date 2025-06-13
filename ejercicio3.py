productList = []

while True:
    print("Sistema de Gestión Básica De Productos ")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        while True:
            nombreProducto = input("Ingrese el nombre del producto: ").strip()
            if not nombreProducto:
                print("El nombre no puede estar vacío.")
                continue

            categoria = input("Ingrese la categoría del producto: ").strip()
            if not categoria:
                print("La categoría no puede estar vacía.")
                continue

            try:
                precio = float(input("Ingrese el precio (entero, sin centavos): ").strip())
                if not precio.is_integer() or precio <= 0:
                    print("El precio debe ser un número entero mayor que cero.")
                    continue
                precio = int(precio)
            except ValueError:
                print("Error: Ingrese un número válido.")
                continue

            productList.append([nombreProducto.title(), categoria.title(), precio])
            print(f"Producto '{nombreProducto.title()}' agregado correctamente.")
            break

    elif opcion == "2":
        if not productList:
            print("No hay productos registrados.")
        else:
            print("Lista de Productos Registrados:")
            for i, p in enumerate(productList, 1):
                print(f"{i}. Nombre: {p[0]}, Categoría: {p[1]}, Precio: ${p[2]}")

    elif opcion == "3":
        termino = input(" Ingrese el nombre del producto a buscar: ").strip().lower()
        encontrados = [p for p in productList if termino in p[0].lower()]

        if encontrados:
            print("📋 Productos encontrados:")
            for i, p in enumerate(encontrados, 1):
                print(f"{i}. Nombre: {p[0]}, Categoría: {p[1]}, Precio: ${p[2]}")
        else:
            print(" No se encontraron productos con ese nombre.")

    elif opcion == "4":
        if not productList:
            print("No hay productos para eliminar.")
        else:
            nombre_a_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
            encontrado = False
            for i, p in enumerate(productList):
                if p[0].strip().lower() == nombre_a_eliminar:
                    eliminado = productList.pop(i)
                    print("Producto  eliminado exitosamente.")
                    encontrado = True
                    break
            if not encontrado:
                print("El producto no se encuentra en la lista.")

    elif opcion == "5":
        print("Gracias por usar el Sistema de Gestión de Productos. ¡Hasta luego!")
        break

    else:
        print("Error. Por favor ingrese un número del 1 al 5.")
