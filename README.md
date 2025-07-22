<br />
<div align="center">
  <h1 align="center">Juego Wordle (en castellano)</h1>
</div>

Este es un sencillo juego estilo **Wordle**, desarrollado en Python para jugar desde la terminal. El objetivo del juego es adivinar una palabra de 5 letras en un máximo de 6 intentos. Cada intento ofrece pistas visuales mediante colores para indicar la precisión de las letras introducidas.

## ¿Cómo jugar?

Al ejecutar el programa, se mostrará un menú con la explicación de los colores:

* 🟩 **Verde**: La letra es correcta y está en la posición correcta.
* 🟨 **Amarillo**: La letra está en la palabra pero en otra posición.
* 🟥 **Rojo**: La letra no está en la palabra.

¡Importante! Todas las palabras deben tener **exactamente 5 letras**.

## Archivos necesarios

* `main.py`: el código del juego, cuyo funcionamiento está completamente explicado paso a paso en comentarios detallados.
* `diccionario.txt`: un archivo de texto con palabras válidas en el diccionario de la RAE (no las incluye todas, se puede ampliar manualmente).

## Requisitos
Para poder ejecutar este programa es imprescindible tener **Python** instalado, puedes descargar la última versión desde [el sitio web oficial de Python](https://www.python.org/). *Este programa ha sido probado con Python 3.12*

## Ejecución del juego

1. Asegúrate de tener el archivo `diccionario.txt` en el mismo directorio que `main.py`. Este archivo debe contener una lista de palabras en minúsculas, sin caracteres especiales ni números. Los acentos o diéresis se normalizan automáticamente.

2. Ejecuta el script en consola:

```bash
python main.py
```

3. El juego seleccionará una palabra aleatoria de 5 letras del diccionario y te pedirá que introduzcas tus intentos. Tienes un máximo de **6 intentos** para adivinar la palabra correcta.

## Futuras actualizaciones
...
