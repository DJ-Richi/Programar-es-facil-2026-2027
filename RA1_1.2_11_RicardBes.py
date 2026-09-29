# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 29/09/2026
# Versió: 1
#
# Descripció: Demana una frase que contingui espais al principi i al final i elimina aquests espais.
# Especificacions d'Entrada: Frase que tingui espais al principi i al final ademes que elimina aquests espais.

frase = input("Introdueix una frase: ")

longitud_frase = len(frase)

frase_nova = frase[1:longitud_frase -1]

print(frase_nova)