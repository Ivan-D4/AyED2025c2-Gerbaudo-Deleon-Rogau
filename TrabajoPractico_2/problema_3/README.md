# 🐍 Palomas mensajeras

Breve descripción del proyecto:

“Para este código se planteó la problematica de llevar un mensaje desde una aldea determinada, hacia cierto número de aldeas vecinas. Para esto se implementó el uso de una estructura de datos no lineal denominada grafo, adémas de una cola de prioridad ligada a un montículo mínimo."

---
## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)
El código, en la carpeta modules, cuenta con:
   -Aldeas.txt: Archivo provisto, que contiene tuplas con (mensajero, destinatario, distancia entre ambos)
   -Clase cola_de_prioridad: Se encarga, junto con el montículo minimo, de seleccionar la menor distancia(aristas) entre vértices (aldeas).
   -Clase Vértice: Representa cada aldea dentro del grafo. 
   -Clase grafo: Gestiona los vértices y las conexiones, dándole la estructura correspondiente.
   -Función Prim: Conecta todos los vertices del grafo con el menor costo o ponderación posibles. Aplicado al problema encuentra la ruta más optima para el envio de los mensajes.

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

- Deleon Iván 
- Gerbaudo Sabina
- Rogau Virgina Isabel

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
