import random

class JeuDevinette:
    def __init__(jeux):
        jeux.nombre_secret = random.randint(1, 100)
        jeux.nombre_essais = 0

    def deviner(jeux, nombre):
        jeux.nombre_essais += 1

        if nombre == jeux.nombre_secret:
            print("Félicitations ! Vous avez trouvé le nombre secret en {} essais.".format(jeux.nombre_essais))
            return True
        elif nombre < jeux.nombre_secret:
            print("Le nombre secret est plus grand.")
        else:
            print("Le nombre secret est plus petit.")

        return False


jeu = JeuDevinette()

print("Bienvenue dans le jeu de devinettes !")
print("Je pense à un nombre entre 1 et 100.")


while True:
    entree = int(input("Devinez le nombre : "))

    if jeu.deviner(entree):
        break

print("Merci d'avoir joué !")
