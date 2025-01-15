from datetime import datetime
import json

def mettre_a_jour_historique(username, score):
    """Met à jour l'historique de l'utilisateur avec son score et la date."""
    try:
        with open('users.json', 'r+', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("Erreur : Le fichier JSON est corrompu. Réinitialisation.")
                data = {"users": {}}

            # Vérifier si la clé 'users' existe et est un dictionnaire
            if not isinstance(data.get('users'), dict):
                data['users'] = {}

            # Trouver ou créer l'utilisateur
            if username not in data['users']:
                data['users'][username] = {"history": []}

            # Ajouter le score et la date à l'historique
            data['users'][username]['history'].append({
                'score': score,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

            # Sauvegarder les modifications
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.truncate()

    except FileNotFoundError:
        print("Erreur : Le fichier users.json est introuvable.")
        # Créer un nouveau fichier avec la structure attendue
        with open('users.json', 'w', encoding='utf-8') as file:
            data = {
                "users": {
                    username: {
                        "history": [{
                            'score': score,
                            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }]
                    }
                }
            }
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
