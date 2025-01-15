import json
import load_users  
import get_user
import main_menu
import save_users
import demarrer_qcm
import init_historique
import mettre_a_jour_historique
import decoration

def main():
    data = load_users.load_users()
    user_id = get_user.get_user(data)
    print(f"Utilisateur sélectionné : {user_id}")
    
    user = next((user for user in data if user['user_id'] == user_id), None)

    while True:
        choice = main_menu.main_menu()
        
        if choice == "1":
            print("Démarrage du QCM...")
            demarrer_qcm.demarrer_qcm(user_id)
            users = load_users.load_users()
        
        elif choice == "2":
            users = load_users.load_users()
            user = next((user for user in data if user['user_id'] == user_id), None)
            if user and user["history"]:
                print(f"Historique de {user['username']}:")
                for entry in user["history"]:
                    print(f"Date: {entry['date']}, Score: {entry['score']}")
            else:
                print("Aucun historique trouvé.")
        
        elif choice == "3":
            user_id = get_user.get_user(data)  # Permet de changer d'utilisateur
            print(f"\n\nUtilisateur sélectionné : {user_id}\n\n\n")

        elif choice == "4":
            init_historique.init_historique(user["user_id"], user["username"])
            users = load_users.load_users()
        elif choice == "5":
            print("Au revoir!")
            save_users.save_users(users)
            break
        
        else:
            print("Option invalide, veuillez réessayer.")

    # Sauvegarder les utilisateurs mis à jour
    save_users.save_users(users)

if __name__ == "__main__":
    decoration.show_intro()
    main()
