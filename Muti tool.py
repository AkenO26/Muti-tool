#!/usr/bin/env python
import pyautogui
import time
import random
import pyperclip

print("Multi-tools")
print("=" * 25)

print("Choisir un outil dans la liste : \n 1 - Spammer\n 2 - Pass gen")
tool = int(input(" Choix : "))

if tool == 1:
    continuer_spammer = 'o'

    while continuer_spammer == 'o':
        entree = input("Quel text ? ")

        nb = int(input("Combien de fois ?"))

        delai = int(input("Quel délai ? (ms)"))

        print("5 secondes")
        time.sleep(5)

        for i in range(0, nb):
            if entree != "":
                pyautogui.typewrite(entree)
                pyautogui.press("enter")
            else:
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press("enter")

            time.sleep(delai / 1000)
        print("Envoyé {0} fois !  ".format(nb))

        continuer_spammer = input("Encore ? o/n")






elif tool == 2:

    print("Générateur de mot de passe")
    print("=" * 25)
    continuer_gen = 'o'

    while continuer_gen == 'o':
        file = open('password.txt', 'a+')
        long = int(input("Combien de caractères ? "))

        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        charsp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
        charsp_oui_non = input("Avec des caractères spéciaux ? (o/n)")

        if charsp_oui_non == 'o':
            chars = charsp
        elif charsp_oui_non == 'n':
            print("")
        else:
            print("Réponse non valide\n/sans caractères spéciaux...\ ")

        password = ''
        for c in range(long):
            password += random.choice(chars)
        print("Le mot de pass générer est {0} il a été copié dans le presse-papier.".format(password))
        pyperclip.copy(password)
        file.write("\nGénérer le {0} le mot de passe est : {1}".format(time.asctime(), password))
        file.close()

        continuer_gen = input("Encore ? (o/n)")
        print("Tout les mots de passe dans le fichier /password.txt")







else:
    print("Pas encore pret")

print("=" * 25)
print("Fin")
