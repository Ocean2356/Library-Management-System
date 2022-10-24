#MLD

### Tous les attributs sont NOT NULL par défaut.
### Plan du document
*   Liste des relations


### Liste des relation

##### Compte_adherents :
Compte_adhérent(#login : str, mot_de_passe : str, nombre_demprunt : int, sanction : str, durée_supension_droit : int, blackliste : bool)
\--- durée_supension_droit **optionnel** 
##### Adhérent :
Adhérent(nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int) 

##### Compte_personnel
Compte_personnel(#login : str, mot_de_passe : str)

##### Personnel :
Personnel(nom : str, prénom : str, adresse : str, e_mail : str) 


##### Ressource :
Ressource(#code : int, titre : str, liste_contributeur : str, date_apparition : date, éditeur : str, genre : str, code_classification : int) 

##### Exemplaire :
Exemplaire(nombre_d_exemplaire : int, état : {neuf, bon, abîmé, perdu})

##### Contributeur :
Contributeur(#id_Contributeur : int, nom : str, prénom : str, date_de_naissance : date, nationalité : str) 


##### Livre :
Livre( #ISBN : int, résumé : str, langue : str) 

##### Film
Film(langue : str, longueur : int, synopsis : str) 

##### Oeuvre_musicale :
Oeuvre_musicale(longueur : int) 

##### Reservation :  
Reservation(#adherent=>Compte_adherents, #exemplaire=>Exemplaire, date_reserve : date)  

##### Prêt :
Prêt(#adherent=>Compte_adherents, #exemplaire=>Exemplaire, date_prêt : date, durée_prêt : int, date_retour : date, etat_retour : etat)  
\--- date_retour, etat_retour **optionnel**  

##### Auteur :
Auteur(#livre=>Livre, #id_Contributeur=>Contributeur)

##### Compositeur :
Compositeur(#musique=>Oeuvre_musicale, #id_Contributeur=>Contributeur) 

##### Interprètre :
Interprète(#musique=>Oeuvre_musicale, #id_Contributeur=>Contributeur) 

##### Réalisateur :
Réalisateur(#film=>Film, #id_Contributeur=>Contributeur) 

##### Acteurs :
Acteurs(#film=>Film, #id_Contributeur=>Contributeur) 



### Enumérations  
Etat : {neuf, bon, abîmé, perdu}
