# 📦 GESTIÓ DE PRODUCTOS
# -----------------------------------------------------------------------------
# Author: Carlos Andres Alzate
# Fecha Mayo,2025
# Descripción: Este script permite gestionar productos en una lista.
# Funcionalidades: agregar, mostrar, buscar y eliminar productos.
# Cada producto tiene: nombre, categoría y precio.
# Estructura simple pero pensada para poder escalar luego.
# -----------------------------------------------------------------------------

# Lista principal de productos (Precargados como ejemplo).
# Cada producto es una sublista: [nombre, categoria, precio]
product_list = [
    {"name": "pan", "category": "panaderia", "price": 120},
    {"name": "abaco", "category": "jugueteria", "price": 300},
    {"name": "tomate", "category": "verduleria", "price": 40},
    {"name": "bife chorizo", "category": "carne", "price": 500},
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
            print("\n--- ➕ Agregar un nuevo producto ➕  ---")
            print("Presione Enter en cualquier campo para volver al menú.\n")

            while True:
                new_product = {}

                # Ingreso del nombre del producto
                name = input("Nombre del Producto: ").strip()
                if not name:
                    break
                found = False
                for product in product_list:
                    if product["name"].lower() == name.lower():
                        found = True
                        print(
                            f"\n🚫 El producto << {product['name'].upper()} >> ya existe 🚫"
                        )
                        print(
                            f"""
                            \r✅ Producto encontrado ✅
                            \r🛍️ Nombre: {product["name"].title()}
                            \r🏷️ Categoría: {product["category"].title()}
                            \r💲 Precio:     ${product["price"]}
                            """
                        )
                        break

                if found:
                    break
                # products_ = product_list.keys()
                # print(products_)
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
                new_product["name"] = name.lower()
                new_product["category"] = category.lower()
                new_product["price"] = int(price)
                product_list.append(new_product)

                # Confirmacion visual del producto agregado
                print("\n✅ ¡Producto agregado exitosamente!")
                print(
                    f"""
                    \r📦 {"Nombre:":<15} {new_product.get("name", "").title():<15}
                    \r🏷️ {"Categoría:":<15} {new_product.get("category", "").title():<15}
                    \r💲 {"Precio:":<15} ${new_product.get("price"):<15}
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
                for i in range(len(product_list)):
                    for j in range(len(product_list) - i - 1):
                        if product_list[j]["name"] > product_list[j + 1]["name"]:
                            # intercambiar
                            temp = product_list[j]
                            product_list[j] = product_list[j + 1]
                            product_list[j + 1] = temp
                # mostrar resultado
                print(f"{'Nº':2} | {'Producto':<15} | {'Categoria':<15} | {'$':<15}")
                print("================================================")
                for index, product in enumerate(product_list, start=1):
                    print(
                        f"{index:2} | {product['name'].title():<15} | {product['category']:<15} | ${product['price']}"
                    )
                print("================================================")
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
                    if search_name.lower() == prod["name"].lower():
                        found = True
                        print(
                            f"""
                            \r✅ Producto encontrado ✅
                            \r🛍️ Nombre: {prod["name"].title()}
                            \r🏷️ Categoría: {prod["category"].title()}
                            \r💲 Precio:     ${prod["price"]}
                            """
                        )
                        break

                    if found:
                        print("==============================================")
                    elif not found:
                        print("\n  ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌")
                        print("❌ Producto no encontrado ❌")
                        print("  ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌\n")
                        break
        case 4:
            # -----------------------------------------------------------------
            # Opción 4: Eliminar producto
            # -----------------------------------------------------------------
            while True:
                print("\n--- 🗑️ Eliminar un producto 🗑️ ---")
                print("Presione Enter en cualquier campo para volver al menú.\n")
                if not product_list:
                    print("⚠️ No hay productos para eliminar.")
                    break

                print("📦 =========================================== 📦")
                # Ordena por nombre en orden alfabetico a - z
                for i in range(len(product_list)):
                    for j in range(len(product_list) - i - 1):
                        if product_list[j]["name"] > product_list[j + 1]["name"]:
                            # intercambiar
                            temp = product_list[j]
                            product_list[j] = product_list[j + 1]
                            product_list[j + 1] = temp
                # mostrar resultado
                print(f"{'Nº':2} | {'Producto':<15} | {'Categoria':<15} | {'$':<15}")
                print("================================================")
                for index, product in enumerate(product_list, start=1):
                    print(
                        f"{index:2} | {product['name'].title():<15} | {product['category']:<15} | ${product['price']}"
                    )
                print("================================================\n")
                # product_list.sort()
                # for i, prod in enumerate(product_list, start=1):
                #     print(
                #         f"{i:2}. {prod[0].title():<15} | {prod[1].title():<12} | ${prod[2]}"
                #     )
                # print("")

                del_input = input(
                    "👉 Ingrese el número del producto a eliminar (o Enter para cancelar): "
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

                # print("")

                # Eliminacición confirmada
                deleted = product_list.pop(del_index)
                print(f"🗑️ Producto '{deleted['name'].title()}' eliminado con éxito.")
                print("")
# 🔚 Fin del programa
