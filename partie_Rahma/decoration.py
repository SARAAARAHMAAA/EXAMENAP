import time
import os

# Fonction pour effacer l'écran
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour afficher un texte avec animation
def animated_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Saut de ligne après le texte

# Fonction pour l'intro stylisée
def show_intro():
    clear_screen()

    # ASCII Art pour "S.Y.S   QCM"
    title = """
         ███████╗██╗   ██╗███████╗     ██████╗  ██████╗███╗   ███╗
         ██╔════╝╚██╗ ██╔╝██╔════╝    ██╔═══██╗██╔════╝████╗ ████║
         ███████╗ ╚████╔╝ ███████╗    ██║   ██║██║     ██╔████╔██║
         ╚════██║  ╚██╔╝  ╚════██║    ██║▄▄ ██║██║     ██║╚██╔╝██║
         ███████║██╗██║██╗███████║    ╚██████╔╝╚██████╗██║ ╚═╝ ██║
         ╚══════╝╚═╝╚═╝╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝╚═╝     ╚═╝
       
           """

    tagline = "✨ S.Y.S QCM – Testez vos connaissances ! ✨\n"
    animated_text(title, delay=0.01)
    animated_text(tagline, delay=0.05)

    # Animation de barre de chargement
    print("\nChargement du QCM, veuillez patienter...")
    for i in range(1, 31):
        print(f"\r[{('=' * i).ljust(30)}] {i * 3.33:.0f}%", end='', flush=True)
        time.sleep(0.05)
    
    print("\n\n✅ Chargement terminé ! Bonne chance ! 💪")
    time.sleep(1)

# Exemple d'utilisation
if __name__ == "__main__":
    show_intro()
    # Début du QCM
    print("Bienvenue dans le QCM ! 🎉 Répondez aux questions ci-dessous.")
