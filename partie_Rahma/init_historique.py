import json
from datetime import datetime

def init_historique(user_id, username):
    """Initialise ou réinitialise l'historique de l'utilisateur dans users.json."""
    try:
        with open('users.json', 'r+', encoding='utf-8') as file:
            users = json.load(file)

            user = next((user for user in users if user["user_id"] == user_id), None)

            if user:
                user['history'] = []  
                print(f"Historique pour {username} réinitialisé avec succès.")
            else:
                print(f"Utilisateur avec ID {user_id} non trouvé.")
                return  

            file.seek(0)
            json.dump(users, file, indent=4, ensure_ascii=False)
            file.truncate()

    except FileNotFoundError:
        print("Erreur : Le fichier users.json est introuvable.")
        # Créer le fichier s'il n'existe pas
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4, ensure_ascii=False)
    except json.JSONDecodeError:
        print("Erreur : Le fichier users.json contient une erreur de format.")

