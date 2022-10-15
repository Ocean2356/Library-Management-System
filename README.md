# NF18_Projet_TD3_G5

## Membres

Abdallah Tafraoui, Haiyang Ma, Jingfang Yuan, Lilian Valin

## Sujet : Biblio

### Système de gestion d'une bibliothèque

> Vous êtes chargés de concevoir un système de gestion pour une bibliothèque municipale qui souhaite informatiser ses activités : catalogage, consultations, gestion des utilisateurs, prêts, etc.
>
> La bibliothèque offre un accès à un large choix de ressources de différents types (livres, films, et enregistrement musicaux). Une ressource, quelque soit son type, a un code unique, un titre, une liste de contributeurs, une date d'apparition, un éditeur, un genre et un code de classification qui permet de la localiser dans la bibliothèque. Un contributeur est caractérisé par son nom, son prénom, sa date de naissance et sa nationalité. Dans le cas d'un livre, les contributeurs sont les auteurs du document. Dans le cas d'une œuvre musicale, on distinguera compositeurs et interprètes. De même, on distinguera les réalisateurs et les acteurs pour les films. On souhaite également conserver des informations spécifiques suivant le type du document, par exemple : l'ISBN d'un livre et son résumé, la langue des documents écrits et des films, la longueur d'un film ou d'une œuvre musicale, le synopsis d'un film, etc. Enfin, les ressources dont dispose la bibliothèque peuvent être disponibles en plusieurs exemplaires, chacun dans un état différent : neuf, bon, abîmé ou perdu.
>
> Chaque membre du personnel de la bibliothèque dispose d'un compte utilisateur (login et mot de passe) qui lui permet d'accéder aux fonctions d'administration du système. Chaque membre est caractérisé par son nom, son prénom, son adresse et son adresse e-mail.
>
> Les adhérents de la bibliothèque disposent, eux aussi, d'un compte utilisateur (login et mot de passe) ainsi que d'une carte d'adhérent qui leur permettent d'emprunter des documents. Un adhérent est caractérisé par son nom, prénom, date de naissance, adresse, adresse e-mail et numéro de téléphone. La bibliothèque souhaite garder trace de toutes les adhésions, actuelles et passées.
>
> Pour pouvoir emprunter un document, un adhérent à besoin de s'authentifier. Chaque prêt est caractérisé par une date de prêt et une durée de prêt. Un document ne peut être emprunté que s'il est disponible et en bon état. Un adhèrent ne peut emprunter simultanément qu'un nombre limité d'œuvres, chacune pour une durée limitée. Un adhérent sera sanctionné pour les retards dans le retour d'un ouvrage, ainsi que s'il dégrade l'état de celui-ci. Tout retard dans la restitution des documents empruntés entraîne une suspension du droit de prêt d'une durée égale au nombre de jours de retard. En cas de perte ou détérioration grave d'un document, la suspension du droit de prêt est maintenue jusqu'à ce que l'adhérent rembourse le document. Enfin, la bibliothèque peut choisir de blacklister un adhérent en cas de sanctions répétées.

### Besoins

* Faciliter aux adhérents la recherche de documents et la gestion de leurs emprunts.

* Faciliter la gestion des ressources documentaires : ajouter des documents, modifier leur description, ajouter des exemplaires d'un document, etc.

* Faciliter au personnel la gestion des prêts, des retards et des réservation.

* Faciliter la gestion des utilisateurs et de leurs données.

* Établir des statistiques sur les documents empruntés par les adhérents, cela permettra par exemple d'établir la liste des documents populaires, mais aussi d'étudier le profil des adhérents pour pouvoir leur suggérer des documents.

## Cadre du projet

### Livrables

Les livrables doivent être rendus en temps et en heure. Il est préférable de rendre un travail incomplet mais de qualité et à temps qu'un travail plus fourni, mais bâclé ou en retard.

* Le code informatique doit s'exécuter correctement. Il doit être lisible, ses conditions de test et d'exécution doivent être simples et documentées. Il n'est pas acceptable qu'un code ne s'exécute pas du tout.

* La documentation doit être correctement rédigée et présentée en français (ou en anglais). Il n'est pas acceptable qu'un document réalisé à plusieurs en temps non limité ne soit pas correct.

### Contraintes

* Les bases de données relationnelles doivent être réalisées avec PostgreSQL, le code doit être compatible avec la version installée sur les serveurs de l'UTC.

* Les bases de données non-relationnelles peuvent-être réalisées avec l'une des technologies vue en cours (sauf mention contraire de votre responsable de projet).

* Les applications doivent être réalisées en Python (sauf mention contraire de votre responsable de projet).

### Git

Les projets sont gérés avec Git. Une livraison de projet se manifeste sous la forme d'une URL vers un commit Git poussé sur le serveur Gitlab de l'UTC comportant :

* un fichier README.md comportant le nom des auteurs ainsi que toutes les informations nécessaires à la compréhension de l'architecture du projet

* une NDC au format markdown

* un modèle UML au format plantuml, et une image du diagramme au format PNG

* un modèle logique au format plain text

* des fichiers de code (SQL, Python...)

On veillera à avoir rendu son dépôt public (project visibility = public) ou accessible aux autres membres de l'instance (project visibility = internal).

### Conseil

* Des canaux privés ont été créés sur Mattermost pour chaque groupe. Vous avez été inscrits dans le canal correspondant à votre groupe. Les discussions sur le projet doivent se faire par ce moyen.

* Si vous rencontrez des problèmes dans le groupe (absence d'un membre par exemple), avertissez votre responsable rapidement, ne laissez pas les situations apparaître tardivement, sinon tout le groupe partage la responsabilité du problème (de par sa non-gestion).

### Plagiat

Tout cas avéré de plagiat entraînera l'exclusion de l'UV et le signalement au conseil de discipline.

### Approche itérative

Le projet est réalisé selon le "planning prévisionnel" publié sur le moodle de NF18. La NDC doit être travaillée pendant la semaine 5 et rendu dans deux jours ouvrables, et ainsi de suite. À l'issue de chaque période, vous devez fournir un livrable opérationnel sur le Gitlab (de l'UTC) de votre projet. Le chargé de TD, qui évaluera vos rendus, doit avoir au moins le droit de lecture sur les fichiers.

### Livrables à déposer sur le Gitlab du projet

* README (avec le sujet du projet et les noms des membres du groupe) lors de la création du Gitlab du projet

* NDC + première version du MCD : date du TD de la semaine 7 + 2 jours avant 23h59

* MCD corrigé + première version du MLD : date du TD de la semaine 9 + 2 jours avant 23h59

* MLD corrigé + SQL (CREATE et INSERT) : date du TD de la semaine 10 + 2 jours avant 23h59

* SQL (SELECT, GROUP BY) +première applic. python : date du TD de la semaine 11 + 2 jours avant 23h59

* Application python finalisée : date du TD de la semaine 15 + 2 jours avant 23h59

* NoSQL R-JSON : date du TD de la semaine 17 + 2 jours avant 23h59

### Client

Votre chargé de TD est votre client, c'est à lui que vous adressez vos livrables, c'est lui qui les évalue.
