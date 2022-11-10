INSERT INTO adherent VALUES (10000001, 'Ma', 'Haiyang', '04-10-2000', '6 Ginza', 'haiyang.ma@etu.utc.fr', 0611223344, '1');
INSERT INTO adherent VALUES (10000012, 'Yuan', 'Jingfang', '29-02-2000', '1 Road Piccadilly', 'yjf@google.com', 0766554433, '1');
INSERT INTO adherent VALUES (10000123, 'Valin', 'Lilian', '01-01-2002', '2 Avenue des Champs-Élysées', 'vl@yahoo.com', 0122334455, '1');
INSERT INTO adherent VALUES (10001234, 'Tafraoui', 'Abdallah', '31-12-2001', '3 Road Beijing', 'TA@qq.com', 0988776655, '0'); --need check

INSERT INTO personnel VALUES (1001, 'Ma', 'Tata', '4 Broadway', 'matata@outlook.com');
INSERT INTO personnel VALUES (1002, 'Yuan', 'Tutu', '5 Fifth Avenue', 'yuantutu@163.com');
INSERT INTO personnel VALUES (1003, 'Valin', 'Tintin', '6 Lombard Street', 'valintintin@gmx.com');
INSERT INTO personnel VALUES (1004, 'Tafraoui', 'Titi', '7 Abbey Road', 'tatiti@aol.com');

INSERT INTO compte_adherent VALUES ('haiyang.ma', '123', '0',10000001);
INSERT INTO compte_adherent VALUES ('jingfang.yuan', 'qwe', '0', 10000012);
INSERT INTO compte_adherent VALUES ('lilian.valin', 'asd', '0', 10000123);
INSERT INTO compte_adherent VALUES ('abdallah.tafraoui', 'zxc', '1', 10001234);

INSERT INTO compte_personnel VALUES ('tata.ma', '890', 1001);
INSERT INTO compte_personnel VALUES ('tutu.yuan', 'iop', 1002);
INSERT INTO compte_personnel VALUES ('tintin.valin', 'kl;', 1003);
INSERT INTO compte_personnel VALUES ('titi.tafraoui', ',./', 1004);

INSERT INTO ressource VALUES (101024, 'a good book', '24-10-1924', 'writer', 'poetique', 1010);
INSERT INTO ressource VALUES (112048, 'a good film', '08-04-2011', 'director', 'realistique', 1120);
INSERT INTO ressource VALUES (124096, 'a good music', '04-12-1996', 'composer', 'classique', 1240);

INSERT INTO exemplaire VALUES (10102401, 'neuf', 101024);
INSERT INTO exemplaire VALUES (10102402, 'bon', 101024);
INSERT INTO exemplaire VALUES (11204801, 'abime', 112048);
INSERT INTO exemplaire VALUES (12409601, 'perdu', 124096);

INSERT INTO reservation VALUES('haiyang.ma', 101024, '23-01-2020');

INSERT INTO pret VALUES ('jingfang.yuan', 10102402, '31-07-2020', 35, '21-08-2020', 'bon');
INSERT INTO pret VALUES ('lilian.valin', 11204801, '01-09-2020', 21, '22-09-2020', 'abime');
INSERT INTO pret VALUES ('abdallah.tafraoui', 12409601, '21-01-2021', 21, '22-06-2021', 'perdu');

INSERT INTO sanction VALUES ('lilian.valin', 11204801, '01-09-2020', 0, 10.00, 'false');
INSERT INTO sanction VALUES ('abdallah.tafraoui', 12409601, '21-01-2021', 152, 5.00, 'true');

INSERT INTO livre VALUES(9876543210123, 'This is a really good book. Really poetique.', 'en', 101024);
INSERT INTO film VALUES (12345678, 'fr', '02:13:55', 'That''s a terrific movie.', 112048);
INSERT INTO oeuvre_musicale VALUES (654321, '01:38:24', 124096);

INSERT INTO contributeur VALUES (65432101, 'Liu', 'Cixin', '23-06-1963', 'chinoise');
INSERT INTO contributeur VALUES (65432102, 'Chopin', 'Frédéric', '01-03-1810', 'polonaise');
INSERT INTO contributeur VALUES (65432103, 'Lang', 'Lang', '13-06-1982', 'chinoise');
INSERT INTO contributeur VALUES (65432104, 'Nolan', 'Christophe', '30-07-1970', 'anglaise');
INSERT INTO contributeur VALUES (65432105, 'Leonardo', 'DiCaprio', '11-11-1974', 'américaine');

INSERT INTO auteur VALUES(9876543210123, 65432101);
INSERT INTO compositeur VALUES (654321, 65432102);
INSERT INTO interprete VALUES (654321, 65432103);
INSERT INTO realisateur VALUES (12345678, 65432104);
INSERT INTO acteur VALUES (12345678, 65432105);