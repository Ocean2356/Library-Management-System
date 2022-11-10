DROP TABLE IF EXISTS compte_adherent;
DROP TABLE IF EXISTS adherent;
DROP TABLE IF EXISTS personnel;
DROP TABLE IF EXISTS compte_personnel;
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS
DROP TABLE IF EXISTS



CREATE TABLE adherent(
    numero_carte INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    date_de_naissance DATE NOT NULL CHECK(date_de_naissance<current_date),
    adresse VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    tel INTEGER NOT NULL,
    actuelle BOOLEAN NOT NULL
)

CREATE TABLE personnel(
    id_personnel INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    adresse VARCHAR NOT NULL,
    email VARCHAR NOT NULL
)

CREATE TABLE compte_adherent(
    login VARCHAR PRIMARY KEY,
    mot_de_passe VARCHAR NOT NULL,
    blackliste BOOLEAN NOT NULL,
    adherant INTEGER NOT NULL REFERENCES adherant(numero_carte) --Need to check
)

CREATE TABLE compte_personnel(
    login VARCHAR PRIMARY KEY,
    mot_de_passe VARCHAR NOT NULL,
    personnel INTEGER NOT NULL REFERENCES adherant(numero_carte) --Need to check
)