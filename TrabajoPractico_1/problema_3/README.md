# Implementacion algoritmos de ordenamiento 

Breve descripción del proyecto:

Este es un script en el que se comparan algoritmos de ordenamiento. Permite mostrar en una grafica en base al tiempo que tarda la ejecucion de cada tipo de ordenamiemto para comparar y detrminar los mas eficientes.

---
## 🏗Arquitectura General

Este proyecto esta conformado por tres codigos de ordenamiento:
*P3_Oburbuja.py*
Contiene la función ordenamiento_burbuja(lista) que implementa el algoritmo de ordenamiento burbuja.
El código principal genera una lista de números aleatorios y la ordena usando esta función.
No utiliza clases, solo funciones.
*P3_Oquicksort.py*
Define la función principal ordenamiento_quicksort(lista) que llama recursivamente a ordenamiento_quicksortAuxiliar.
Utiliza la función particion para dividir la lista según el pivote.
Todo el ordenamiento se realiza mediante funciones, sin clases.
*P3_Oradix.py*
Implementa el algoritmo Radix Sort en la función ordenamiento_radix(lista).
Usa la función auxiliar obtener_digito para extraer dígitos de los números.
El código principal genera una lista de números aleatorios y la ordena.
Solo utiliza funciones, no clases.

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
