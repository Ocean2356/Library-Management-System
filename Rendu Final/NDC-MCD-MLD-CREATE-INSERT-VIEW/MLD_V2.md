# MLD

* Tous les attributs sont NOT NULL par défaut.
* Tous les héritages sont exclusifs.

## Plan du document

* Liste des relations
* Liste des contraintes
* Choix héritages

## Liste des relation

### Compte_adhérents

**Compte_adhérent**(#login : str, mot_de_passe : str, blackliste : bool, adhérent => **Adherent**)  
**vCompte_adhérent**(#login : str, mot_de_passe : str, suspendu : bool, date_suspension_droit : date, blackliste : bool, sommeDu : int, adhérent => **Adherent**)

### Adhérent

**Adhérent**(#numéro_carte : int, nom : str, prénom : str, date_de_naissance : date, adresse : str, e_mail : str, tel : int, actuelle : booléan)

### Compte_personnel

**Compte_personnel**(#login : str, mot_de_passe : str, personnel => **Personnel**)

### Personnel

**Personnel**(#id_personnel : int, nom : str, prenom : str, adresse : str, e_mail : str)

### Ressource

**Ressource**(#code : int, titre : str, date_apparition : date, éditeur : str, genre : str, code_classification : int)

### Exemplaire

**Exemplaire**(#id_exemplaire : int, état : Etat, ressource => **Ressource**)

### Réservation

**Réservation**(#adhérent => **Compte_adhérents**, #ressource => **Ressource**, #date_reserve : date)

### Prêt

**Prêt**(#adhérent => **Compte_adhérents**, #exemplaire => **Exemplaire**, #date_prêt : date, durée_prêt : int, date_retour : date, etat_retour : etat)

### Sanction

**Sanction**(#adhérent => **Prêt**.adhérent, #exemplaire => **Prêt**.exemplaire, #date_prêt => **Prêt**.date_prêt, duree_sanction : int, remboursement : monnaie, remboursementDu : bool)  
**vSanction**(#adhérent => **Prêt**.adhérent, #exemplaire => **Prêt**.exemplaire, #date_prêt => **Prêt**.date_prêt, date_sanction : date, remboursement : monnaie, remboursementDu : bool)

### Livre

**Livre**(#ISBN : int, résumé : str, langue : str, ressource => **Ressource**)

### Film

**Film**(#id_film : int, langue : str, longueur : int, synopsis : str, ressource => **Ressource**)

### Oeuvre_musicale

**Oeuvre_musicale**(#id_oeuvre_musicale : int, longueur : int, ressource => **Ressource**)

### Contributeur

**Contributeur**(#id_Contributeur : int, nom : str, prénom : str, date_de_naissance : date, nationalité : str)

### Auteur

**Auteur**(#livre => **Livre**, #id_Contributeur => **Contributeur**)

### Compositeur

**Compositeur**(#musique => **Oeuvre_musicale**, #id_Contributeur => **Contributeur**)

### Interprètre

**Interprete**(#musique => **Oeuvre_musicale**, #id_Contributeur => **Contributeur**)

### Réalisateur

**Realisateur**(#film => **Film**, #id_Contributeur => **Contributeur**)

### Acteurs

**Acteurs**(#film => **Film**, #id_Contributeur => **Contributeur**)

### Enumérations  

Etat : {neuf, bon, abîmé, perdu}

## Liste des contraintes

* Contraintes entre relation
  * intersection(projection(Compte_personnel, login), projection(Compte_adherant, login)) = 0
  * projection(Personnel, id_personnel) - projection(Compte_personnel, personnel) = 0
  * projection(Restriction(Adhérant, actuelle = 1), numéro_carte) - projection(Compte_adhérant, adhérant) = 0
  * intersection(projection(Restriction(Adhérant, actuelle = 0), numéro_carte), projection(Compte_adhérant, adhérant)) = 0
  * intersection(projection(Film, ressource), projection(Livre, ressource)) = 0
  * intersection(projection(Film, ressource), projection(Oeuvre_musicale, ressource)) = 0
  * intersection(projection(Livre, ressource), projection(Oeuvre_musicale, ressource)) = 0
  * projection(Film, id_film) - projection(Réalisateur, film) = 0
  * projection(Film, id_film) - projection(Acteur, film) = 0
  * projection(Livre, ISBN) - projection(Auteur, livre) = 0
  * projection(Oeuvre_musicale, id_oeuvre) - projection(Compositeur, musique) = 0
  * projection(Oeuvre_musicale, id_oeuvre) - projection(Interprete, musique) = 0
  * projection(Contributeur, id_contributeur) - projection(Réalisateur, id_contributeur) - projection(Acteur, id_contributeur) - projection(Compositeur, id_contributeur) - projection(interprete, id_contributeur) - projection(Auteur, id_contributeur) = 0
* Pour tous attributs de type date
  * date <= today()
* Pour la relation **Compte_adhérant**
  * durée_supension_droit est optionnel
  * suspendu = ((date_suspension_droit > today()) || blackliste || sommeDu)
  * date_suspension_droit = MAX(vSanction.date_sanction)
  * sommeDu = ADD(remboursement * remboursementDu)
* Pour la relation **Adhérent**
  * adresse doit être unique
  * e_mail doit être unique
  * tel doit être unique
* Pour la relation **Personnel**
  * e_mail doit être unique
  * adresse doit être unique
* Pour la relation **Prêt**
  * date_retour est optionnel
  * etat_retour est optionnel
* Pour la relation **Sanction**
  * date_sanction = duree_sanction + **Prêt**.date_retour

## Choix héritages

On utilise l'héritage par les classes filles pour les comptes, parce que cela permet plus d'isolement entre les deux types du compte comme ils ont des fonctions et droits différents.

On utilise l'héritage par référence pour les ressources, parce que cela permet d'avoir une liste de tous types des ressources, qui facilite la recherche et la recommendation qui ne limite pas le type de ressource.
