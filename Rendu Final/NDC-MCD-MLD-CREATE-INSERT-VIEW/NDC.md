# Note de clarification

> On suppose que tous les attributs ne peuvent pas être nuls sauf si indiqués comme tels.

## Liste des objets qui devront être gérés dans la base de données

* Compte_adhérent
* Adhérent
* Compte_personnel
* Personnel
* Prêt
* reservation
* Ressource
* Exemplaire
* Contributeur
* Auteur
* Compositeur
* Interprète
* Réalisateur
* Acteurs
* Livre
* Film
* Oeuvre_musicale

## Liste des propriétés associées à chaque objet

### Compte_adhérent

* login (key)
* mot_de_passe
* nombre_d_emprunt
* état_compte
* durée_suspension_droit
* black_liste
* **Contraintes**
  * **état_compte doit être un booléen**, il indique si l'adhésion est actuelle ou passée
  * **(black_liste) doit être un booléen**

### Adhérent

* nom
* prénom
* date_de_naissance
* adresse
* e_mail
* tel
* **Contraintes**
  * **(e_mail, tel) doit être unique**
* **Association**
  * possède Compte_adhérent (1..1)

### Compte_personnel

* login (key)
* mot_de_passe

### Personnel

* nom
* prénom
* adresse
* e_mail
* **Contraintes**
  * **(e_mail) doit être unique**
* **Association**
  * possède Compte_personnel (1..1)

### Prêt

* date_prêt
* durée_prêt
* **Association**
  * classe d'association entre Exemplaire et Compte_adherant

### Reservation

* date_reservation
* **Association**
  * classe d'association entre Exemplaire et Compte_adherant
  
### Ressource

* code (key)
* titre
* liste_contributeur
* date_apparition
* éditeur
* genre
* code_classification
* **Héritage**
  * classe mère abstraite de Livre, Enregistrement_musical et Film
* **Association**
  * a plusieurs Exemplaires (Compositon 1--N)

### Exemplaire

* nombre_d_exemplaire
* état
* **Contraintes**
  * **(état) doit être : {neuf, bon, abîmé, perdu}**

### Contributeur

* nom
* prénom
* date_de_naissance
* nationalité

### Auteur

* **Association**
  * classe d'association entre Livre et Contributeur (N--1..N)

### Compositeur

* **Association**
  * classe d'association entre Enregistrement_musical et Contributeur (N--1..N)

### Interprète

* **Association**
  * classe d'association entre Enregistrement_musical et Contributeur (N--1..N)

### Réalisateur

* **Association**
  * classe d'association entre Film et Contributeur (N--1..N)

### Acteurs

* **Association**
  * classe d'association entre Film et Contributeur (N--1..N)

### Livre

* ISBN (key)
* résumé
* langue

### Film

* langue
* longueur
* synopsis

### Oeuvre_musicale

* longueur
