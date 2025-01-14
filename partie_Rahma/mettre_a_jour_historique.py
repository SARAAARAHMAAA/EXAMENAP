from datetime import datetime
import json

def mettre_a_jour_historique(username, score):
    """Met à jour l'historique de l'utilisateur avec son score et la date."""
    try:
        with open('users.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)

            # Trouver l'utilisateur
            utilisateur = next((u for u in data['utilisateurs'] if u['nom'] == username), None)

            if utilisateur:
                # Ajouter le score et la date
                utilisateur['historique'].append({
                    'score': score,
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                # Si l'utilisateur n'existe pas, le créer
                data['utilisateurs'].append({
                    'nom': username,
                    'historique': [{
                        'score': score,
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }]
                })

            # Sauvegarder les modifications
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.truncate()

    except FileNotFoundError:
        print("Erreur : Le fichier users.json est introuvable.")
    except json.JSONDecodeError:
        print("Erreur : Le fichier users.json contient une erreur de format.")
