# MLD

## Contraint par défaut

* Tous les attributs sont NOT NULL
* Tous les héritages sont exclusif

## Liste des relation

* Compte_adhérent(#login : str, mot_de_passe : str, nombre_demprunt : int, date_supension_droit : date, blackliste : bool, adhérent => Adherent)  
\--- durée_supension_droit **optionnel**
* Adhérent(#numéro_carte : int, nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int)
* Compte_personnel(#login : str, mot_de_passe : str, personnel => Personnel)
* Personnel(#id_personnel : int, nom : str, prenom : str, adresse : str, e_mail : str)
* Ressource(#code : int, titre : str, liste_contributeur : str, date_apparition : date, éditeur : str, genre : str, code_classification : int)
* Exemplaire(#id_exemplaire : int, nombre_d_exemplaire : int, état : Etat, ressource => Ressource)
* Contributeur(#id_Contributeur : int, nom : str, prénom : str, date_de_naissance : date, nationalité : str)
* Livre( #ISBN : int, résumé : str, langue : str, ressource => Ressource)
* Film(#id_film : int, langue : str, longueur : int, synopsis : str, ressource => Ressource)
* Oeuvre_musicale(#id_oeuvre_musicale : int, longueur : int, ressource => Ressource)
* Reservation(#adhérent => Compte_adhérents, #ressource => Ressource, #date_reserve : date)  
* Prêt(#adhérent => Compte_adhérents, #exemplaire => Exemplaire, #date_prêt : date, durée_prêt : int, date_retour : date, etat_retour : etat)  
\--- date_retour, etat_retour **optionnel**  
* Sanction(#pret => Prêt, duree_suspension : int, remboursement : monnaie)
* Auteur(#livre => Livre, #id_Contributeur => Contributeur)
* Compositeur(#musique => Oeuvre_musicale, #id_Contributeur => Contributeur)
* Interprete(#musique => Oeuvre_musicale, #id_Contributeur => Contributeur)
* Realisateur(#film => Film, #id_Contributeur => Contributeur)
* Acteurs(#film => Film, #id_Contributeur => Contributeur)

## Enumérations  

* Etat : {neuf, bon, abîmé, perdu}
