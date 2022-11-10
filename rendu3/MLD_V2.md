# MLD

### Tous les attributs sont NOT NULL par défaut.
### Tous les héritages sont exclusifs
### L'héritage de compte est exclusif (si un personnel veut emprunter un livre, il le fait en tant qu'un adhérent, et il doit utiliser un compte d'adhérent).

## Plan du document
*   Liste des relations
*   Liste des contraintes
*   Choix héritages


## Liste des relation

#### Compte_adhérents :
**Compte_adhérent**(#login : str, mot_de_passe : str, blackliste : bool, adhérent => **Adherent**) \br
**vCompte_adhérent**(#login : str, mot_de_passe : str, suspendu : bool, date_suspension_droit : date, blackliste : bool, sommeDu : int, adhérent => **Adherent**) 


#### Adhérent :
**Adhérent**(#numéro_carte : int, nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int, actuelle : booléan)

#### Compte_personnel :
**Compte_personnel**(#login : str, mot_de_passe : str, personnel => **Personnel**)

#### Personnel :
**Personnel**(#id_personnel : int, nom : str, prenom : str, adresse : str, e_mail : str) 

#### Ressource : 
**Ressource**(#code : int, titre : str, date_apparition : date, éditeur : str, genre : str, code_classification : int)

#### Exemplaire :
**Exemplaire**(#id_exemplaire : int, état : Etat, ressource => **Ressource**)

#### Réservation :
**Réservation**(#adhérent => **Compte_adhérents**, #ressource => **Ressource**, #date_reserve : date)

#### Prêt :
**Prêt**(#adhérent => **Compte_adhérents**, #exemplaire => **Exemplaire**, #date_prêt : date, durée_prêt : int, date_retour : date, etat_retour : etat)

#### Sanction :
**Sanction**(#adhérent => **Prêt**.adhérent, #exemplaire => **Prêt**.exemplaire, #date_prêt => **Prêt**.date_prêt, duree_sanction : int, remboursement : monnaie, remboursementDu : bool) \br
**vSanction**(#adhérent => **Prêt**.adhérent, #exemplaire => **Prêt**.exemplaire, #date_prêt => **Prêt**.date_prêt, date_sanction : date, remboursement : monnaie, remboursementDu : bool) 

#### Livre :
**Livre**(#ISBN : int, résumé : str, langue : str, ressource => **Ressource**)

#### Film : 
**Film**(#id_film : int, langue : str, longueur : int, synopsis : str, ressource => **Ressource**)

#### Oeuvre_musicale :
**Oeuvre_musicale**(#id_oeuvre_musicale : int, longueur : int, ressource => **Ressource**)

#### Contributeur :
**Contributeur**(#id_Contributeur : int, nom : str, prénom : str, date_de_naissance : date, nationalité : str)

#### Auteur :
**Auteur**(#livre => **Livre**, #id_Contributeur => **Contributeur**)

#### Compositeur :
**Compositeur**(#musique => **Oeuvre_musicale**, #id_Contributeur => **Contributeur**)

#### Interprètre :
**Interprete**(#musique => **Oeuvre_musicale**, #id_Contributeur => **Contributeur**)

#### Réalisateur :
**Realisateur**(#film => **Film**, #id_Contributeur => **Contributeur**)

#### Acteurs :
**Acteurs**(#film => **Film**, #id_Contributeur => **Contributeur**)


### Enumérations  
Etat : {neuf, bon, abîmé, perdu}

## Liste des contraintes 

- Pour la relation **Compte_adhérent**
    - état_compte doit être un booléen
    - black_liste doit être un booléen 
    - durée_supension_droit est optionnel 
    - suspendu = ((date_suspension_droit > today()) || blackliste || sommeDu)
    - date_suspension_droit = MAX(vSanction.date_sanction)
    - sommeDu = ADD(remboursement * remboursementDu)

- Pour la relation **Adhérent**
    - adresse doit être unique
    - e_mail doit être unique
    - tel doit être unique
    - actuelle doit être un booléen

- Pour la relation **Personnel**
    - e_mail doit être unique
    - adresse doit être unique

- Pour la relation **Prêt**
    - date_retour est optionnel
    - etat_retour est optionnel

- Pour la relation **Sanction**
    - date_sanction = duree_sanction + **Prêt**.date_retour

- Pour la relation **Exemplaire**
    - état doit être : {neuf, bon, abîmé, perdu}

## Choix héritages

On utilise un hériatge exclusif pour l'ensemble des relations.