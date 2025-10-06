# Liste initiale des adresses IP
adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

# Q1 - Afficher la première adresse IP
print("La première adresse est :", adresses_ip[0])

# Q2 - Afficher la dernière adresse IP
print("La dernière adresse est :", adresses_ip[-1])

# Q3 - Afficher la troisième adresse IP
print("La troisième adresse est :", adresses_ip[2])

# Q4 - Ajouter une nouvelle adresse IP à la liste
adresses_ip.append("172.31.0.1")

# Q5 - Supprimer une adresse IP spécifique
adresses_ip.remove("200.100.50.1")

# Afficher la liste mise à jour
print("Liste après modification :", adresses_ip)

# Q6 - Afficher le nombre total d’adresses restantes
print(f"Le nombre d’éléments restants est : {len(adresses_ip)}")

# Q7 - Vérifier si une adresse IP spécifique est présente dans la liste
if "192.168.0.1" in adresses_ip:
    print("L’adresse 192.168.0.1 se trouve dans la liste.")
else:
    print("L’adresse 192.168.0.1 ne se trouve pas dans la liste.")

# Q8 - Déterminer la classe d’une adresse IP donnée
ip = "10.0.0.1".split('.')
premier_octet = int(ip[0])
if 0 < premier_octet < 128:
    print("L’adresse 10.0.0.1 appartient à la classe A.")
else:
    print("L’adresse 10.0.0.1 n’appartient pas à la classe A.")

# Q9 - Trier la liste des adresses IP
adresses_ip.sort()
print("Liste triée :", adresses_ip)

# Q10 - Vérifier si toutes les adresses sont de la classe C
compteur_classe_c = 0
for adresse in adresses_ip:
    premier_octet = int(adresse.split('.')[0])
    if 192 <= premier_octet <= 223:
        compteur_classe_c += 1

if compteur_classe_c == len(adresses_ip):
    print("Toutes les adresses sont de  classe C.")
else:
    print("La liste contient des adresses qui n’appartiennent pas à la classe C.")

# Q11 - Compter le nombre d’adresses publiques (commençant par 200)
compteur_publique = 0
for adresse in adresses_ip:
    premier_octet = int(adresse.split('.')[0])
    if premier_octet == 200:
        compteur_publique += 1

print("Le nombre d’adresses de classe publique est :", compteur_publique)
