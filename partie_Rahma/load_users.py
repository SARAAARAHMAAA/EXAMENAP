import json

# Chargement des utilisateurs depuis un fichier JSON
def load_users(filename="users.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Aucun fichier d'utilisateurs trouvé, création d'un nouveau fichier.")
        return {}
    except json.JSONDecodeError:
        print("Erreur de lecture du fichier JSON. Le fichier est peut-être corrompu.")
        return {}
