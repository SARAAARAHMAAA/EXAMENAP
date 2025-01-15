import json


# Sauvegarde des utilisateurs et de l'historique dans un fichier JSON
def save_users(users, filename="users.json"):
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
    print("Utilisateurs sauvegardés avec succès.")
