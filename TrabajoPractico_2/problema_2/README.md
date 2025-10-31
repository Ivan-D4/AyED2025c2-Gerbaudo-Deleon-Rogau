# 🐍 Temperaturas_DB

Breve descripción del proyecto:

“El código presentado busca optimizar la consulta, comparación, registro y odificación  de una base de datos de temperaturas. Internamente se implenta un árbol AVL. "

---
## 🏗Arquitectura General

Archivos y responsabilidades
avl_tree.py

Clases:
Node: nodo del árbol (clave = fecha string "dd/mm/yyyy", value = temperatura).
AVLTree: árbol AVL con:
Métodos de inserción/borrado/búsqueda: insert, _insert, delete, _delete, search, _search.
Control de balanceo: get_height, get_balance, left_rotate, right_rotate.
Helpers de orden/valor mínimo: get_min_value_node.
Comparación y parsing de fechas: _convert_date(date_str) y _compare_dates(...) para comparar correctamente por día/mes/año.
Consultas por rango: get_records_in_range(fecha1, fecha2) que usa _inorder_range y devuelve lista de (fecha, temperatura) ordenada; y funciones agregadas para rango: max_in_range, min_in_range, extreme_in_range.
Uso: estructura de datos principal para guardar y consultar registros temporales por fecha.
database.py

Clase Temperaturas_DB (fachada sobre AVLTree):
Métodos:
guardar_temperatura(temperatura, fecha) — inserta en el AVL y mantiene contador.
devolver_temperatura(fecha) — busca un registro por fecha.
max_temp_rango(fecha1, fecha2), min_temp_rango(...), temp_extremos_rango(...) — delegan en métodos del AVL.
devolver_temperaturas(fecha1, fecha2) — obtiene lista de registros en rango (delegado).
borrar_temperatura(fecha) — borra y decrementa contador.
cantidad_muestras() — devuelve contador.
cargar_muestras_desde_archivo(filepath) — lee muestras.txt (líneas dd/mm/yyyy;temperatura) y llama guardar_temperatura.
Uso: API usada por el menú y cualquier otro módulo que necesite consultar datos.
leer_muestras.py

Punto de entrada / interfaz CLI:
Crea instancia Temperaturas_DB, carga muestras.txt usando ruta relativa.
Muestra menú con opciones (agregar, buscar por fecha, máximos/mínimos en rango, borrar, listar en rango, total muestras, salir).
Interactúa con el usuario y llama a los métodos de Temperaturas_DB.
Nota: exige formato de fecha dd/mm/yyyy en las entradas.
analyzer.py

Funciones utilitarias (no referenciadas por otros ficheros actualmente):
calcular_promedio_temperaturas(db, fecha1, fecha2)
generar_reporte_temperaturas(db, fecha1, fecha2)
Uso: opcional; actualmente no es importado por el resto del proyecto.
muestras.txt

Datos de entrada: cada línea con dd/mm/yyyy;temperatura (por ejemplo 01/01/2025;23.5).
Temperaturas_DB.cargar_muestras_desde_archivo lo parsea y lo carga automáticamente al iniciar.
Archivos experimentales (prueba.py, prueba2.py, etc.)
Implementaciones parciales/alternativas de árboles. No son necesarios si avl_tree.py está presente y usado por database.py.
Flujo de datos (contrato corto)
Entrada: muestras.txt (texto), entradas del usuario (fechas en dd/mm/yyyy, números float).
Almacenamiento: AVLTree con clave = fecha string, value = float temperatura.
Salida: listas de tuplas (fecha, temperatura), valores numéricos (max/min/promedio), mensajes en consola.
Consideraciones y edge cases
Formato de fecha obligatorio: dd/mm/yyyy; fechas mal formateadas provocan excepción en datetime.strptime.
Duplicados: AVLTree actualiza el valor si la misma fecha ya existe.
Rango: get_records_in_range y los métodos min_in_range/max_in_range usan comparaciones inclusivas [fecha1, fecha2].
Si no hay registros en un rango, los métodos retornan None o listas vacías según corresponda (el CLI muestra mensajes amigables).
Cómo ejecutar (breve)
Desde la carpeta que contiene modules, ejecutar:
python leer_muestras.py
Asegúrate de que muestras.txt está en la misma carpeta modules y las fechas usan dd/mm/yyyy.

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

- Deleon Iván
- Gerbaudo Sabina
- Rogau Virginia Isabel

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
