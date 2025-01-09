import json


# Gestion de la connexion de l'utilisateur
def get_user(users):
    user_id = input("Entrez votre identifiant : ").strip()
    if user_id not in users:
        print("Nouvel utilisateur. Création du profil...")
        users[user_id] = {"history": []}
    else:
        print(f"Bienvenue de retour, {user_id}! Voici votre historique :")
        if users[user_id]["history"]:
            for entry in users[user_id]["history"]:
                print(f"Date: {entry['date']}, Score: {entry['score']}")
        else:
            print("Aucun historique trouvé.")
    return user_id
