import json


# Sauvegarde des utilisateurs et de l'historique dans un fichier JSON
def save_users(users, filename="users.json"):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)
    print("Utilisateurs sauvegardés avec succès.")
