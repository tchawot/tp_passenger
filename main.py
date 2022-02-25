import bus
import passager

listeBus = []
listePassagerEnAttente = []

#creer un bus et l'ajoute à la flotte
def addBus():
    print("--------------------Ajout des Bus-------------------")
    nombreBus=int(input("Entrez le nombre de bus que vous souhaitez creer: "))
    for i in range(0, nombreBus):
        newBus = bus.creerBus()
        listeBus.append(newBus)

#affiche la liste des bus de la flotte
def afficheListeBus():
    print("--------------------liste des bus de ma flotte-------------------")
    for bus in listeBus:
        print("Identifiant du Bus: {} \n nombre de place max: {} \n nombre de place disponible: {} \n Poids max: {} " .format(bus["identifiant"],bus["nombrePlaceMax"],bus["nombrePlaceDisponible"],bus["poidsMax"]))

#recherche le premier bus non plein de la flotte
def firstAvalableBusIndex():
    trouve = False
    item = 0
    while trouve == False and item < len(listeBus):
        if listeBus[item]["nombrePlaceDisponible"] > 0:
            trouve = True
        else:
            item += 1
    if trouve == True:
        return item
    else:
        return -1

# creer un passager et l'ajoute dans le premier bus non plein de la flotte
def addPassage():
    nombrePassager = int(input("Entrez le nombre de Passager que vous souhaitez enregistrer: "))
    for i in range(0, nombrePassager):
        newPassager = passager.creerPassager()
        if firstAvalableBusIndex() != -1:
            bus.ajouterPassagerBus(listeBus[firstAvalableBusIndex()],newPassager)
        else:
            listePassagerEnAttente.append(newPassager)

#affiche la liste des passagers en attanente d'un bus
def afficheListePassagerEnAttente():
    print("Liste des passagers en attente")
    for i in listePassagerEnAttente:
        print("Identifiant: {} Nom: {} \n")

#recherche un passager dans la fil d'attente des passagers à partir de son identifiant saisie au clavier
def cherchePassager(str):
    trouve = False
    item = 0
    while trouve == False and item < len(listePassagerEnAttente):
        if listePassagerEnAttente[item]["identifiant"] == str:
            trouve = True
        else:
            item += 1
    if trouve == True:
        return item
    else:
        return -1

#recherche l'index d'un bus dans la liste des bus à partir de son identifiant saisi au clavier
def chercherBus(str):
    trouve = False
    item = 0
    while trouve == False and item < len(listeBus):
        if listeBus[item]["identifiant"] == str:
            trouve = True
        else:
            item += 1
    if trouve == True:
        return item
    else:
        return -1

#Ajoute un passager dans un bus. l'identifiant de bus et passager saisie au clavier
def ajouterPassagerBus():
    print("------------------ Ajoutter un passager dans un bus -------------------------")
    passager = input("Entrez l'idenfifiant du passager: ")
    bus = input("Entrez l'idenfifiant du bus: ")
    indexPassager= cherchePassager(passager)
    indexBus = chercherBus(bus)
    if indexBus != -1 and indexPassager != -1:
        bus.ajouterPassagerBus(bus,passager)
    else:
        print("Erreur!!! verifier que le bus et le passer existent bien!")


#affiche le nombre de place disponible dans un bus dont l'identifiant sera saisi au clavier
def afficherNombrePlacePisponible():
    print("------------------ Recherche du nombre de place disponible d'un bus -------------------------")
    identifiant = input("Entrez l'idenfifiant du bus: ")
    indexBus=chercherBus(identifiant)
    if indexBus != -1:
        print("Le bus d'idenfifint {} a {} places disponibles:" .format(listeBus[indexBus]["identifiant"], listeBus[indexBus]["nobrePlaceDisponible"]))
    else:
        print("Le bus d'identifiant {} ne fait pas partie de votre flotte" .format(bus[str]))


#affiche l'ensemble des kg disponibles pour un bus. identifiant du bus recupéré au clavier
def afficherNombreKgDisponbleBus():
    print("------------------ Recherche du nombre de kg disponible d'un bus -------------------------")
    identifiant = input("Entrez l'idenfifiant du bus: ")
    indexBus = chercherBus(identifiant)
    if indexBus != -1:
        print("Le bus d'idenfifint {} a {} Kg disponibles".format(listeBus[indexBus]["identifiant"],listeBus[indexBus]["poidsDisponible"]))
    else:
        print("Le bus d'identifiant {} ne fait pas partie de votre flotte".format(bus[str]))


#affiche l'esnsemble des passagers present dans un bus. identifiant du bus saisi au clavier
def afficherListePassagerBus():
    print("------------------ Liste des passagers d'un bus -------------------------")
    identifiant = input("Entrez l'idenfifiant du bus")
    indexBus = chercherBus(identifiant)
    print("Le noms des passagers  bus d'idenfifint {}".format(listeBus[indexBus]["identifiant"]))
    for item in listeBus[indexBus]["listePassager"]:
        print(item["nom"] + "\n")


#affiche l'ensemble des passagers de la flotte
def affichePassagerFlotte():
    print("------------------ Liste des passagers d'un de la flotte -------------------------")
    for item in listeBus:
        for i in item:
            print(item["nom"] + "\n")


#verifie qu'un passager donnée est dans un bus donné
def passagerEstDansBus(bus,passager):
    indexBus=chercherBus(bus)
    indexPassager=cherchePassager(passager)

    present = False
    if indexBus != -1 and indexPassager!=-1:
        for item in listeBus[indexBus]:
            if item["listePassager"] == passager["nom"]:
                present = True
        if present == True:
            print("Le passager {} est dans le bus {} " .format(passager, bus))
    else:
        print("le bus ou le passager n'est pas dans votre system")

#verifier si le transfert de passagers entre deux bus est possible
def transfertBus(busInitial, busDestination):
    indexBusInitial = chercherBus(busInitial)
    indexBusDestination = chercherBus(busDestination)

    if indexBusInitial != -1 and indexBusDestination != -1:
        if listeBus[indexBusDestination]["nombrePlaceDisponible"] >= listeBus[indexBusInitial]["nombrePlaceMax"] - listeBus[indexBusInitial]["nombrePlaceDisponible"]:
            print("Le Bus {} peut accueillir les passagers du bus {}" .format(busDestination, busInitial))
        else:
            print("Le Bus {} ne peut pas  accueillir les passagers du bus {}".format(busDestination, busInitial))
    else:
        print("l'un des bus que vous avez entré n'existe pas")


addBus()
addPassage()
afficheListeBus()
afficherListePassagerBus()






