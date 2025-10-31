# 🐍 Sala de emergencias

Breve descripción del proyecto:

“Este código simula la actividad de recepción en una sala de emergencias. Se reciben a los pacientes tomando nombre, apellido y nivel de riesgo (1 alto, 2 moderado, 3 bajo). En particular se decidió tomar la hora de llegada de cada paciente, para el caso en que cuenten con un mismo nivel de riesgo; será atendido aquel que ha llegado primero.Se utilizan estructuras de datos jerárquicas (montículo binario) para resolver el problema planteado"

---
## 🏗Arquitectura General

El presente código cuenta, en la carpeta modules, con:
   -Clase Cola_de_prioridad: Se encarga de recibir los datos de los pacientes y evalúar su porioridad. Por cada paciente ingresado elimina el primero en la cola de espera. Cuenta con funciones fundamentales para realizar este procedimiento como:
      -Encolar: Añade un elemento al montículo.
      -Desencolar:Extrae el elemento de mayor prioridad del montículo.
   -Clase Montículo_binario: Recibe los datos de la cola de prioridad y organiza según el nivel determinado por la misma. En este caso se utilizó un monticulo mínimo, el cual toma al elemento de menor valor como el de mayor prioridad. Una de las funciones que permite dicha actividad es la de eliminarMin, la cual se encarga de eliminar el elemento en la raíz del montículo; es decir atender al paciente de mayor prioridad.
   -Clase paciente: Se encarga de crear los pacientes (nombre y apellido), nivel de riesgo y hora de llegada, todos aleatorios. Los organiza en una cadena de texto, y compara su hora de llegada o nivel de riesgo según corresponda. 
   -Clase salita: Simula el ambiente de una sala de emergencias utiliza todas las clases anteriores para su funcionamiento. 

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
- Rogau Virginia isabel 

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
