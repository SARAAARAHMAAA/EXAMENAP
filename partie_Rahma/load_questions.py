import json

def load_questions():
    """Charge les questions depuis le fichier questions.json."""
    file_path = r"C:\Users\Condor\Downloads\examen tp ap\version 3\questions.json"  # Remplacez par le chemin absolu
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Erreur : Le fichier questions.json est introuvable.")
        return []
    except json.JSONDecodeError:
        print("Erreur : Le fichier questions.json contient une erreur de format.")
        return []
