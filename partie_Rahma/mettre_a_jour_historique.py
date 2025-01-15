import json
from datetime import datetime

def mettre_a_jour_historique(user_id, username, score):
    """Met à jour l'historique de l'utilisateur avec son score et la date."""
    try:
        # Vérifier que le score est valide (non nul)
        if score is None:
            print(f"Erreur : Le score ne peut pas être nul.")
            return
        
        # Ouvrir le fichier en mode lecture/écriture
        with open('users.json', 'r+', encoding='utf-8') as file:
            # Essayer de charger les utilisateurs du fichier JSON
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                # Si le fichier est vide ou corrompu, on initialise une liste vide
                users = []

            user_id = int(user_id)
            user = next((user for user in users if user["user_id"] == user_id), None)

            # Si l'utilisateur existe, on met à jour son historique, sinon on l'ajoute
            if user:
                user['history'].append({
                    'score': score,
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                # Ajout d'un nouvel utilisateur avec son historique
                users.append({
                    'user_id': user_id,
                    'username': username,
                    'history': [{
                        'score': score,
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }]
                })

            # Revenir au début du fichier et réécrire les données mises à jour
            file.seek(0)
            json.dump(users, file, indent=4, ensure_ascii=False)
            file.truncate()  # Assure que les anciennes données sont supprimées

    except FileNotFoundError:
        print("Erreur : Le fichier users.json est introuvable.")
    except json.JSONDecodeError:
        print("Erreur : Le fichier users.json contient une erreur de format.")
