import json
import load_users  
import get_user
import main_menu
import save_users
import demarrer_qcm
import mettre_a_jour_historique

def main():
    users = load_users.load_users()
    user_id = get_user.get_user(users)
    print(f"Utilisateur sélectionné : {user_id}")
    
    while True:
        choice = main_menu.main_menu()
        
        if choice == "1":
            print("Démarrage du QCM...")
            demarrer_qcm.demarrer_qcm(user_id)
        
        elif choice == "2":
            user = next((user for user in users if user['user_id'] == user_id), None)
            if user and user["history"]:
                print(f"Historique de {user['username']}:")
                for entry in user["history"]:
                    print(f"Date: {entry['date']}, Score: {entry['score']}")
            else:
                print("Aucun historique trouvé.")
        
        elif choice == "3":
            user_id = get_user.get_user(users)  # Permet de changer d'utilisateur
            print(f"Utilisateur sélectionné : {user_id}")
        
        elif choice == "4":
            print("Au revoir!")
            break
        
        else:
            print("Option invalide, veuillez réessayer.")

    # Sauvegarder les utilisateurs mis à jour
    save_users.save_users(users)

if __name__ == "__main__":
    main()
