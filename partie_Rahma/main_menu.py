import json
from colorama import Fore, Style, init

# Initialiser Colorama
init(autoreset=True)

def main_menu():
    """Affiche le menu principal dans un cadre rectangulaire."""
    print(Fore.CYAN + Style.BRIGHT + "+" + "-" * 40 + "+")
    print(Fore.CYAN + Style.BRIGHT + "|          " + Fore.YELLOW + "MENU PRINCIPAL" + Fore.CYAN + "            |")
    print(Fore.CYAN + Style.BRIGHT + "+" + "-" * 40 + "+")
    print(Fore.GREEN + "|  1. 🏁 Démarrer un QCM                 |")
    print(Fore.GREEN + "|  2. 📜 Afficher l'historique           |")
    print(Fore.GREEN + "|  3. 🔄 Changer d'utilisateur           |")
    print(Fore.GREEN + "|  4. 🧹 Initialiser votre historique    |")
    print(Fore.RED + "|  5. ❌ Quitter                         |")
    print(Fore.CYAN + Style.BRIGHT + "+" + "-" * 40 + "+")
    choix = input(Fore.CYAN + "👉 Choisissez une option (1-5) : ").strip()
    return choix
