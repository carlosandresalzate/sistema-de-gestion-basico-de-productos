# 📦 GESTIÓ DE PRODUCTOS
# -----------------------------------------------------------------------------
# Author: Carlos Andres Alzate
# Fecha: Mayo - 2025
# Descripción: Este script permite gestionar productos en una lista.
# Funcionalidades: agregar, mostrar, buscar y eliminar productos.
# Cada producto tiene: nombre, categoría y precio.
# Estructura simple pero pensada para poder escalar luego.

# Lista principal de productos (Precargados como ejemplo).
# Cada producto es una sublista: [nombre, categoria, precio]
product_list = [
    ["pan", "panaderia", 120],
    ["abaco", "jugueteria", 300],
    ["tomate", "verduleria", 40],
    ["bife chorizo", "carne", 500],
]

# Menú de opciones del sistema
menu_opcion = [
    "Agregar producto",
    "Mostrar productos",
    "Buscar producto",
    "Eliminar producto",
    "Salir",
]

# Símbolo decoratico para el input
symbol = ">"

# Controla el ciclo principal del programa
is_running = True

# Titulo de bienvenida
print("=" * 40)
print("📦 BIENVENIDO A LA GESTIÓN DE PRODUCTOS 📦")
print("=" * 40)

# 🔁 Bucle principal
while is_running:
    # muestro el menu
    print("\n--- Menú Principal ---\n")

    # Se imprime el menú  con índices numerado
    for i, option in enumerate(menu_opcion, 1):
        print(f"{i}. {option.title()}")
    print("")

    # Solicita al usuario una opciín del menú
    user_input = input(f"Ingrese una opcion (1-{len(menu_opcion)})\n{symbol} ").strip()

    # Validaciones: entrada vacía o no numérica
    if not user_input:
        print("❌ Entrada vacía. Cerrando el programa.")
        break

    if not user_input.isdigit():
        print("❌ Debe ingresar un número válido.")
        continue

    # Conversión sergura de entrada a entero
    option = int(user_input)

    if option < 1 or option > len(menu_opcion):
        print(f"⚠️ Opción inválida. Ingrese un número entre 1 y {len(menu_opcion)}.")
        continue

    # Opción "salir"
    if option == 5:
        is_running = False
        break

    # 📌 Menú principal controlado con match-case
    match option:
        case 1:
            # -----------------------------------------------------------------
            # Opción 1: Agregar nuevo producto
            # -----------------------------------------------------------------
            print("\n--- ➕ Agregar un nuevo producto ---")
            print("Presione Enter en cualquier campo para volver al menú.\n")

            while True:
                new_product = []

                # Ingreso del nombre del producto
                name = input("Nombre del Produto: ").strip()
                if not name:
                    break

                # Ingreso de la categoria
                category = input("Categoria del producto: ").strip()
                if not category:
                    break

                # Ingreso del precio
                price = input("Precio del producto: ").strip()
                if not price:
                    break

                if not price.isdigit():
                    print("⚠️ El precio debe ser un número.")
                    continue

                # Se almacena el producto en la lista
                new_product = [name.lower(), category.lower(), int(price)]
                product_list.append(new_product)

                # Confirmacion visual del producto agregado
                print("\n✅ ¡Producto agregado exitosamente!")
                print(
                    f"""
                    \r📦 Producto:  {new_product[0].title()}
                    \r🏷️ Categoría: {new_product[1].title()}
                    \r💲 Precio:    ${new_product[2]}
                    """
                )
                break

        case 2:
            # -----------------------------------------------------------------
            # Opción 2: Mostrar productos
            # -----------------------------------------------------------------
            print("\n-- 📦 Lista de Productos --")
            print("Presione Enter en cualquier campo para volver al menú.\n")
            if not product_list:
                print("No hay Productos aun")
            else:
                print("📦 =========================================== 📦")
                # Ordena por nombre en orden alfabetico a - z
                product_list.sort()
                for i, prod in enumerate(product_list, start=1):
                    print(
                        f"{i:2}. {prod[0].title():<15} | {prod[1].title():<12} | ${prod[2]}"
                    )
        case 3:
            # -----------------------------------------------------------------
            # Opción 3: Buscar producto
            # -----------------------------------------------------------------
            while True:
                print("\n--- 🔍 Buscar producto por nombre ---\n")
                print("Presione Enter en cualquier campo para volver al menú.\n")
                # Nota Mental: el uso de parentesis para continuar con una expresion multilenea se conoce como _implicit line continuation_
                search_name = (
                    input(
                        "Ingrese el nombre exacto del producto (o Enter para cancelar): "
                    )
                    .strip()
                    .lower()
                )

                if not search_name:
                    break

                found = False
                for prod in product_list:
                    if search_name == prod[0]:
                        print(
                            f"""
                            \r✅ Producto encontrado
                            \r🛍️ Nombre: {prod[0].title()}
                            \r🏷️ Categoría: {prod[1].title()}
                            \r💲 Precio:     ${prod[2]}
                            """
                        )
                        found = True
                        break
                    if found:
                        print("==============================================")
                    if not found:
                        print("❌ Producto no encontrado.")
                    else:
                        print("\n  ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌")
                        print("❌ Producto no encontrado ❌")
                        print("  ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌\n")
                        break
        case 4:
            # -----------------------------------------------------------------
            # Opción 4: Eliminar producto
            # -----------------------------------------------------------------
            print("\n--- 🗑️ Eliminar un producto ---\n")
            print("Presione Enter en cualquier campo para volver al menú.\n")
            if not product_list:
                print("⚠️ No hay productos para eliminar.")
                break

            print("📦 =========================================== 📦")
            # Ordena por nombre en orden alfabetico a - z
            product_list.sort()
            for i, prod in enumerate(product_list, start=1):
                print(
                    f"{i:2}. {prod[0].title():<15} | {prod[1].title():<12} | ${prod[2]}"
                )
            print("")

            del_input = input(
                "Ingrese el número del producto a eliminar (o Enter para cancelar): "
            ).strip()

            if not del_input:
                print("🔙 Operación cancelada.")
                break

            if not del_input.isdigit():
                print("⚠️ Entrada inválida. Debe ingresar un número.")
                break

            del_index = int(del_input) - 1
            if del_index < 0 or del_index >= len(product_list):
                print("❌ Número fuera de rango.")
                break

            print("")

            # Eliminacición confirmada
            deleted = product_list.pop(del_index)
            print(f"🗑️ Producto '{deleted[0].title()}' eliminado con éxito.")
            print("")
# 🔚 Fin del programa
