import time
import threading
import csv
import sys
from colorama import Fore, Style, init

# Initialiser colorama
init(autoreset=True)

def compte_a_rebours(temps_max, stop_event):
    """Affiche un compte à rebours dynamique pendant que l'utilisateur répond."""
    for secondes_restantes in range(temps_max, 0, -1):
        if stop_event.is_set():
            break
        sys.stdout.write(Fore.CYAN + f"\r( Temps restant : {secondes_restantes} secondes ) => Votre réponse (1-4) : ")
        sys.stdout.flush()
        time.sleep(1)
    if not stop_event.is_set():
        sys.stdout.write(Fore.RED + "\nTemps écoulé ! Réponse non prise en compte.\n")


def poser_questions(questions, chrono_limite=30):
    """Pose les questions à l'utilisateur avec un chronomètre visible."""
    categories = list(questions.keys())
    print(Fore.GREEN + "\nCatégories disponibles :")
    for i, categorie in enumerate(categories, start=1):
        print(f"{i}. {categorie}")
    
    choix = int(input(Fore.YELLOW + "Choisissez une catégorie (numéro) : "))
    categorie_choisie = categories[choix - 1]
    
    score = 0
    total_questions = len(questions[categorie_choisie])

    print(Fore.MAGENTA + f"\nVous avez choisi la catégorie : {categorie_choisie}\n")

    for index, question in enumerate(questions[categorie_choisie]):
        print(Fore.BLUE + f"\nQuestion {index + 1}/{total_questions}: {question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        
        stop_event = threading.Event()
        chrono_thread = threading.Thread(target=compte_a_rebours, args=(chrono_limite, stop_event))
        chrono_thread.start()
        
        reponse = None
        debut = time.time()
        
        while not stop_event.is_set():
            try:
                reponse = input().strip()
                # Vérification si la réponse est un chiffre et dans l'intervalle 1-4
                if reponse.isdigit():
                    reponse = int(reponse)
                    if reponse < 1 or reponse > 4:
                        print(Fore.RED + "Erreur : Choisissez un numéro entre 1 et 4.")
                        reponse = None  # Réinitialiser la réponse pour redemander
                    else:
                        stop_event.set()  # Arrêter le chrono dès que la réponse est saisie
                        break
                else:
                    print(Fore.RED + "Erreur : Veuillez entrer un numéro valide.")
            except ValueError:
                print(Fore.RED + "Erreur : Entrée invalide. Veuillez entrer un numéro.")
        
        chrono_thread.join()  # Assurez-vous que le chrono s'arrête correctement
        if reponse:
            index_reponse = reponse - 1
            if question['options'][index_reponse] == question['bonne_reponse']:
                print(Fore.GREEN + "Bonne réponse ! 🎉")
                score += 1
            else:
                print(Fore.RED + f"Mauvaise réponse. La bonne réponse était : {question['bonne_reponse']}.")
        
        # Affichage des statistiques en temps réel
        print(Fore.CYAN + f"Score actuel : {score}/{index + 1}")

    return score, total_questions



def enregistrer_resultats(nom_utilisateur, score, total_questions):
    """Enregistre les résultats dans un fichier CSV."""
    with open("resultats.csv", mode="a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom_utilisateur, score, total_questions])



def show_final_message(score, total_questions):
    """Affiche un message personnalisé en fonction du score."""
    if score / total_questions >= 0.8:
        print(Fore.GREEN + f"\nExcellent travail ! 🎉 Vous avez obtenu {score}/{total_questions}. Vous êtes un champion ! 🏆")
    elif score / total_questions >= 0.5:
        print(Fore.YELLOW + f"\nPas mal ! 👍 Vous avez obtenu {score}/{total_questions}. Continuez à vous améliorer ! 💪")
    else:
        print(Fore.RED + f"\nVous avez obtenu {score}/{total_questions}. Ne vous découragez pas, entraînez-vous encore ! 💡")


# Exemple d'utilisation
if __name__ == "__main__":
    questions = {
        "Python": [
            {"question": "Que fait la fonction len() ?", 
             "options": ["Retourne la longueur", "Ajoute un élément", "Trie la liste", "Supprime un élément"], 
             "bonne_reponse": "Retourne la longueur"},
            {"question": "Comment définir une fonction ?", 
             "options": ["def nom_fonction()", "function nom_fonction", "func nom_fonction()", "create nom_fonction"], 
             "bonne_reponse": "def nom_fonction()"}
        ],
        "Réseaux": [
            {"question": "Quel est le protocole utilisé pour envoyer des e-mails ?", 
             "options": ["HTTP", "SMTP", "FTP", "IMAP"], 
             "bonne_reponse": "SMTP"}
        ]
    }
    

    nom_utilisateur = input(Fore.YELLOW + "Entrez votre nom : ").strip()
    score, total_questions = poser_questions(questions)
    show_final_message(score, total_questions)
    enregistrer_resultats(nom_utilisateur, score, total_questions)
    print(Fore.CYAN + "\nRésultats enregistrés dans 'resultats.csv'. Merci de votre participation !")
