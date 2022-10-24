#MLD

### Tous les attributs sont NOT NULL par défaut.
### Plan du document
*   Liste des relations


### Liste des relation

##### Compte_adherents :
Compte_adhérent : (#login : str, mot_de_passe : str, nombre_demprunt : int, sanction : str, durée_supension_droit : int, blackliste : bool)
\--- durée_supension_droit **optionnel** 
##### Adhérent :
Adhérent : (nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int) 

##### Compte_personnel
Compte_personnel : (#login : str, mot_de_passe : str)

##### Personnel :
Personnel : (nom : str, prénom : str, adresse : str, e_mail : str) 

##### Prêt :
Prêt : (date_prêt : date, durée_prêt : int, date_retour : date, etat_retour : etat)  
\--- date_retour, etat_retour **optionnel** 

##### Ressource :
Ressource : (#code : int, titre : str, liste_contributeur : str, date_apparition : date, éditeur : str, genre : str, code_classification : int) 

##### Exemplaire :
Exemplaire : (nombre_d_exemplaire : int, état : {neuf, bon, abîmé, perdu})

##### Contributeur :
Contributeur : (nom : str, prénom : str, date_de_naissance : date, nationalité : str) 

##### Auteur :
Auteur : ()

##### Compositeur :
Compositeur : () 

##### Interprètre :
Interprète : () 

##### Réalisateur :
Réalisateur : () 

##### Acteurs :
Acteurs : () 

##### Livre :
Livre : ( #ISBN : int, résumé : str, langue : str) 

##### Film
Film : (langue : str, longueur : int, synopsis : str) 

##### Oeuvre_musicale :
Oeuvre_musicale : (longueur : int) 


### Enumérations  
Etat : {neuf, bon, abîmé, perdu}
