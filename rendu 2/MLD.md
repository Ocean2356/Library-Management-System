#MLD

### Tous les attributs sont NOT NULL par défaut.
##### L'héritage de compte est exclusif (si un personnel veut emprunter un livre, il le fait en tant qu'un adhérent, et il doit utiliser un compte d'adhérent).

### Plan du document
*   Liste des relations


### Liste des relation


##### Compte_adhérents :
Compte_adhérent(#login : str, mot_de_passe : str, nombre_demprunt : int, sanction : str, durée_supension_droit : int, blackliste : bool, adhérent => Adherent)
\--- durée_supension_droit **optionnel** 

##### Adhérent :
Adhérent(#numéro_carte : int, nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int) 

##### Compte_personnel :
Compte_personnel(#login : str, mot_de_passe : str, personnel => Personnel)

##### Personnel :
Personnel(#id_personnel : int, nom : str, prenom : str, adresse : str, e_mail : str) 

##### Ressource :
Ressource(#code : int, titre : str, liste_contributeur : str, date_apparition : date, éditeur : str, genre : str, code_classification : int) 

##### Exemplaire :
Exemplaire(#id_exemplaire : int, nombre_d_exemplaire : int, état : {neuf, bon, abîmé, perdu})

##### Contributeur :
Contributeur(#id_Contributeur : int, nom : str, prénom : str, date_de_naissance : date, nationalité : str) 

##### Livre :
Livre( #ISBN : int, résumé : str, langue : str) 

##### Film
Film(#id_film : int, langue : str, longueur : int, synopsis : str) 

##### Oeuvre_musicale :
Oeuvre_musicale(#id_oeuvre_musicale : int, longueur : int) 

##### Reservation :  
Reservation(#adhérent => Compte_adhérents, #exemplaire => Exemplaire, #date_reserve : date)  

##### Prêt :
Prêt(#adhérent => Compte_adhérents, #exemplaire => Exemplaire, #date_prêt : date, durée_prêt : int, date_retour : date, etat_retour : etat)  
\--- date_retour, etat_retour **optionnel**  

##### Sanction : 
Sanction(#pret => Prêt, suspension : int, remboursement : monnaie)

##### Auteur :
Auteur(#livre => Livre, #id_Contributeur => Contributeur)

##### Compositeur :
Compositeur(#musique => Oeuvre_musicale, #id_Contributeur => Contributeur) 

##### Interprètre :
Interprete(#musique => Oeuvre_musicale, #id_Contributeur => Contributeur) 

##### Réalisateur :
Realisateur(#film => Film, #id_Contributeur => Contributeur) 

##### Acteurs :
Acteurs(#film => Film, #id_Contributeur => Contributeur) 



### Enumérations  
Etat : {neuf, bon, abîmé, perdu}