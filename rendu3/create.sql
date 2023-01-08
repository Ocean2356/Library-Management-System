DROP TABLE IF EXISTS acteur CASCADE;
DROP TABLE IF EXISTS realisateur CASCADE;
DROP TABLE IF EXISTS interprete CASCADE;
DROP TABLE IF EXISTS compositeur CASCADE;
DROP TABLE IF EXISTS auteur CASCADE;
DROP TABLE IF EXISTS contributeur CASCADE;
DROP TABLE IF EXISTS oeuvre_musicale CASCADE;
DROP TABLE IF EXISTS film CASCADE;
DROP TABLE IF EXISTS livre CASCADE;
DROP TABLE IF EXISTS sanction CASCADE;
DROP TABLE IF EXISTS pret CASCADE;
DROP TABLE IF EXISTS reservation CASCADE;
DROP TABLE IF EXISTS exemplaire CASCADE;
DROP TABLE IF EXISTS ressource CASCADE;
DROP TABLE IF EXISTS compte_personnel CASCADE;
DROP TABLE IF EXISTS compte_adherent CASCADE;
DROP TABLE IF EXISTS personnel CASCADE;
DROP TABLE IF EXISTS adherent CASCADE;



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
    adherent INTEGER NOT NULL REFERENCES adherent(numero_carte) --Need to check
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
    id_exemplaire INTEGER,
    etat VARCHAR NOT NULL CHECK(etat IN ('neuf', 'bon', 'abime', 'perdu')),
    ressource INTEGER REFERENCES ressource(code) ON DELETE CASCADE,
    PRIMARY KEY (id_exemplaire, ressource)
);

CREATE TABLE reservation(
    adherent VARCHAR REFERENCES compte_adherent(login),
    ressource INTEGER REFERENCES ressource(code) ON DELETE CASCADE ,
    date_reserve DATE,
    PRIMARY KEY (adherent, ressource, date_reserve)  
);

CREATE TABLE pret(
    adherent VARCHAR REFERENCES compte_adherent(login),
    exemplaire INTEGER,
    code_ressource INTEGER, 
    date_pret DATE CHECK(date_pret<=current_date),
    duree_pret INTEGER NOT NULL,
    date_retour DATE CHECK(date_retour>=date_pret),
    etat_retour VARCHAR CHECK(etat_retour IN ('neuf', 'bon', 'abime', 'perdu')),
    PRIMARY KEY (adherent, exemplaire, code_ressource, date_pret),
    FOREIGN KEY (exemplaire, code_ressource) REFERENCES exemplaire(id_exemplaire, ressource) ON DELETE CASCADE 
);

CREATE TABLE sanction(
    adherent VARCHAR,
    exemplaire INTEGER,
    code_ressource INTEGER, 
    date_pret DATE,
    duree_sanction INTEGER NOT NULL CHECK(duree_sanction >= 0),
    remboursement MONEY NOT NULL CHECK(remboursement::money::numeric::float8 >=0),
    remboursement_du BOOLEAN NOT NULL,
    PRIMARY KEY (adherent, exemplaire, code_ressource, date_pret),
    FOREIGN KEY (adherent, exemplaire, code_ressource, date_pret) REFERENCES pret(adherent, exemplaire, code_ressource, date_pret) ON DELETE CASCADE
);

/* CREATE TABLE livre(
    isbn NUMERIC(13) PRIMARY KEY,
    langue VARCHAR NOT NULL,
    resumé VARCHAR NOT NULL,
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
); */

CREATE TABLE livre(
    isbn NUMERIC(13) NOT NULL UNIQUE,
    langue VARCHAR NOT NULL,
    resumé VARCHAR NOT NULL,--Potentiellement problématique
    ressource INTEGER PRIMARY KEY REFERENCES ressource(code) ON DELETE CASCADE
);

CREATE TABLE film(
    langue VARCHAR NOT NULL,
    longeur TIME NOT NULL, --modify MLD
    synopsis VARCHAR NOT NULL,
    ressource INTEGER PRIMARY KEY REFERENCES ressource(code) ON DELETE CASCADE
);

CREATE TABLE oeuvre_musicale(
    longeur TIME NOT NULL,
    ressource INTEGER PRIMARY KEY REFERENCES ressource(code) ON DELETE CASCADE
);

CREATE TABLE contributeur(
    id_contributeur INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    date_de_naissance DATE NOT NULL CHECK(date_de_naissance < current_date),
    nationalite VARCHAR NOT NULL
);

CREATE TABLE auteur(
    livre INTEGER NOT NULL REFERENCES livre(ressource) ON DELETE CASCADE,
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur) ON DELETE CASCADE,
    PRIMARY KEY(livre, id_contributeur)
);

CREATE TABLE compositeur(
    musique INTEGER NOT NULL REFERENCES oeuvre_musicale(ressource) ON DELETE CASCADE,
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur) ON DELETE CASCADE,
    PRIMARY KEY(musique, id_contributeur)
);

CREATE TABLE interprete(
    musique INTEGER NOT NULL REFERENCES oeuvre_musicale(ressource) ON DELETE CASCADE,
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur) ON DELETE CASCADE,
    PRIMARY KEY(musique, id_contributeur)
);

CREATE TABLE realisateur(
    film INTEGER NOT NULL REFERENCES film(ressource) ON DELETE CASCADE,
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur) ON DELETE CASCADE,
    PRIMARY KEY(film,id_contributeur)
);

CREATE TABLE acteur( -- without 's'
    film INTEGER NOT NULL REFERENCES film(ressource) ON DELETE CASCADE,
    id_contributeur INTEGER NOT NULL REFERENCES contributeur(id_contributeur) ON DELETE CASCADE,
    PRIMARY KEY(film,id_contributeur)
);

CREATE VIEW film_all AS 
SELECT r.*, f.langue, f.longeur, f.synopsis FROM ressource r JOIN film f ON r.code=f.ressource; 

CREATE VIEW livre_all AS 
SELECT r.*, f.isbn, f.langue, f.resumé FROM ressource r JOIN livre f ON r.code=f.ressource; 

CREATE VIEW music_all AS 
SELECT r.*, f.longeur FROM ressource r JOIN oeuvre_musicale f ON r.code=f.ressource; 
