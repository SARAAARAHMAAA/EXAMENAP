import json
import load_users
from colorama import Fore, Style, init

# Initialiser Colorama
init(autoreset=True)

def get_user(users):
    """Récupère ou crée un utilisateur en fonction de son nom d'utilisateur."""
    
    # Charger les utilisateurs existants
    data = load_users.load_users()
    users = data
    
    # Demander le nom d'utilisateur
    print(Fore.CYAN + Style.BRIGHT + "\n🔍 Identification utilisateur")
    user_name = input(Fore.YELLOW + "Entrez votre nom d'utilisateur : ").strip()

    # Chercher l'utilisateur dans la liste
    user = next((user for user in users if user["username"].lower() == user_name.lower()), None)

    if not user:
        # Créer un nouveau profil utilisateur
        user_id = len(users) + 1 
        print(Fore.GREEN + f"\n🆕 Nouvel utilisateur détecté. Création du profil avec ID {user_id}...")
        user = {"user_id": user_id, "username": user_name, "history": []}
        users.append(user)
    else:
        # L'utilisateur existe déjà
        user_id = user["user_id"]
        print(Fore.GREEN + f"\n👋 Bienvenue de retour, {user['username']}!")

    # Sauvegarder les utilisateurs dans le fichier users.json
    try:
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)
        print(Fore.BLUE + "\n✅ Profil utilisateur mis à jour avec succès.")
    except Exception as e:
        print(Fore.RED + f"\n❌ Erreur lors de la mise à jour du fichier : {e}")

    return user_id
