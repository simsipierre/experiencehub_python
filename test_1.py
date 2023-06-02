class joueur:
    pv = float(100)
    shild = float(50)
    vitesse = float(300)
    force = float(250)

enemi = joueur()

def game():
    stat = input("choisir le montant de dégat: ")
    if float(stat) > 10.0 or float(stat) < 0.0:
        print("trop grande/petite valeur\n\n\n")
        return
    print("Liste des caractéristique: pv, shild, vitesse, force")
    caractérisitique = input("choisir une de ces caractéristique: ")

    if caractérisitique == "pv" or caractérisitique == "Pv":
        enemi.pv = enemi.pv - float(stat)
    if caractérisitique == "shild" or caractérisitique == "Shild":
        enemi.shild = enemi.shild - float(stat)
    if caractérisitique == "vitesse" or caractérisitique == "Vitesse":
        enemi.vitesse = enemi.vitesse - float(stat)
    if caractérisitique == "force" or caractérisitique == "Force":
        enemi.force = enemi.force + float(stat)

    print("\n\n")
    print("pv du joueur:", enemi.pv)
    print("bouclier du joueur:", enemi.shild)
    print("vitesse du joueur:", enemi.vitesse)
    print("force du joueur:", enemi.force)
    print("\n\n\n\n\n")

    if enemi.force <= 0 or enemi.vitesse <= 0 or enemi.shild <= 0 or enemi.pv <= 0:
        return False

while True:
    game()