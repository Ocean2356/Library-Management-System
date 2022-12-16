def recherche(cur):
    print("Entrer les mots clés à rechercher pour chaque champ")
    titre = input("Titre : ")
    editeur = input("Éditeur : ")
    genre = input("Genre : ")
    sql = """SELECT r.* FROM ressource r WHERE r.titre LIKE '%"""+titre+"""%' AND r.editeur LIKE '%"""+editeur+"""%' AND r.genre LIKE '%"""+genre+"""%';"""
    cur.execute(sql)
    raw = cur.fetchall()
    sql = "SELECT exemplaire, COUNT(exemplaire) AS nb FROM Pret GROUP BY exemplaire;"
    cur.execute(sql)
    nb_pret = cur.fetchall()
    print(nb_pret)
    for ligne in raw:
        print("--------------------------------------------------------")
        print("Le titre du document est : ",ligne[1])
        print("Il a était publié le : ",ligne[2])
        print("Il a était publié par : ",ligne[3])
        print("Le genre du document est : ",ligne[4])
        print("Le code de classification de la ressource est : ",ligne[5])
        print("Le code de la ressource est : ",ligne[0])
        for i in nb_pret :
            if ligne[0] == i[0]//100 :
                print("Le document à été emprunté : ",i[1],"fois")
        code = ligne[0]

        # Livre
        sql = """SELECT * FROM livre l WHERE l.ressource = '%d';""" % code
        cur.execute(sql)
        spe = cur.fetchone()
        if spe is not None:
            print("L'ISBN du lives est : ",spe[0])
            print("La langue du livre est : ",spe[1])
            print("Le résumé du livre est : \"",spe[2], "\"")
            code = spe[3]
            sql = """select c.* from auteur p, contributeur c where p.livre = %d and p.id_contributeur = c.id_contributeur ;""" % code
            cur.execute(sql)
            contributeur = cur.fetchall()
            for auteur in contributeur:
                print("L'auteur(e) du livre s'appelle",auteur[2],auteur[1])
                print("Il/Elle est né le : ",auteur[3])
                print("Il/Elle est : ",auteur[4])

        # Film
        else:
            sql = """select * from film l where l.ressource = '%d';""" % code
            cur.execute(sql)
            spe = cur.fetchone()
            if spe is not None:
                print("La langue du film est : ", spe[0])
                print("Le film dure : ", spe[1])
                print("Le synopsis du film est : \"", spe[2], "\"")

            #Musique
            else:
                sql = """select * from oeuvre_musicale l where l.ressource = '%d';""" % code
                cur.execute(sql)
                spe = cur.fetchone()
                print("La durée de la musique est :",spe[0])
        
        print()

def visualiser(cur, login):
    user_choix1 = -1
    while user_choix1!="0":
        print("1 Pour visualiser les emprunts terminé")
        print("2 Pour visualiser les emprunts en cours")
        print("0 Quitter")
        user_choix1 = input("Sélectionner un choix : ")
        if user_choix1!="0":
            if user_choix1=="1":
                print("--------------------------------------------------------")
                print("                Emprunts terminé ")
                user_choix = -1
                i_emprunt = 0
                sql = "SELECT ressource.code, ressource.titre, ressource.date_apparition, ressource.editeur, ressource.genre, pret.exemplaire, pret.date_pret, pret.duree_pret, pret.etat_retour, pret.date_retour FROM ressource JOIN pret ON pret.code_ressource = ressource.code WHERE adherent='%s' and date_retour is not null;" % (login)
                cur.execute(sql)
                raw = cur.fetchall()
                # Aucun prêt en cour
                if raw == []:
                    print("--------------------")
                    print("Aucun emprunt terminé")
                    print("--------------------")
                    user_choix = "0"
                # Affichage des prêts en cours
                nombre_emprunt = len(raw)
                while user_choix != "0":
                    print("--------------------------------------------------------")
                    print("Le code du document est :", raw[i_emprunt][0])
                    print("Le titre du document est : ", raw[i_emprunt][1])
                    print("Il a été publié le : ", raw[i_emprunt][2])
                    print("Il a été publié par : ", raw[i_emprunt][3])
                    print("Le genre du document est : ", raw[i_emprunt][4])
                    print("C'est l'exemplaire numéro : ", raw[i_emprunt][5])
                    print("Il a été prété le : ", raw[i_emprunt][6])
                    print("Pour un durée de ", raw[i_emprunt][7], " jours")
                    print("Il a été rendu dans un état : ", raw[i_emprunt][8])
                    print("Il a été rendu le : ", raw[i_emprunt][9])
                    print("--------------------------------------------------------")
                    print("1 Pour passer à l'emprunt suivant")
                    print("0 Pour quitter")
                    user_choix = input("Sélectionner un choix : ")
                    if user_choix == "1":
                        if i_emprunt + 1 < nombre_emprunt:
                            i_emprunt += 1
                        elif i_emprunt + 1 == nombre_emprunt:
                            i_emprunt = 0
            elif user_choix1=="2":
                print("--------------------------------------------------------")
                print("                Emprunts en cours ")
                user_choix = -1
                i_emprunt = 0
                sql = "SELECT ressource.code, ressource.titre, ressource.date_apparition, ressource.editeur, ressource.genre, pret.exemplaire, pret.date_pret, pret.duree_pret FROM ressource JOIN pret ON pret.code_ressource = ressource.code WHERE adherent='%s' and date_retour is null;" % (login)
                cur.execute(sql)
                raw = cur.fetchall()
                # Aucun prêt en cour
                if raw == []:
                    print("--------------------")
                    print("Aucun emprunt en cours")
                    print("--------------------")
                    user_choix = "0"
                # Affichage des prêts en cours
                nombre_emprunt = len(raw)
                while user_choix != "0":
                    print("--------------------------------------------------------")
                    print("Le code du document est :", raw[i_emprunt][0])
                    print("Le titre du document est : ", raw[i_emprunt][1])
                    print("Il a été publié le : ", raw[i_emprunt][2])
                    print("Il a été publié par : ", raw[i_emprunt][3])
                    print("Le genre du document est : ", raw[i_emprunt][4])
                    print("C'est l'exemplaire numéro : ", raw[i_emprunt][5])
                    print("Il a été prété le : ", raw[i_emprunt][6])
                    print("Pour un durée de ", raw[i_emprunt][7], " jours")
                    print("--------------------------------------------------------")
                    print("1 Pour passer à l'emprunt suivant")
                    print("0 Pour quitter")
                    user_choix = input("Sélectionner un choix : ")
                    if user_choix == "1":
                        if i_emprunt + 1 < nombre_emprunt:
                            i_emprunt += 1
                        elif i_emprunt + 1 == nombre_emprunt:
                            i_emprunt = 0
            else :
                print("Veuillez effectuer une saisie valide")
