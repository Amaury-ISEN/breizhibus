import mysql.connector as mysqlcon

#Cette classe centralise le travail sur bdd.
class Base_donnee:

    def __init__ (self):
        self.host = 'localhost'
        self.port = 8081
        self.user = 'root'
        self.mdp = 'root'
        self.nom = 'breizhibus'
        self.conn = None
        self.curseur = None

    #############
    # CONNEXION #
    #############

    #Générer la connexion:
    def gen_connexion (self, nom_bdd):

        #On teste si la connexion à la bdd n'existe pas :
        if self.conn == None:
            #Si pas de connexion, on en crée une à la bdd souhaitée en paramètre de la méthode :
            connexion = mysqlcon.connect(port = self.port,
                                        host = self.host,
                                        user = self.user,
                                        password = self.mdp,
                                        database = nom_bdd)

            setattr(self, "conn", connexion)

    def fermer_connexion (self):
        self.conn.close()


    ###########
    # CURSEUR #
    ###########

    def creer_curseur (self):
        self.curseur = self.conn.cursor(buffered=True)

    def fermer_curseur (self, curseur):
        self.curseur.close()

    ########
    # BASE #
    ########

    def ajout_colonne (self, nom_table, nom_colonne):
        query = f"ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} VARCHAR(255)"
        self.curseur.execute(query)
        del query

    #Méthode qui retourne une liste d'apprenants à partir de la bdd :
    def recup_lignes_base (self):

        resultat = []
        self.curseur.execute('SELECT * FROM lignes;')

        for x in self.curseur.fetchall():
            resultat.append(x)

        return resultat

    #Méthode qui récupère les lignes et leurs bus associés en base.
    def recup_lignes_et_bus (self):
    
        resultat = []
        self.curseur.execute('SELECT A.id_ligne, A.nom, B.numero, B.immatriculation, B.nombre_place FROM lignes A JOIN bus B ON A.id_ligne = B.id_ligne;')

        for x in self.curseur.fetchall():
            resultat.append(x)

        return resultat

    #Méthode qui récupère les lignes et leurs arrêts associés en base.
    def recup_lignes_arrets (self):
    
        resultat = []
        self.curseur.execute('SELECT A.id_ligne, A.nom, C.nom, C.adresse FROM lignes A, arrets_lignes B, arrets C WHERE A.id_ligne = B.id_ligne AND B.id_arret = C.id_arret')

        for x in self.curseur.fetchall():
            resultat.append(x)

        return resultat
    
    # #Méthode pour mettre à jour un bus
    # def modifier_bus_base (self, objets):
        
    #     sql = "UPDATE bus SET mail = %s WHERE id_apprenant = %s;"
    #     var = []
    #     for x in objets:
    #         var.append( (x.mail, x.id) )
    #     self.curseur.executemany(sql,var)
    #     self.conn.commit()
    #     del sql
    #     del var

    def ajout_bus_base (self, id_ligne, nb_places, numero_bus, immat_bus):
        """Prend toutes les infos nécessaires à la création d'un bus rentrées par l'utilisateur dans l'instance app."""
        
        sql = "INSERT INTO bus (numero, immatriculation, nombre_place, id_ligne) VALUES (%s, %s, %s, %s);"

        var = []
        var.append(numero_bus)
        var.append(immat_bus)
        var.append(nb_places)
        var.append(id_ligne)
        var = tuple(var)

        self.curseur.execute(sql,var)
        self.conn.commit()
        del sql
        del var


    #Méthode pour mettre à jour un bus
    def supprimer_bus_base (self, var):
        
        sql = "DELETE FROM bus WHERE numero = %s;"

        self.curseur.execute(sql,var)
        self.conn.commit()
        del sql

        
    #Méthode pour récupérer tous les bus
    def recuperer_bus_base (self):
        resultat = []
        sql = "SELECT * FROM bus;"

        self.curseur.execute(sql)
        self.conn.commit()
        del sql

        for x in self.curseur.fetchall():
            resultat.append(x)

        return resultat
