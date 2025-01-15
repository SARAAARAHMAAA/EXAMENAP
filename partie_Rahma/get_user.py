import json

def get_user(users):
    with open('users.json', 'r', encoding='utf-8') as file:
        users = json.load(file)
    
    user_name = input("Entrez votre nom d'utilisateur : ").strip()

    user = next((user for user in users if user["username"] == user_name), None)

    if not user:
        user_id = len(users) + 1 
        print(f"Nouvel utilisateur. Création du profil avec ID {user_id}...")
        users.append({"user_id": user_id, "username": user_name, "history": []})
        user = {"user_id": user_id, "username": user_name, "history": []}
    else:
        user_id = user["user_id"]
        print(f"Bienvenue de retour, {user['username']}!")

    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

    return user_id  
