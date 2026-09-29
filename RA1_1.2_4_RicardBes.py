# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 29/09/2026
# Versió: 1
#
# Descripció: Crea una petita calculadora que demani dos números i la operació que vol fer i la mostri per pantalla.
# Especificacions d'Entrada: Calculadora que mostri la operacio per pantalla

primer_numero = float(input("Introdueix el primer número: "))

operacio = input("Introdueix l'operació (+, -, *, /): ")

segon_numero = float(input("Introdueix el segon número: "))

print(f"El resultat de la teva operacio es: {primer_numero} {operacio} {segon_numero}")