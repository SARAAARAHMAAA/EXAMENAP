import json
import load_users
import get_user
import main_menu
import save_users

# Fonction principale
def main():
    users = load_users()
    user_id = get_user(users)

    while True:
        choice = main_menu()
        if choice == "1":
            print("Démarrage du QCM... (cette partie sera gérée par la deuxième personne)")
            # Appel à une fonction pour démarrer le QCM ici
        elif choice == "2":
            if users[user_id]["history"]:
                print("Historique des QCM :")
                for entry in users[user_id]["history"]:
                    print(f"Date: {entry['date']}, Score: {entry['score']}")
            else:
                print("Aucun historique disponible.")
        elif choice == "3":
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

    save_users(users)

if __name__ == "__main__":
    main()