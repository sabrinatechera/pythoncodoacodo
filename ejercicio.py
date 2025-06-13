productList = []

while True:
    print(" Sistema de Gestión Básica De Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = int(input("Por favor seleccione una opción del menu anterior : ").strip())

    if opcion == "1":
        while True:
            producto= input("Ingrese el nombre del producto: ").strip()
            if producto == "":
                print(" El nombre del producto no puede estar vacío.")
                continue

            categoria = input("Ingrese la categoría del producto: ").strip()
            if categoria == "":
                print(" La categoría no puede estar vacía.")
                continue

            precio=float(input("Ingrese el precio pero asegurese de que sea un numero entero.Gracias: ").strip())
          
            if not precio.is_integer() or precio<=0:
                print("El precio debe ser un número entero mayor que cero.")
                continue

            precio = int(precio)
            productoDatos = [producto.title(), categoria.title(), precio]
            productList.append(productoDatos)
            print(f"\nProducto '{producto}' agregado correctamente!")
            break

    elif opcion == "2":
        if len(productList) == 0:
            print(" No hay productos registrados.")
        else:
            print("Lista de Productos Registrados:")
            for i in range(len(productos)):
                print(f"{i+1}. Nombre: {productos[i][0]}, Categoría: {productos[i][1]}, Precio: ${productos[i][2]}")

    elif opcion == "3":
        termino = input("🔍 Ingrese el nombre del producto a buscar: ").strip().lower()
        encontrados = []
        for p in productos:
            if termino in p[0].lower():
                encontrados.append(p)

        if len(encontrados) > 0:
            print("Productos encontrados:")
            for i in range(len(encontrados)):
                print(f"{i+1}. Nombre: {encontrados[i][0]}, Categoría: {encontrados[i][1]}, Precio: ${encontrados[i][2]}")
        else:
            print("No se encontraron productos con ese nombre.")

    elif opcion == "4":
        if len(productList) == 0:
            print(" No hay productos para eliminar.")
        else:
                
         nombre_a_eliminar = input("\nIngrese el nombre del producto a eliminar: ").strip().lower()

         encontrado = False
         for i, producto in enumerate(productList):
            if producto[0].strip().lower() == nombre_a_eliminar:
                eliminado = productList.pop(i)
                print(f"El producto fueeliminado exitosamente.")
                encontrado = True
                break
        
         if not encontrado:
            print(f" El producto solicitado no se encuentra en la lista.")

    elif opcion == "5":
        print("Gracias por usar el Sistema de Gestión de Productos. ¡Hasta luego!")
        break

else:
    print("Error: Opción no válida. Por favor ingrese un número del 1 al 5.")
