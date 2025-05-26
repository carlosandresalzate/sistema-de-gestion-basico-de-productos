# 🐍 Sistema de Gestión Básica de Productos

Este proyecto es un sistema interactivo de consola desarrollado en **Python 3.13.3** 🐍. Permite a una empresa registrar, visualizar, buscar y eliminar productos a través de una interfaz sencilla y amigable para el usuario. Está orientado a principiantes en programación que deseen practicar estructuras de datos como listas, ciclos `while` y `for`, validación de entrada y lógica condicional.

---

## 📌 Descripción del Proyecto

Este programa tiene como objetivo diseñar un sistema básico que permita **gestionar información inicial sobre productos** de una empresa de forma interactiva desde la consola. Ofrece un menú que guía al usuario a través de las siguientes funcionalidades:

- ➕ Agregar productos (nombre, categoría y precio sin centavos)
- 📋 Visualizar todos los productos ingresados, de manera ordenada
- 🔍 Buscar productos por nombre
- ❌ Eliminar productos por su número en la lista
- 🚪 Salir del programa

---

## ⚙️ Requisitos Técnicos

### ✅ Requisitos funcionales:

1. Utilizar **listas** para almacenar y gestionar los datos.
2. Incorporar **bucles `while` y `for`** según corresponda.
3. Validar las entradas del usuario, evitando datos vacíos o no válidos.
4. Utilizar **estructuras condicionales** para gestionar opciones del menú.
5. Mantener el programa en ejecución hasta que el usuario elija salir.

### 💾 Estructura de los datos:

Cada producto es representado como una sublista:

```python
["nombre", "categoría", precio]
```

Y se almacena dentro de una lista general de productos.

---

## 🧪 Requisitos de software

* ✔️ **Python 3.13.3** (o superior)
* 🧠 Funciona en cualquier sistema operativo compatible con Python

---

## 💻 Cómo ejecutar el programa

### ▶️ En Linux / Ubuntu 🐧

```bash
python3 main.py
```

> Asegurate de tener Python 3.13.3 instalado:
>
> ```bash
> python3 --version
> ```

### ▶️ En Windows 🪟

```cmd
python main.py
```

> Si `python` no funciona, probá con:
>
> ```cmd
> py main.py
> ```

### ▶️ En macOS 🍎

```bash
python3 main.py
```

> Verificá la versión con:
>
> ```bash
> python3 --version
> ```

---

## 📄 Funcionalidades detalladas

### 📥 Ingreso de productos

* Solicita nombre, categoría y precio.
* El precio debe ser un número entero.
* Los productos se guardan en una lista como sublistas.

### 📊 Visualización de productos

* Muestra todos los productos con su número.
* Presenta los datos en una tabla legible y alineada.

### 🔎 Búsqueda de productos

* Permite buscar productos por su **nombre**.
* Si hay coincidencias, muestra el producto completo.
* Si no se encuentra nada, muestra un mensaje informativo.

### 🗑️ Eliminación de productos

* Permite eliminar un producto por su número en la lista.
* Valida que la entrada sea correcta.

---

## 🧠 Tabla de nombres de variables y estructuras

| Español                           | Inglés                | Tipo de dato                            |
| :-------------------------------- | :-------------------- | :-------------------------------------- |
| Lista de productos                | `product_list`        | `list` de sublistas `[str, str, int]`   |
| Producto individual nuevo         | `new_product`         | `list` de 3 elementos `[str, str, int]` |
| Nombre del producto               | `name`                | `str`                                   |
| Categoría del producto            | `category`            | `str`                                   |
| Precio del producto               | `price`               | `str` → convertido a `int`              |
| Lista de opciones del menú        | `menu_opcion`         | `list` de `str`                         |
| Entrada del usuario (menú)        | `user_input`          | `str`                                   |
| Entrada del usuario (eliminar)    | `del_input`           | `str`                                   |
| Índice del producto a eliminar    | `del_index`           | `int`                                   |
| Producto eliminado                | `deleted`             | `list` (sublista eliminada)             |
| Texto símbolo del prompt          | `symbol`              | `str`                                   |
| Bucle de ejecución del programa   | `is_running`          | `bool`                                  |
| Opción seleccionada (entero)      | `option`              | `int`                                   |
| Contador de productos en lista    | `i`                   | `int`                                   |
| Nombre a buscar                   | `search_name`         | `str`                                   |
| Bandera de producto encontrado    | `found`               | `bool`                                  |
| Texto estático tabla de productos | *(constante literal)* | *dentro de `print()`*                   |

---

## 📘 Notas adicionales

* El código está documentado con claridad.
* Este proyecto es ideal para comenzar con lógica de programación aplicada.
* Se recomienda extenderlo más adelante con persistencia en archivos o una interfaz gráfica.

---

## ✨ Licencia

Proyecto educativo de uso libre. Creado por un autodidacta apasionado por la programación 🤓🚀

---

## 🧠 Autor

**Carlos Andres Alzate** — 🇦🇷 Soy un aprendiz autodidacta enfocado en desarrollo web, interfaces gráficas, electrónica con Arduino, y más.
Este proyecto forma parte de mi proceso de aprendizaje en Python 🐍.
