def recherche(cur):
    print("Entrer les mots clés à rechercher pour chaque champ")
    t = input("Titre : ")
    # d = input("Date d'apparition : ")
    e = input("Éditeur : ")
    g = input("Genre : ")
    # c = input("Contributeur : ")
    sql = """SELECT r.*
            FROM ressource r
            WHERE r.titre LIKE '%"""+t+"""%'
                AND r.editeur LIKE '%"""+e+"""%'
                AND r.genre LIKE '%"""+g+"""%'
                ;"""
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)
        code = ligne[0]
        
        sql = """select * 
                from livre l 
                where l.ressource = '%d'
                ;""" % code
        cur.execute(sql)
        spe = cur.fetchone()
        if spe is not None:
            print(spe)
            code = spe[3]
            sql = """select c.*
                    from auteur p, contributeur c
                    where p.livre = %d
                        and p.id_contributeur = c.id_contributeur
                    ;""" % code
            cur.execute(sql)
            contributeur = cur.fetchall()
            for auteur in contributeur:
                print(auteur)
            
        else:
            sql = """select * 
                    from film l 
                    where l.ressource = '%d'
                    ;""" % code
            cur.execute(sql)
            spe = cur.fetchone()
            if spe is not None:
                print(spe)
                
            else:
                sql = """select * 
                        from oeuvre_musicale l 
                        where l.ressource = '%d'
                        ;""" % code
                cur.execute(sql)
                spe = cur.fetchone()
        
                print(spe)
        
        print()
        
"""def visualiser(cur, login):
    sql = """SELECT *
            FROM pret
            WHERE adherent = '%s'
            ;""" % (login)
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)
"""

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
                sql = "select * from pret where adherent='%s' and date_retour is not null;" % (login)
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
                    print("Le document à était emprunté par :", raw[i_emprunt][0])
                    print("C'est l'exemplaire numéro : ", raw[i_emprunt][1])
                    print("Le code du document est : ", raw[i_emprunt][2])
                    print("Le début du prêt est en date du : ", raw[i_emprunt][3])
                    print("La durée du prêt est de ", raw[i_emprunt][4], "jours")
                    print("La fin du prêt est en date du : ", raw[i_emprunt][5])
                    print("L'état au retour est", raw[i_emprunt][6])
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
                sql = "select * from pret where adherent='%s' and date_retour is null;" % (login)
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
                    print("Le document à était emprunté par :", raw[i_emprunt][0])
                    print("C'est l'exemplaire numéro : ", raw[i_emprunt][1])
                    print("Le code du document est : ", raw[i_emprunt][2])
                    print("Le début du prêt est en date du : ", raw[i_emprunt][3])
                    print("La durée du prêt est de ", raw[i_emprunt][4], "jours")
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