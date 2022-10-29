# MLD

## Contraint par défaut

* Tous les attributs sont NOT NULL
* Tous les héritages sont exclusif

## Liste des relation

* Compte_adhérent(#login : str, mot_de_passe : str, blackliste : bool, adhérent => Adherent)
  * vCompte_adhérent(#login : str, mot_de_passe : str, suspendu : bool, date_suspension_droit : date, blackliste : bool, sommeDu : int, adhérent => Adherent) avec suspendu = ((date_suspension_droit > today()) || blackliste || sommeDu), sommeDu = ADD(remboursement * remboursementDu), date_suspension_droit = MAX(vSanction.date_sanction), date_suspension_droit optionnel
* Adhérent(#numéro_carte : int, nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int, actuelle : booléan)
* Compte_personnel(#login : str, mot_de_passe : str, personnel => Personnel)
* Personnel(#id_personnel : int, nom : str, prenom : str, adresse : str, e_mail : str)
* Ressource(#code : int, titre : str, date_apparition : date, éditeur : str, genre : str, code_classification : int)
* Exemplaire(#id_exemplaire : int, état : Etat, ressource => Ressource)
* Reservation(#adhérent => Compte_adhérents, #ressource => Ressource, #date_reserve : date)  
* Prêt(#adhérent => Compte_adhérents, #exemplaire => Exemplaire, #date_prêt : date, durée_prêt : int, date_retour : date, etat_retour : etat) avec date_retour, etat_retour optionnel  
* Sanction(#adhérent => Prêt.adhérent, #exemplaire => Prêt.exemplaire, #date_prêt => Prêt.date_prêt, duree_sanction : int, remboursement : monnaie, remboursementDu : bool)
  * vSanction(#adhérent => Prêt.adhérent, #exemplaire => Prêt.exemplaire, #date_prêt => Prêt.date_prêt, date_sanction : date, remboursement : monnaie, remboursementDu : bool) avec date_sanction = duree_sanction + Prêt.date_retour
* Livre(#ISBN : int, résumé : str, langue : str, ressource => Ressource)
* Film(#id_film : int, langue : str, longueur : int, synopsis : str, ressource => Ressource)
* Oeuvre_musicale(#id_oeuvre_musicale : int, longueur : int, ressource => Ressource)
* Contributeur(#id_Contributeur : int, nom : str, prénom : str, date_de_naissance : date, nationalité : str)
* Auteur(#livre => Livre, #id_Contributeur => Contributeur)
* Compositeur(#musique => Oeuvre_musicale, #id_Contributeur => Contributeur)
* Interprete(#musique => Oeuvre_musicale, #id_Contributeur => Contributeur)
* Realisateur(#film => Film, #id_Contributeur => Contributeur)
* Acteurs(#film => Film, #id_Contributeur => Contributeur)

## Enumérations  

* Etat : {neuf, bon, abîmé, perdu}
