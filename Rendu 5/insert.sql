/* ADHERENT */
INSERT INTO adherent VALUES (10000001, 'Ma', 'Haiyang', '2000-10-04', '674, impasse Charlotte Sauvage, Vasseur-sur-Perez', 'haiyang.ma@etu.utc.fr', 0611223344, '1');
INSERT INTO adherent VALUES (10000012, 'Yuan', 'Jingfang', '2000-02-29', 'boulevard François Le Roux, Dumas', 'jingfang.yuan@etu.utc.fr', 0766554433, '1');
INSERT INTO adherent VALUES (10000123, 'Valin', 'Lilian', '2001-05-16', '71, rue de Mathieu, ChevalierVille', 'lilian.valin@etu.utc.fr', 0622334455, '1');
INSERT INTO adherent VALUES (10001234, 'Tafraoui', 'Abdallah', '2001-12-31', '81, rue de Rodriguez, Moulin', 'abdallah.tafraoui@etu?utc.fr', 0688776655, '0'); --need check

INSERT INTO compte_adherent VALUES ('haiyang.ma', '123', '0',10000001);
INSERT INTO compte_adherent VALUES ('jingfang.yuan', '258', '0', 10000012);
INSERT INTO compte_adherent VALUES ('lilian.valin', '963', '0', 10000123);
INSERT INTO compte_adherent VALUES ('abdallah.tafraoui', '147', '1', 10001234);

/* PERSONELLE */
INSERT INTO personnel VALUES (1001, 'Lefreuvre', 'Eric', 'boulevard Henry, Menardboeuf', 'eric.lefreuve@outlook.fr');
INSERT INTO personnel VALUES (1002, 'Genet', 'Gaël', '63, place Hamon, Boyer-la-Foret', 'geal.genet@outlook.fr');
INSERT INTO personnel VALUES (1003, 'Sharpe', 'Brice', '15, rue Antoinette Pasquier, Fabre-sur-Julien', 'brice.sharpe@outlook.fr');
INSERT INTO personnel VALUES (1004, 'Boulle', 'Hugues', '35, avenue de Texier, Lefevre-les-Bains', 'hugues.boulle@outlook.fr');
INSERT INTO personnel VALUES (1005, 'Admin ', 'Admin', '50, avenue de Texier, Lefevre-les-Bains', 'admin.admin@outlook.fr');

INSERT INTO compte_personnel VALUES ('eric.lefreuve', '789', 1001);
INSERT INTO compte_personnel VALUES ('gael.genet', '159', 1002);
INSERT INTO compte_personnel VALUES ('brice.sharpe', '753;', 1003);
INSERT INTO compte_personnel VALUES ('hugues.boulle', '456', 1004);
INSERT INTO compte_personnel VALUES ('Admin', '123', 1004);

/* RESSOURCE */
INSERT INTO ressource VALUES (101024, 'Le Petit Prince', '1943-04-6', 'Aegitas', 'Roman', 1010);
INSERT INTO ressource VALUES (101100, 'L Etranger', '1942-06-24', 'Edition Gallimard', 'Roman', 1011);
INSERT INTO ressource VALUES (112048, 'Titanic', '1998-01-07', '20th Century Fox', 'Amour', 1120);
INSERT INTO ressource VALUES (112112, 'Avatar', '2009-12-16', '20th Century Fox', 'Science Fiction', 1121);
INSERT INTO ressource VALUES (112211, 'Speed', '1994-06-10', '20th Century Fox', 'Action', 1122);
INSERT INTO ressource VALUES (124096, 'Billie Jean', '1982-04-12', 'Epic Records', 'Pop', 1240);
INSERT INTO ressource VALUES (124163, 'De la lune', '2021-02-25', 'NBOW', 'Rap', 1241);

/* EXEMPLAIRE */
INSERT INTO exemplaire VALUES (10102401, 'neuf', 101024);
INSERT INTO exemplaire VALUES (10102402, 'bon', 101024);
INSERT INTO exemplaire VALUES (10110001, 'bon', 101100);
INSERT INTO exemplaire VALUES (11204801, 'abime', 112048);
INSERT INTO exemplaire VALUES (11211201, 'bon', 112112);
INSERT INTO exemplaire VALUES (11211202, 'neuf', 112112);
INSERT INTO exemplaire VALUES (11221101, 'neuf', 112211);
INSERT INTO exemplaire VALUES (12409601, 'perdu', 124096);
INSERT INTO exemplaire VALUES (12416301, 'perdu', 124163);

/* RESERVATION */
INSERT INTO reservation VALUES('haiyang.ma', 101024, '2020-01-23');
INSERT INTO reservation VALUES('lilian.valin', 124163, '2022-12-06');

/* PRET */
INSERT INTO pret VALUES ('jingfang.yuan', 10102402, 101024, '2020-07-31', 35, '2020-08-21', 'bon');
INSERT INTO pret VALUES ('lilian.valin', 11204801, 112048, '2020-09-01', 21, '2020-09-22', 'abime');
INSERT INTO pret VALUES ('abdallah.tafraoui', 12409601, 124096, '2021-01-21', 21, '2021-06-22', 'perdu');

/* SANCTION */
INSERT INTO sanction VALUES ('lilian.valin', 11204801, 112048, '2020-09-01', 0, 10.00, 'false');
INSERT INTO sanction VALUES ('abdallah.tafraoui', 12409601, 124096, '2021-01-21', 152, 5.00, 'true');

/* LIVRE */
INSERT INTO livre VALUES(9783140464079, 'Fr', 'Les aventures du Petit Prince commencent sur son astéroïde, nommé astéroïde B612, où un jour pousse une rose. Le Petit Prince devient l''ami de cette rose fragile et belle. Il décide ensuite de visiter d''autres mondes, car il s''ennuyait sur sa petite planète.', 101024);
INSERT INTO livre VALUES(9780203978696, 'Fr', 'Publié en 1942, l''Étranger retrace l''histoire d''un homme ordinaire soumis à l''absurdité de l''existence et de la condition. Rédigé au passé, ce récit propose de suivre le parcours de Meursault, de l''annonce du décès de sa mère jusqu''à sa condamnation pour homicide, un an plus tard.', 101100);
/* FILM */
INSERT INTO film VALUES ('En', '03:14:00', 'En 1997, l''épave du Titanic est l''objet d''une exploration fiévreuse, menée par des chercheurs de trésor en quête d''un diamant bleu qui se trouvait à bord. Frappée par un reportage télévisé, l''une des rescapées du naufrage, âgée de 102 ans, Rose DeWitt, se rend sur place et évoque ses souvenirs. 1912. Fiancée à un industriel arrogant, Rose croise sur le bateau un artiste sans le sou.', 112048);
INSERT INTO film VALUES ('En', '02:41:00', 'Sur le monde extraterrestre luxuriant de Pandora vivent les Na''vi,des êtres qui semblent primitifs, mais qui sont très évolués. Jake Sully,un ancien Marine paralysé,redevient mobile grâce à un tel Avatar et tombe amoureux d''une femme Na''vi. Alors qu''un lien avec elle grandit,il est entraîné dans une bataille pour la survie de son monde.', 112112);
INSERT INTO film VALUES ('En', '01:56:00', 'Un jeune policier est aux prises avec un maître chanteur, artificier à la retraite, qui menace de faire sauter un autobus dans lequel il a placé une bombe. Les règles sont simples : si quelqu''un descend du bus ou si la vitesse de celui-ci passe sous les 80 kilomètres à l''heure, le véhicule explosera.', 112211);
/* MUSIQUE */
INSERT INTO oeuvre_musicale VALUES ('00:06:22', 124096);
INSERT INTO oeuvre_musicale VALUES ('00:03:17', 124163);

/* CONTRIBUTEUR */
INSERT INTO contributeur VALUES (65432101, 'Liu', 'Cixin', '1963-06-23', 'Chinois');
INSERT INTO contributeur VALUES (65432102, 'Chopin', 'Frédéric', '1810-03-01', 'Polonais');
INSERT INTO contributeur VALUES (65432103, 'Lang', 'Lang', '1982-06-13', 'Chinois');
INSERT INTO contributeur VALUES (65432104, 'Nolan', 'Christophe', '1970-07-30', 'Anglais');
INSERT INTO contributeur VALUES (65432105, 'Leonardo', 'DiCaprio', '1974-11-11', 'Américain');
INSERT INTO contributeur VALUES (65432106, 'de Saint-Exupéry', 'Antoine', '1900-06-29', 'Français');
INSERT INTO contributeur VALUES (65432107, 'Camus', 'Albert', '1913-11-07', 'Français');
INSERT INTO contributeur VALUES (65432108, 'Cameron', 'James', '1954-08-16', 'Américain');
INSERT INTO contributeur VALUES (65432109, 'Jackson', 'Michael', '1958-08-29', 'Américain');
INSERT INTO contributeur VALUES (65432110, 'Jacques', 'B.B', '1999-05-10', 'Beyrouth');
INSERT INTO contributeur VALUES (65432111, 'Rodriguez', 'Michelle', '1978-07-12', 'Américaine');
INSERT INTO contributeur VALUES (65432112, 'de Bont', 'Jan', '1973-10-22', 'Néerlandais');
INSERT INTO contributeur VALUES (65432113, 'Reeves', 'Keanu', '1964-09-02', 'Beyrouth');

/*Le Petit Prince */
INSERT INTO auteur VALUES(101024, 65432106);
/*L'Etranger */
INSERT INTO auteur VALUES(101100, 65432107);
/*Billie Jean */
INSERT INTO compositeur VALUES (124096, 65432109);
INSERT INTO interprete VALUES (124096, 65432109);
/*De la lune */
INSERT INTO compositeur VALUES (124163, 65432110);
INSERT INTO interprete VALUES (124163, 65432110);
/*Titanic */
INSERT INTO realisateur VALUES (112048, 65432108);
INSERT INTO acteur VALUES (112048, 65432105);
/*Avatar */
INSERT INTO realisateur VALUES (112112, 65432108);
INSERT INTO acteur VALUES (112112, 65432111);
/* Speed */
INSERT INTO realisateur VALUES (112211, 65432112);
INSERT INTO acteur VALUES (112211, 65432113);