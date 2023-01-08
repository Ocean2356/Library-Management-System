INSERT INTO adherent VALUES (10000001, 'Ma', 'Haiyang', '2000-10-04', '6 Ginza', 'haiyang.ma@etu.utc.fr', 0611223344, '1');
INSERT INTO adherent VALUES (10000012, 'Yuan', 'Jingfang', '2000-02-29', '1 Road Piccadilly', 'yjf@google.com', 0766554433, '1');
INSERT INTO adherent VALUES (10000123, 'Valin', 'Lilian', '2002-01-01', '2 Avenue des Champs-Élysées', 'vl@yahoo.com', 0122334455, '1');
INSERT INTO adherent VALUES (10001234, 'Tafraoui', 'Abdallah', '2001-12-31', '3 Road Beijing', 'TA@qq.com', 0988776655, '0'); --need check

INSERT INTO personnel VALUES (1001, 'Ma', 'Tata', '4 Broadway', 'matata@outlook.com');
INSERT INTO personnel VALUES (1002, 'Yuan', 'Tutu', '5 Fifth Avenue', 'yuantutu@163.com');
INSERT INTO personnel VALUES (1003, 'Valin', 'Tintin', '6 Lombard Street', 'valintintin@gmx.com');
INSERT INTO personnel VALUES (1004, 'Tafraoui', 'Titi', '7 Abbey Road', 'tatiti@aol.com');

INSERT INTO compte_adherent VALUES ('haiyang.ma', '123', '0',10000001, '[{"ressource":101024, "date_reserve":"2021-01-29"}]');
INSERT INTO compte_adherent VALUES ('jingfang.yuan', 'qwe', '0', 10000012, '[{"ressource":112048, "date_reserve":"2021-01-23"}, {"ressource":101024, "date_reserve":"2021-03-18"}]');
INSERT INTO compte_adherent VALUES ('lilian.valin', 'asd', '0', 10000123, '[{"ressource":124096, "date_reserve":"2021-09-23"}]');
INSERT INTO compte_adherent VALUES ('abdallah.tafraoui', 'zxc', '1', 10001234, '[{"ressource":124096, "date_reserve":"2021-01-23"}]');

INSERT INTO compte_personnel VALUES ('tata.ma', '890', 1001);
INSERT INTO compte_personnel VALUES ('tutu.yuan', 'iop', 1002);
INSERT INTO compte_personnel VALUES ('tintin.valin', 'kl;', 1003);
INSERT INTO compte_personnel VALUES ('titi.tafraoui', ',./', 1004);

INSERT INTO ressource VALUES (101024, 'a good book', '1924-10-24', 'writer', 'poetique', 1010,
'{"auteur":[{"nom":"Liu", "prenom":"Cixin", "date_de_naissance":"1963-06-23", "nationalite":"chinoise"}]}');
INSERT INTO ressource VALUES (112048, 'a good film', '2011-04-08', 'director', 'realistique', 1120,
'{"compositeur":[{"nom":"Nolan", "prenom":"Christophe", "date_de_naissance":"1970-07-30", "nationalite":"anglaise"}], 
"interprete":[{"nom":"Leonardo", "prenom":"DiCaprio", "date_de_naissance":"1974-11-11", "nationalite":"américaine"}]}');
INSERT INTO ressource VALUES (124096, 'a good music', '1996-12-04', 'composer', 'classique', 1240,
'{"compositeur":[{"nom":"Chopin", "prenom":"Frédéric", "date_de_naissance":"1810-03-01", "nationalite":"polonaise"}], 
"interprete":[{"nom":"Lang", "prenom":"Lang", "date_de_naissance":"1982-06-13", "nationalite":"chinoise"}]}');

INSERT INTO exemplaire VALUES (10102401, 'neuf', 101024);
INSERT INTO exemplaire VALUES (10102402, 'bon', 101024);
INSERT INTO exemplaire VALUES (11204801, 'abime', 112048);
INSERT INTO exemplaire VALUES (12409601, 'perdu', 124096);

--INSERT INTO reservation VALUES('haiyang.ma', 101024, '2020-01-23');

INSERT INTO pret VALUES ('jingfang.yuan', 10102402, 101024, '2020-07-31', 35, '2020-08-21', 'bon');
INSERT INTO pret VALUES ('lilian.valin', 11204801, 112048, '2020-09-01', 21, '2020-09-22', 'abime');
INSERT INTO pret VALUES ('abdallah.tafraoui', 12409601, 124096, '2021-01-21', 21, '2021-06-22', 'perdu');

INSERT INTO sanction VALUES ('lilian.valin', 11204801, 112048, '2020-09-01', 0, 10.00, 'false');
INSERT INTO sanction VALUES ('abdallah.tafraoui', 12409601, 124096, '2021-01-21', 152, 5.00, 'true');

INSERT INTO livre VALUES(9876543210123, 'This is a really good book. Really poetique.', 'en', 101024);
INSERT INTO film VALUES ('fr', '02:13:55', 'That''s a terrific movie.', 112048);
INSERT INTO oeuvre_musicale VALUES ('01:38:24', 124096);


