# TAD Lista doblemente enlazada

Breve descripción del proyecto:

A partir de unas especificaciones logicas se implemento el TAD listas doblemente enlazadas, para poder crear una grafica de (n) cantidad de elementos sobre tiempo de ejecucion de los metodos __len__(), invertir() y copiar() para comparar su eficiencia. 

---
## 🏗Arquitectura General

LDE.py
Clase Nodo: Representa un nodo de la lista doblemente enlazada, con referencias al dato, al siguiente y al anterior nodo.
Clase ListaDobleEnlazada: Implementa la estructura de lista doblemente enlazada y sus operaciones principales:
Métodos para agregar al inicio/final, insertar en posición, copiar, extraer, invertir, concatenar, verificar si está vacía, obtener longitud, sumar listas y recorrer la lista.
Todos los métodos están encapsulados en la clase, no hay funciones sueltas.

Graficas_LDE.py
Contiene funciones para medir el tiempo de ejecución de operaciones sobre la lista doblemente enlazada:
medir_tiempos_len, medir_tiempos_copia, medir_tiempos_invertir: Miden el tiempo de las operaciones len, copiar e invertir respectivamente.
graficar_tiempos: Genera y muestra una gráfica comparando los tiempos de las operaciones anteriores.

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Sabina Gerbaudo
- Ivan Nicolas Deleon
- Virginia Isabel Rogau

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
