# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 29/09/2026
# Versió: 1
#
# Descripció: Demana una frase i una paraula que vulguis substituir i després substitueix-la per una altra paraula.
# Especificacions d'Entrada: Frase que canvie mentres contestes les preguntes del programa.

frase = input("introdueix una frase: ")

paraula_sub = input("Quina paraula vols substituir? ")

paraula_nova = input("Nova paraula: ")

frase_nova = frase.replace("paraula_sub", "paraula_nova")