import json
import os

def load_users():
    """Charge les questions depuis le fichier users.json."""
    # Utilisation d'un chemin relatif
    file_path = os.path.join(os.path.dirname(__file__), "users.json")  # Remplacez par le chemin relatif
    
    try:
       with open('users.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Erreur : Le fichier users.json est introuvable à l'emplacement {file_path}.")
    except json.JSONDecodeError:
        raise ValueError("Erreur : Le fichier users.json contient une erreur de format.")

