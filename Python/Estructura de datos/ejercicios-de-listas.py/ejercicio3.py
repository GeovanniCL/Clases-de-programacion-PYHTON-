"""
Tienes una lista de temperaturas en grados Celsius de varios días,
y necesitas convertirlas a Fahrenheit y luego identificar las temperatura
que están por encima de 75 grados Fahrenheit.
"""

temperatura_celciu = [0, 10, 21,2 ,60, 10, 120, 20 ,30]


print("temperaturas en Fahrenheit mayores a 75 grados son:")
for x in temperatura_celciu:
    fahrenheit = x * 1.8 + 32
    if fahrenheit > 75:
        print(x)