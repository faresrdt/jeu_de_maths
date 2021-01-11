import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NIVEAU = int(input("Quel niveau souhaitez vous ? Tapez 1 pour débutant, 2 pour intermédiaire, 3 pour Expert : "))
NOMBRE_QUESTION = int(input("Combien de question souhaitez vous ?"))

if NIVEAU == 1:
    NOMBRE_MIN = 1
    NOMBRE_MAX = 5
elif NIVEAU == 2:
    NOMBRE_MIN = 1
    NOMBRE_MAX = 20
elif NIVEAU == 3:
    NOMBRE_MIN = 1
    NOMBRE_MAX = 100


def poser_question():
    premier_nombre = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    deuxieme_nombre = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    # operateurs = ["+", "-", "*", "/"]
    # operateur = random.choice(operateurs)
    o = random.randint(0, 3)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    elif o == 2:
        operateur_str = "-"
    elif o == 3:
        operateur_str = "/"

    reponse_str = input(f"Calculez : {premier_nombre} {operateur_str} {deuxieme_nombre} ?")
    reponse_int = int(reponse_str)

    calcul = premier_nombre + deuxieme_nombre
    if o == 1:
        calcul = premier_nombre * deuxieme_nombre
    elif o == 2:
        calcul = premier_nombre - deuxieme_nombre
    elif o == 3:
        calcul = premier_nombre / deuxieme_nombre

    if reponse_int == calcul:
        return True

    return False


nbr_points = 0

for i in range(0, NOMBRE_QUESTION):
    i += 1
    print(f"Question n°{i} sur {NOMBRE_QUESTION} : ")
    # poser_question()
    if poser_question():
        print("Bravo, le resultat est correct.")
        nbr_points += 1
    else:
        print(f"Mauvaise réponse.")

    print(f"Vous avez {nbr_points} points.")
    print()

print(f"Votre note est {nbr_points}/{NOMBRE_QUESTION}")
MOYENNE = NOMBRE_QUESTION / 2
MOYENNE_INT = int(MOYENNE)
if nbr_points == NOMBRE_QUESTION:
    print("Excellent !")
elif nbr_points == 0:
    print("Révisez vos maths...")
elif nbr_points > MOYENNE_INT:
    print("Pas mal")
elif nbr_points < MOYENNE_INT:
    print("Peut mieux faire")
