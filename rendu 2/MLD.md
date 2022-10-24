#Note_de_Clarification

### Plan du document
*   Liste des relations


### Liste des relation

##### Compte_adherents :
Compte_adhérent : (#login : str, mot_de_passe : str, nombre_demprunt : int, sanction : str, durée_supension_droit : int, blackliste : bool) [Adhérent ; Exemplaire]

##### Adhérent :
Adhérent : (nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int) [Compte_adhérent]

##### Compte_personnel
Compte_personnel : (#login : str, mot_de_passe : str) [Personnel]

##### Personnel :
Personnel : (nom : str, prénom : str, adresse : str, e_mail : str) [Compte_personnel]

##### Prêt :
Prêt : (date_prêt : date, durée_prêt : int) 

##### Ressource :
Ressource : (#code : int, titre : str, liste_contributeur : str, date_apparition : date, éditeur : str, genre : str, code_classification : int) [Film ; Livre ; Oeuvre_musicale]

##### Exemplaire :
Exemplaire : (nombre_d_exemplaire : int, état : {neuf, bon, abîmé, perdu}) [Ressource]

##### Contributeur :
Contributeur : (nom : str, prénom : str, date_de_naissance : date, nationalité : str) [Film ; Livre ; Oeuvre_musicale ; Auteur ; Compositeur ; Interprète : Réalisateur ; Acteurs]

##### Auteur :
Auteur : () [Livre]

##### Compositeur :
Compositeur : () [Oeuvre_musicale]

##### Interprètre :
Interprète : () [Oeuvre_musicale]

##### Réalisateur :
Réalisateur : () [Film]

##### Acteurs :
Acteurs : () [Film]

##### Livre :
Livre : ( #ISBN : int, résumé : str, langue : str) [Auteur]

##### Film
Film : (langue : str, longueur : int, synopsis : str) [Réalisateur ; Acteurs]

##### Oeuvre_musicale :
Oeuvre_musicale : (longueur : int) [Interprète ; Compositeur]

On suppose que tous les attributs ne peuvent pas être nuls sauf si indiqués comme tels.
