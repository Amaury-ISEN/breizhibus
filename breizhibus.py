from base_donnee import Base_donnee
from interface import App
from fonctions import *

# On crée notre objet connexion mySQL
connexion = Base_donnee()

# Dans notre main on va lancer un "mainloop" tkinter.
def main():

    # On se connecte à la BDD
    connexion.gen_connexion('breizhibus')

    # On crée le curseur
    connexion.creer_curseur()

    # On crée notre fenêtre principale pour l'appli :
    app = App()

    # On récupère toutes les lignes de bus depuis la base et on les met dans une liste:
    liste_lignes_arrets = connexion.recup_lignes_arrets()
    
    app.liste_bus = connexion.recuperer_bus_base()
    app.liste_numeros_bus = creer_liste_numeros_bus(app.liste_bus)


    # On crée nos frames :
    app.creer_frame_principale()
    app.creer_frame_choix_lignes()

    app.creer_frame_gestion_bus()
    app.creer_frame_ajout_bus()
    app.creer_frame_supprimer_bus()

    # On crée nos listes de travail bien séparées à partir de la liste issue d'une requête en base. 
    liste_lignes, liste_arrets = creer_listes_lignes_et_arrets_separees (liste_lignes_arrets)
    print("la liste de lignes est :", liste_lignes)
    print("la liste d'arrêts est :", liste_arrets)

    liste_lignes_bus = connexion.recup_lignes_et_bus()
    print("ligne et bus :",liste_lignes_bus)

    
    # On fabrique le menu déroulant de lignes de bus :
    liste_lignes_sans_id = creer_liste_lignes_noms(liste_lignes)
    app.creer_menu_deroulant("Choisir une ligne :", app.frame_choix_lignes, app.menu_choix_lignes, liste_lignes_sans_id, app.ligne_choisie)

    # On fabrique un bouton de validation du choix de ligne pour afficher les arrêts :
    app.creer_bouton_validation('Afficher les arrêts', app.frame_choix_lignes, quels_arrets_par_ligne, liste_lignes_arrets)    

    # Création du dropdown menu pour l'ajout de bus :
    app.creer_menu_deroulant("Choisir une ligne :", app.frame_ajout_bus, app.menu_bus_ajouter, liste_lignes_sans_id, app.ligne_choisie2)
        
    # On fabrique un bouton de validation pour ajouter un nouveau bus en base :
    app.cree_bouton_ajout_bus('Ajouter le bus', app.frame_ajout_bus, ajout_bus, connexion, liste_lignes)


    app.creer_menu_deroulant('Choisir un bus :', app.frame_supprimer_bus, app.menu_bus_supprimer, app.liste_numeros_bus, app.bus_a_supprimer)
    app.creer_bouton_supprimer_bus("Supprimer le bus", app.frame_supprimer_bus, supprimer_bus, connexion)

    app.mainloop()
    
    # La boucle tkinter terminée, on peut fermer le curseur mysql.
    connexion.fermer_curseur
    
main()
