minuts = int(input("Introdueix un numero per als minuts:"))

hores = minuts // 60

minuts_sobrants = minuts % 60

print(f"Aquest es el resultat:{hores} hores i {minuts_sobrants} minuts")