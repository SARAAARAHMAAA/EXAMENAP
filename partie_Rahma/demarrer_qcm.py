import load_questions
import poser_questions
import mettre_a_jour_historique


def demarrer_qcm(user_id):
    """Démarre le QCM pour un utilisateur donné."""
    # Charger les questions
    questions = load_questions.load_questions()
    if not questions:
        print("Aucune question disponible. Veuillez vérifier le fichier questions.json.")
        return

    # Poser les questions
    score, _ = poser_questions.poser_questions(questions)

    # Afficher le score final
    print(f"\n{user_id}, votre score final est : {score}/12")

    try:
        mettre_a_jour_historique.mettre_a_jour_historique(user_id, score)
        print(f"L'historique pour {user_id} a été mis à jour avec succès.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour de l'historique : {e}")