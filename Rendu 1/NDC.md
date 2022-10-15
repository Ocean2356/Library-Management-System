# Note_de_Clarification

### Liste des objets qui devront être gérés dans la base de données
*   Compte_adhérent
*   Adhérent
*   Compte_personnel
*   Personnel
*   Prêt
*   Ressource
*   Exemplaire
*   Contributeur
*   Auteur
*   Compositeur
*   Interprète
*   Réalisateur
*   Acteurs
*   Livre
*   Film
*   Oeuvre_musicale


### Liste des propriétés associées à chaque objet
##### Compte_adhérent
- login (key)
- mot_de_passe
- nombre_d_emprunt
- sanction
- durée_suspension_droit
- black_liste
- **Contraintes**
    - **(login) doit être unique**
    - **(black_liste) doit être un booléen**

##### Adhérent
- nom
- prénom
- date_de_naissance
- adresse
- e_mail
- tel
- **Contraintes**
    - **(e_mail, tel) doit être unique**

##### Compte_personnel
- login (key)
- mot_de_passe
- **Contraintes**
    - **(login) doit être unique**

##### Personnel
- nom
- prénom
- adresse
- e_mail
- **Contraintes**
    - **(e_mail) doit être unique**

##### Prêt
- date_prêt
- durée_prêt

##### Ressource
- code (key)
- titre
- liste_contributeur
- date_apparition
- éditeur
- genre
- code_classification
- **Contraintes**
    - **(code) doit être unique**

##### Exemplaire
- nombre_d_exemplaire
- état
- **Contraintes**
    - **(état) doit être : {neuf, bon, abîmé, perdu}**

##### Contributeur
- nom
- prénom
- date_de_naissance
- nationalité

##### Auteur

##### Compositeur

##### Interprète

##### Réalisateur

##### Acteurs

##### Livre
- ISBN (key)
- résumé
- langue
- **Contraintes**
    - **(ISBN) doit être unique**

##### Film
- langue
- longueur
- synopsis

##### Oeuvre_musicale
- longueur

On suppose que tous les attributs ne peuvent pas être nuls sauf si indiqués comme tels.
