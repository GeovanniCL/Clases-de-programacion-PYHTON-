#mecanografia 

import random
import time

# Lista de textos largos para practicar
texts = [
    "La programación es una herramienta poderosa que nos permite resolver problemas complejos de manera creativa y eficiente.",
    "Practicar mecanografía mejora no solo la velocidad de escritura, sino también la precisión y la confianza en el teclado.",
    "Python es un lenguaje de programación versátil, popular tanto en ciencia de datos como en desarrollo web y automatización.",
    "La constancia y la paciencia son claves fundamentales para aprender cualquier habilidad nueva, incluida la mecanografía."
]

def typing_practice():
    # Selección aleatoria de un texto
    text = random.choice(texts)
    print("\nTexto para escribir:")
    print(text)
    print("\nEscribe el texto exactamente como aparece arriba y presiona Enter cuando termines.\n")

    # Inicio del cronómetro
    start_time = time.time()

    # Entrada del usuario
    user_input = input("Tu entrada: ")

    # Fin del cronómetro
    end_time = time.time()

    # Cálculo de tiempo transcurrido
    elapsed_time = end_time - start_time

    # Comparar texto original con entrada del usuario
    errors = sum(1 for orig, typed in zip(text, user_input) if orig != typed) + abs(len(text) - len(user_input))
    precision = max(0, (len(text) - errors) / len(text) * 100)  # Evita precisión negativa

    # Calcular palabras por minuto (WPM)
    words = len(text.split())
    wpm = (words / elapsed_time) * 60

    # Mostrar resultados
    print("\n--- Resultados ---")
    print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")
    print(f"Precisión: {precision:.2f}%")
    print(f"Velocidad: {wpm:.2f} palabras por minuto")
    print(f"Errores: {errors}")

# Ejecutar el programa
typing_practice()
