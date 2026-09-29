# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 29/09/2026
# Versió: 1
#
# Descripció: Fes un programa que demani:Nom, Cognom, Ciutat, Institut, Cicle formatiu i Mòdul preferit.
# Especificacions d'Entrada: programa que comta quants caracter te aquella paraula posada per l'usuari.


nom = input("Introdueix el teu nom: ")
cognom = input("Introdueix el teu cognom: ")
ciutat = input("Introdueix la teva ciutat: ")
institut = input("Introdueix el teu institut: ")
cicle = input("Introdueix el teu cicle formatiu: ")
modul = input("Introdueix el teu mòdul preferit: ")

print("\n=== Resum de les dades ===")
print("Nom complet: " + nom + " " + cognom)
print("Ciutat de residència: " + ciutat)
print("Centre d'estudis: " + institut)
print("Cicle que estàs cursant: " + cicle)
print("El teu mòdul preferit és: " + modul)
print("==========================")