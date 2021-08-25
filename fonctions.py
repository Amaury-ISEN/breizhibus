from _typeshed import ReadableBuffer
from interface import App
from base_donnee import *
# Nécessaire pour dé-nester la liste de noms de lignes dans la fonction creer_liste_lignes_noms : 
from itertools import chain

def creer_listes_lignes_et_arrets_separees (liste_lignes_arrets):
    """Cette fonction crée une liste de lignes [(id, nom_de_ligne)] et une liste d'arrêts."""
    liste_lignes = []
    liste_arrets = []
    
    for i in liste_lignes_arrets :

        liste_lignes.append([i[0],i[1]])

        liste_arrets.append(i[2])
    
    # Suppression des doublons dans la liste d'arrêts :
    liste_arrets = set(liste_arrets)
    liste_arrets = list(liste_arrets)
    liste_arrets.sort()

    # Suppression des doublons dans la liste de lignes :
    liste_lignes = list(set(tuple(sub) for sub in liste_lignes))

    return liste_lignes, liste_arrets

def creer_liste_numeros_bus (liste_bus):
    resultat = []

    for i in liste_bus :
        resultat.append(i[1])

    return resultat


def creer_liste_lignes_noms (liste_lignes):
    """Cette fonction crée une liste avec uniquement les noms des lignes et pas les id
    associés (pour ne pas les afficher dans les dropdown menus, par exemple.)."""
    resultat = []

    for i in liste_lignes :
        i = list(i)
        i.pop(0)
        resultat.append(i)

    resultat = list(chain(*resultat))

    return resultat

def quels_arrets_par_ligne (app, ligne, liste_lignes_arrets):
    """Cette fonction renvoie les arrêtes pour une ligne donnée."""
    resultat = []
    for i in liste_lignes_arrets:
        # On regarde dans chaque tuple de la liste de lignes et d'arrêts :
        for j in i:
            # Si il y a la ligne considérée dans le tuple, on ajoute l'arrêt à la liste résultat
            if j == ligne.get():
                liste_arret_adresse = []
                liste_arret_adresse.append(i[2])
                liste_arret_adresse.append(i[3])
                resultat.append(liste_arret_adresse)
    app.creer_label_arrets(app.frame_choix_lignes, resultat)  
    return resultat

def creer_liste_bus (liste_lignes_bus):
    """Cette fonction crée et renvoie une liste de noms de bus uniques."""
    resultat = []

    for i in liste_lignes_bus:
        resultat.append(i[2])

    resultat = set(resultat)
    resultat = list(resultat)
    resultat = resultat.sort()
    
    return resultat

def ajout_bus (app, connexion, liste_lignes):
    nb_places = app.nb_places_input.get()
    immat_bus = app.immat_input.get()
    numero_bus = app.numero_bus_input.get()
    ligne_choisie = app.ligne_choisie2.get()
    id_ligne = 0 

    # On vérifie que tous les champs nécessaires ont été remplis par l'utilisateur :
    if len(nb_places) != 0 and len(immat_bus) !=0 and len(numero_bus) != 0 :
        
        #On vérifie si le champ nombre de places est numérique :
        if nb_places.isnumeric():
            
            # On regarde à quel id correspond le nom de ligne choisi par l'utilisateur pour l'envoi du nouveau bus en base :
            for i in liste_lignes :
                
                if i[1] == ligne_choisie :
                    id_ligne = str(i[0])
                    print("l'id ligne est :", id_ligne)

            try :
                connexion.ajout_bus_base(id_ligne, nb_places, numero_bus, immat_bus)
                app.popup("Bus ajouté en base !")

                app.rafraichir_liste_bus(connexion)
                # Refresh de la frame pour supprimer les bus : 
                app.suppr_frame_supprimer_bus()
                app.creer_frame_supprimer_bus()
                app.creer_menu_deroulant('Choisir un bus :', app.frame_supprimer_bus, app.menu_bus_supprimer, app.liste_numeros_bus, app.bus_a_supprimer)
                app.creer_bouton_supprimer_bus("Supprimer le bus", app.frame_supprimer_bus, supprimer_bus, connexion)

                
            except : 
                app.popup("Le bus n'a pas pu être ajouté en base.")


    
        else :
            app.popup("Le nombre de place doit être une valeur numérique.")
    else :
        app.popup("Il faut remplir tous les champs.")


    resultat = []
    return resultat

def rafraichir_liste_bus (app, connexion):
    app.liste_bus = connexion.recuperer_bus_base()
    app.liste_numeros_bus = creer_liste_numeros_bus(app.liste_bus)


def supprimer_bus (app, connexion):
    if app.confirmation("Voulez vous vraiment supprimer ce bus ?") == 1 :
        bus_a_supprimer = []
        bus_a_supprimer.append(app.bus_a_supprimer.get())
        bus_a_supprimer = tuple(bus_a_supprimer)
        
        print("bus supprimé :", bus_a_supprimer)
        connexion.supprimer_bus_base(bus_a_supprimer)
        app.popup("Bus supprimé de la base !")

        # Refresh de la liste de bus
        app.liste_bus = connexion.recuperer_bus_base()
        app.liste_numeros_bus = creer_liste_numeros_bus(app.liste_bus)

        # Refresh de la frame pour supprimer les bus : 
        app.suppr_frame_supprimer_bus()
        app.creer_frame_supprimer_bus()
        app.creer_menu_deroulant('Choisir un bus :', app.frame_supprimer_bus, app.menu_bus_supprimer, app.liste_numeros_bus, app.bus_a_supprimer)
        app.creer_bouton_supprimer_bus("Supprimer le bus", app.frame_supprimer_bus, supprimer_bus, connexion)

    else :
        pass

