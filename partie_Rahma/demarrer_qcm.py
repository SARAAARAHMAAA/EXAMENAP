import load_questions
import poser_questions


def demarrer_qcm(username):
    """Démarre le QCM pour un utilisateur donné."""
    # Charger les questions
    questions = load_questions.load_questions()
    print(f"Questions chargées : {questions}") 
    if not questions:
        print("Aucune question disponible. Veuillez vérifier le fichier questions.json.")
        return

    # Poser les questions
    score, _ = poser_questions.poser_questions(questions)

    # Afficher le score final
    print(f"\n{username}, votre score final est : {score}/12")

    # Mettre à jour l'historique
    mettre_a_jour_historique.mettre_a_jour_historique(username, score)
