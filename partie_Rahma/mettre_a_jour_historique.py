import json
from datetime import datetime

def mettre_a_jour_historique(user_id,username, score):
    """Met à jour l'historique de l'utilisateur avec son score et la date."""
    try:
        with open('users.json', 'r+', encoding='utf-8') as file:
            users = json.load(file)
            user_id = int(user_id)
            user = next((user for user in users if user["user_id"] == user_id), None)

            if user:
                user['history'].append({
                    'score': score ,
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                users.append({
                    'user_id': user_id,
                    'username': username, 
                    'history': [{
                        'score': score,
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }]
                })

            file.seek(0)
            json.dump(users, file, indent=4, ensure_ascii=False)
            file.truncate()

    except FileNotFoundError:
        print("Erreur : Le fichier users.json est introuvable.")
    except json.JSONDecodeError:
        print("Erreur : Le fichier users.json contient une erreur de format.")
