import random

# Demande le nombre de participants
nombre_participants = int(input("Entrez le nombre de participants : "))

# Initialise la liste des participants
participants = []

# Boucle pour collecter les noms
for i in range(nombre_participants):
    nom = input(f"Entrez le nom du participant {i + 1} : ")
    participants.append(nom)

# Affiche la liste pour vérifier
print("Liste des participants :", participants)

# On suppose que participants est déjà rempli
random.shuffle(participants)

# Créons un dictionnaire pour stocker les paires Secret Santa
santa_pairs = {}

# Assigner chaque participant au suivant dans la liste
for i in range(len(participants)):
    donneur = participants[i]
    receveur = participants[(i + 1) % len(participants)]  # Boucle pour que le dernier donne au premier
    santa_pairs[donneur] = receveur

# Afficher les résultats
print("Paires Secret Santa :")
for donneur, receveur in santa_pairs.items():
    print(f"{donneur} offre un cadeau à {receveur}")
