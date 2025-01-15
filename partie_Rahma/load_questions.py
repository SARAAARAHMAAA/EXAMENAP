import json
import os

def load_questions():
    """Charge les questions depuis le fichier questions.json."""
    # Utilisation d'un chemin relatif
    file_path = os.path.join(os.path.dirname(__file__), "questions.json")  # Remplacez par le chemin relatif
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Erreur : Le fichier questions.json est introuvable à l'emplacement {file_path}.")
    except json.JSONDecodeError:
        raise ValueError("Erreur : Le fichier questions.json contient une erreur de format.")

