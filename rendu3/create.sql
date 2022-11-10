DROP TABLE IF EXISTS acteur;
DROP TABLE IF EXISTS realisateur;
DROP TABLE IF EXISTS interprete;
DROP TABLE IF EXISTS compositeur;
DROP TABLE IF EXISTS auteur;
DROP TABLE IF EXISTS contributeur;
DROP TABLE IF EXISTS oeuvre_musicale;
DROP TABLE IF EXISTS film;
DROP TABLE IF EXISTS livre;
DROP TABLE IF EXISTS sanction;
DROP TABLE IF EXISTS pret;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS exemplaire;
DROP TABLE IF EXISTS ressource;
DROP TABLE IF EXISTS compte_personnel;
DROP TABLE IF EXISTS compte_adherent;
DROP TABLE IF EXISTS personnel;
DROP TABLE IF EXISTS adherent;



CREATE TABLE adherent(
    numero_carte INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    date_de_naissance DATE NOT NULL CHECK(date_de_naissance<current_date),
    adresse VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    tel INTEGER NOT NULL,
    actuelle BOOLEAN NOT NULL
);

CREATE TABLE personnel(
    id_personnel INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    adresse VARCHAR NOT NULL,
    email VARCHAR NOT NULL
);

CREATE TABLE compte_adherent(
    login VARCHAR PRIMARY KEY,
    mot_de_passe VARCHAR NOT NULL,
    blackliste BOOLEAN NOT NULL,
    adherant INTEGER NOT NULL REFERENCES adherent(numero_carte) --Need to check
);

CREATE TABLE compte_personnel(
    login VARCHAR PRIMARY KEY,
    mot_de_passe VARCHAR NOT NULL,
    personnel INTEGER NOT NULL REFERENCES personnel(id_personnel) --Need to check
);

CREATE TABLE ressource(
    code INTEGER PRIMARY KEY,
    titre VARCHAR NOT NULL,
    date_apparition DATE NOT NULL CHECK(date_apparition<current_date),
    editeur VARCHAR NOT NULL,
    genre VARCHAR NOT NULL,
    code_classification INTEGER NOT NULL
);

CREATE TABLE exemplaire(
    id_exemplaire INTEGER PRIMARY KEY,
    etat VARCHAR NOT NULL CHECK(etat IN ('neuf', 'bon', 'abime', 'perdu')),
    ressource INTEGER NOT NULL REFERENCES ressource(code)
);

CREATE TABLE reservation(
    adherant VARCHAR REFERENCES compte_adherent(login),
    ressource INTEGER REFERENCES ressource(code),
    date_reserve DATE,
    PRIMARY KEY (adherant, ressource, date_reserve)  
);

CREATE TABLE pret(
    adherant VARCHAR REFERENCES compte_adherent(login),
    exemplaire INTEGER REFERENCES exemplaire(id_exemplaire),
    date_pret DATE CHECK(date_pret<=current_date),
    duree_pret INTEGER NOT NULL,
    date_retour DATE CHECK(date_retour>=current_date),
    etat_retour VARCHAR CHECK(etat_retour IN ('neuf', 'bon', 'abime', 'perdu')),
    PRIMARY KEY (adherant, exemplaire, date_pret)  
);

CREATE TABLE sanction(
    adherant VARCHAR,
    exemplaire INTEGER,
    date_pret DATE CHECK(date_pret<=current_date),
    duree_sanction INTEGER NOT NULL,
    remboursement MONEY NOT NULL CHECK(remboursement::money::numeric::float8 >=0),
    remboursement_du BOOLEAN NOT NULL,
    PRIMARY KEY (adherant, exemplaire, date_pret),
    FOREIGN KEY (adherant, exemplaire, date_pret) REFERENCES pret(adherant, exemplaire, date_pret)
);

CREATE TABLE livre(
    isbn INTEGER PRIMARY KEY,
    resumé VARCHAR NOT NULL,
    langue VARCHAR NOT NULL,
    ressource INTEGER NOT NULL REFERENCES ressource(code)
);

CREATE TABLE film(
    id_film INTEGER PRIMARY KEY,
    langue VARCHAR NOT NULL,
    longeur TIME NOT NULL, --modify MLD
    synopsis VARCHAR NOT NULL,
    ressource INTEGER NOT NULL REFERENCES ressource(code)
);







CREATE TABLE oeuvre_musicale(
    id_oeuvre_musicale INTEGER PRIMARY KEY,
    longeur TIME NOT NULL,
    ressource INTEGER NOT NULL REFERENCES ressource(code)
);

CREATE TABLE contributeur(
    id_contributeur INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    date_de_naissance DATE NOT NULL CHECK(date_de_naissance < current_date),
    nationalite VARCHAR NOT NULL
);

CREATE TABLE auteur(
    livre INTEGER NOT NULL REFERENCES livre(isbn),
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur),
    PRIMARY KEY(livre, id_contributeur)
);

CREATE TABLE compositeur(
    musique INTEGER NOT NULL REFERENCES oeuvre_musicale(id_oeuvre_musicale),
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur),
    PRIMARY KEY(musique, id_contributeur)
);

CREATE TABLE interprete(
    musique INTEGER NOT NULL REFERENCES oeuvre_musicale(id_oeuvre_musicale),
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur),
    PRIMARY KEY(musique, id_contributeur)
);

CREATE TABLE realisateur(
    film INTEGER NOT NULL REFERENCES film(id_film),
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur),
    PRIMARY KEY(film,id_contributeur)
);

CREATE TABLE acteur( -- without 's'
    film INTEGER NOT NULL REFERENCES film(id_film),
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur),
    PRIMARY KEY(film,id_contributeur)
)