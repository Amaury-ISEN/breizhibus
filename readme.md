# Readme Breizhibus

## 1) Fonctionnement de l'application  

L'application fonctionne avec 4 fichiers pythons .py qui contiennent les scripts :

1) **breizhibus** : l'application principale qui contient la fonction main (incluant le mainloop() tkinter), le programme se lance via ce script.

2) **fonctions** : script de fonctions généralistes pour le fonctionnement de l'appli notamment la création de listes python à partir des résultats de requêtes de base_donnee.py.

3) **interface** : script qui contient des fonctions liées à l'interface graphique tkinter.

4) **base_donnee** : script qui isole et contient la partie BDD avec connexion et méthodes de requêtes de récupération et d'envoi de données en base.

## 2) Choix techniques

### 2.1) Choix de mySQL :
Il y a eu utilisation de mySQL car la BDD est de petite taille donc cela suffit (c'est de toute façon exigé par le client). Emploi de phpmyadmin en mode IHM pour structurer et peupler rapidement la BDD.

### 2.2) Choix du connecteur python :

J'ai utilisé le connecteur python mysql pour coordonner les algorithmes python et la BDD locale mysql.

### 2.3) Utilisation d'objets :

Utilisation d'objets pour l'interface graphique ainsi que pour la connexion mysql via python.

**Pour interface.py :** objet "app", c'est la fenêtre racine réalisée avec l'objet de top-niveau tkinter tk.Tk() (souvent appelée root ou master par d'autres développeurs.). 

**Pour base_donnee.py :** objet généraliste que j'appelle "connexion" mais qui a en attribut les *credentials* pour la connexion à la BDD, la connexion elle-même ainsi que le curseur.

Utiliser des objets rend le code plus facile à manier, on peut stocker des variables dans des attributs notamment les stringvar tkinter et les retrouver plus facilement, par exemple.

### 2.4) Economie de requêtes :

J'aime limiter mes requêtes SQL dans une perspective d'économie de requêtes sur serveur en entreprise. Cela entraîne des difficultés en terme d'algorithmes python car il faut bien découper le peu de listes crées via les requêtes afin d'avoir des listes plus adaptées au besoins des scripts mais cela évite de requêter la base trop souvent sans réelle raison.
 
## 3) Difficultés rencontrées

### 3.1) tkinter...
Difficulté à comprendre et prendre en main la logique tkinter. Je n'ai pas particulièrement été aidé par un tutoriel donné, je me suis inspiré de la logique que nous avions employée pour le travail de groupe Data Pursuit.

### 3.2) Gestion du temps

Autre difficulté non surmontée : arriver à finir dans les temps. J'ai eu du mal à gérer mon temps et jongler entre tous les projets. Au début de l'année, j'étais très lent, tout s'accumulait et le travail en soirée ne suffisait pas.

Sur Breizhibus, je manquais beaucoup de pratique et d'expérience et je n'arrivais pas à estimer les tâches qui allaient me prendre beaucoup de temps ni estimer celles qui seraient rapides à effectuer.

### 3.3) Garder le code propre et générique
J'ai eu de grosses difficultés à maintenir mon code propre, générique et bien factorisé. Très souvent, une petite nouveauté en terme de besoin me fait me rendre compte qu'une fonction nécessite un ajustement (par exemple l'ajout d'un nouvel argument en entrée).

C'est dû au manque d'expérience et peut-être aussi que je n'ai pas assez posé les choses en brouillon au début (en termes de quoi récupérer en base pour couvrir les besoins de l'ensemble du projet, comment structurer la partie tkinter, etc.). 

J'ai été tiraillé entre mon envie de faire un code propre et générique et la tentation de basculer dans une multitude de solutions ad hoc moins propres mais plus faciles à mettre en place. Au final, le résultat est un peu un mélange des deux assez suboptimal.


### 3.4) Ressources utilisées :
Pour m'aider dans les requêtes et fonctions j'ai utilisé les documentations officielles mysql et celle pour le connecteur. J'ai utilisé W3school pour m'aider sur quelques méthodes python et stackoverflow pour débugguer quelques messages d'erreurs particuliers.

## 4) Idées pour les requêtes non traitées :
### 4.1) Modification de bus : 
Pour ne pas s'embêter avec des conditions trop compliquées pour gérer les cas où l'utilisateur souhaiterait ne modifier que telle ou telle valeur pour un bus, le plus simple serait de récupérer toutes les infos pour un bus choisi par l'utilisateur via un dropdown menu.

Concrètement, la modification d'un bus en base serait en fait un ajout-écrasement de bus en base.

Ensuite, pré-remplir des champs de saisie entrybox avec les valeurs du bus choisi. Libre à l'utilisateur de les modifier ensuite et de cliquer sur un bouton modifier qui enverrait la requête suivante en base :

```
UPDATE bus
SET numero = numero_input,
    immatriculation = immatriculation_input,
    nombre_place = nombre_place_input,
    id_ligne = id_ligne_input
WHERE id = id_bus_input
```

Les _input correspondraient à des variables tkinter issues de l'écoute des entryboxes mentionnées plus haut.

Elles seraient intégrées aux requêtes passées au curseur avec des wildcards %s.