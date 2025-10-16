# Juego de Cartas (Guerra)

Breve descripción del proyecto:

Se implementa el TAD mazo a Python utilizando la clase ListaDoblementeEnlazada creada previamente, para poder recrear una partida del juego de cartas "Guerra" entre dos personas.

---
## 🏗Arquitectura General

Clase DequeEmptyError: Excepción personalizada que se lanza cuando se intenta sacar una carta de un mazo vacío.
Clase Mazo: Representa un mazo de cartas usando una lista doblemente enlazada (ListaDobleEnlazada).
Método __init__: Inicializa el mazo vacío.
Método poner_carta_arriba(carta): Agrega una carta al inicio del mazo.
Método poner_carta_abajo(carta): Agrega una carta al final del mazo.
Método sacar_carta_arriba(mostrar=False): Quita y devuelve la carta del inicio del mazo, mostrando un mensaje si se indica.
Método __len__: Devuelve la cantidad de cartas en el mazo.


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
