import tkinter as tk
from tkinter import messagebox
from functools import partial

class App (tk.Tk):
    """Cette classe concerne notre fenêtre racine pour notre IHM."""
    def __init__ (self):
        tk.Tk.__init__(self)
        self.wm_title("Breizhibus")
        self.geometry("1024x720")
        self.label = tk.Label()
        self.frame_principale = tk.Frame()
        self.frame_choix_lignes = tk.Frame()
        self.frame_gestion_bus = tk.Frame()
        self.frame_ajout_bus = None

        self.ligne_choisie = tk.StringVar()
        self.label_arrets = tk.Label()
        
        self.liste_bus = None
        self.liste_numeros_bus = None
        
        self.bus_a_supprimer = tk.StringVar()
        
        # Variables destinées à contenir les menus déroulants :
        self.menu_bus_supprimer = None
        self.menu_bus_ajouter = None
        self.menu_choix_lignes = None


        # Nos variables issues de l'utilisateur, pour l'ajout de bus en base :
        self.ligne_choisie2 = tk.StringVar()
        self.immat_input = tk.StringVar()
        self.numero_bus_input = tk.StringVar()
        self.nb_places_input = tk.StringVar()

    def creer_frame_principale (self):
        self.frame_principale.pack()

    def creer_frame_choix_lignes (self):
        self.frame_choix_lignes = tk.Frame(self.frame_principale, borderwidth=2, relief="groove")
        self.frame_choix_lignes.pack()

    def creer_frame_gestion_bus (self):
        self.frame_gestion_bus = tk.Frame(self.frame_principale, borderwidth=2, relief="groove")
        self.frame_gestion_bus.pack()
        self.label_frame_gestion_bus = tk.Label(self.frame_gestion_bus, text = "Gestions des bus :")
        self.label_frame_gestion_bus.pack()

         
    def creer_frame_ajout_bus (self):

        self.frame_ajout_bus = tk.Frame(self.frame_gestion_bus, borderwidth=2, relief="groove")
        self.frame_ajout_bus.pack()
        self.label_frame_ajout_bus = tk.Label(self.frame_ajout_bus, text = "Ajouter des bus :")
        self.label_frame_ajout_bus.pack()

        self.label = tk.Label(self.frame_ajout_bus, text = "Numéro du bus :")
        self.label.pack()
        self.ajout_bus_entry_numero = tk.Entry(self.frame_ajout_bus, textvariable = self.numero_bus_input)
        self.ajout_bus_entry_numero.pack()
        
        self.label = tk.Label(self.frame_ajout_bus, text = "Immatriculation :")
        self.label.pack()
        self.ajout_bus_entry_immat = tk.Entry(self.frame_ajout_bus, textvariable = self.immat_input)
        self.ajout_bus_entry_immat.pack()
        
        self.label = tk.Label(self.frame_ajout_bus, text = "Nombre de places :")
        self.label.pack()
        self.ajout_bus_entry_nbplaces= tk.Entry(self.frame_ajout_bus, textvariable = self.nb_places_input)
        self.ajout_bus_entry_nbplaces.pack()

    def creer_frame_supprimer_bus (self):

        self.frame_supprimer_bus = tk.Frame(self.frame_gestion_bus, borderwidth=2, relief="groove")
        self.frame_supprimer_bus.pack()
        self.label_frame_supprimer_bus = tk.Label(self.frame_supprimer_bus, text = "Supprimer des bus :")
        self.label_frame_supprimer_bus.pack()


    def creer_bus_entry_box (self, frame):
        self.nom_bus_entry = tk.Entry(frame)
        self.nom_bus_entry.pack()

    def creer_menu_deroulant (self, text, frame, menu, liste_du_menu, variable):
        variable.set(liste_du_menu[0])

        self.label_choix_lignes = tk.Label(frame, text = text)
        self.label_choix_lignes.pack()

        self.menu = tk.OptionMenu(frame, variable, *liste_du_menu)
        self.menu.pack()
    
    def creer_label_arrets (self, frame, texte):
        self.label_arrets.forget()
        self.label_arrets = tk.Label(frame, text = texte)
        self.label_arrets.pack()
        
    def creer_bouton_validation (self, text, frame, fonction, argument):
        self.button = tk.Button(frame, text=text, command = partial(fonction, self, self.ligne_choisie, argument))
        self.button.pack()

    def cree_bouton_ajout_bus (self, text, frame, fonction, connexion, liste_lignes):
        self.button = tk.Button(frame, text=text, command = partial(fonction, self, connexion, liste_lignes))
        self.button.pack()

    def creer_bouton_supprimer_bus (self, text, frame, fonction, connexion):
        self.button = tk.Button(frame, text=text, command = partial(fonction, self, connexion))
        self.button.pack()


    def popup (self, message):
        """Cette fonction crée et affiche un pop-up d'avertissement contenant le message qui lui est passé en paramètre."""
        messagebox.showinfo("Breizhibus", message)
    
    def confirmation (self, message):
        """Cette fonction crée et affiche un pop-up d'avertissement contenant le message qui lui est passé en paramètre."""
        return(messagebox.askyesno("Breizhibus", message))


    def suppr_frame_supprimer_bus(self):
        self.frame_supprimer_bus.destroy()