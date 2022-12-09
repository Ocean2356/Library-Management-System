from datetime import date

def gerer_pret(cur, login):
    user_choix = -1
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("1 Afficher les prêts en cours")
        print("2 Afficher les prêts terminé")
        print("3 Crée un nouveau prêt")
        print("4 Retourner un prêt")
        print("5 Gérer les réservations")
        print("0 Quitter")
        user_choix = input("Sélectioner un choix : ")
        if user_choix != "0":
            if user_choix == "1":
                Affichage_pret_en_cour(cur)
            elif user_choix == "2":
                Affichage_pret_fini(cur)
            elif user_choix == "3":
                Nouveau_pret(cur)
            elif user_choix == "4":
                Retour_pret(cur)
            elif user_choix == "5":
                Gerer_reservation(cur)
            else:
                print("Veuillez effectuer une saisie valide !")

def Affichage_pret_en_cour(cur):
    user_choix = -1
    i_pret = 0
    sql="select * from pret where etat_retour is null"
    cur.execute(sql)
    raw = cur.fetchall()
    #Aucun prêt en cour
    if raw == []:
        print("--------------------")
        print("Aucun prêt en cours")
        print("--------------------")
        user_choix = "0"
    #Affichage des prêts en cours
    nombre_pret = len(raw)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("Le document à était emprunté par :",raw[i_pret][0])
        print("C'est l'exemplaire numéro : ",raw[i_pret][1])
        print("Le code du document est : ", raw[i_pret][2])
        print("Le début du prêt est en date du : ",raw[i_pret][3])
        print("La durée du prêt est de ",raw[i_pret][4],"jours")
        print("--------------------------------------------------------")
        print("1 Pour passer au prêt suivant")
        print("0 Pour quitter")
        user_choix = input("Sélectionner un choix : ")
        if user_choix == "1":
            if i_pret+1 < nombre_pret:
                i_pret += 1
            elif i_pret+1 == nombre_pret:
                i_pret = 0

def Affichage_pret_fini(cur):
    user_choix =-1
    i_pret = 0
    sql="select * from pret where etat_retour is not null"
    cur.execute(sql)
    raw = cur.fetchall()
    #Aucun prêt fini
    if raw == []:
        print("--------------------")
        print("Aucun prêt en fini")
        print("--------------------")
        user_choix = "0"
    #Affichage des prêts fini
    nombre_pret = len(raw)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("Le document à était emprunté par :", raw[i_pret][0])
        print("C'est l'exemplaire numéro : ", raw[i_pret][1])
        print("Le code du document est : ", raw[i_pret][2])
        print("Le début du prêt est en date du : ", raw[i_pret][3])
        print("La durée du prêt est de ", raw[i_pret][4], "jours")
        print('La date de retour est le : ', raw[i_pret][5])
        print("l'état au retour est ", raw[i_pret][6])
        print("--------------------------------------------------------")
        print("1 Pour passer au prêt suivant")
        print("0 Pour quitter")
        user_choix = input("Sélectionner un choix : ")
        if user_choix == "1":
            if i_pret+1 < nombre_pret:
                i_pret += 1
            elif i_pret+1 == nombre_pret:
                i_pret = 0

def Nouveau_pret(cur):
    #login
    print("Entrée le login de l'adhérent")
    login_adh = input("Login : ")
    sql = "select login from compte_adherent where login='%s';" % (login_adh)
    cur.execute(sql)
    raw = cur.fetchone()
    #test login
    while not raw:
        print("login invalide, veuillez réessayer")
        login_adh = input("Login : ")
        sql = "select login from compte_adherent where login='%s';" % (login_adh)
        cur.execute(sql)
        raw = cur.fetchone()
    #date prêt
    print("Entrée la date de prêt ")
    Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
    Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        print("La date saisie est impossible! Veuillez réessayer !")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
        Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    #durée
    print(("Entrée la durée du prêt en jours"))
    nb_jours = input("Nombre de jours : ")
    #code ressource
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("Code ressource : "))
    #exemplaire
    print("Entrée le numéro de l'exemplaire prêté")
    exemplaire = int(input("Numéro : "))
    sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % (exemplaire)
    cur.execute(sql)
    raw = cur.fetchone()
    if raw:
        exemplaire_prete = 0
    while exemplaire_prete == 0:
        print("Exemplaire déjà en prêté, voulez vous le réserver ?")
        print("1 Oui")
        print("0 Non")
        user_choix = int(input("Saisir un choix : "))
        if user_choix == 1:
            Reservation(login_adh,code_ressource,cur)
            exit()
        if user_choix == 0:
            # code ressource
            print("Entrée le code la ressource prêté")
            code_ressource = int(input("Code ressource : "))
            # exemplaire
            print("Entrée le numéro de l'exemplaire prêté")
            exemplaire = int(input("Numéro : "))
            sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % (exemplaire)
            cur.execute(sql)
            raw = cur.fetchone()
            if not raw :
                exemplaire_prete = 1
    # SQL
    sql = "insert into pret(adherent,exemplaire,code_ressource,date_pret,duree_pret) values ('%s','%s','%s','%s','%s');" % (login_adh, exemplaire, code_ressource, date(Nyear_pret, Nmonth_pret, Nday_pret), nb_jours)
    cur.execute(sql)

def Retour_pret(cur):
    #login
    print("Entrée le login de l'adhérent")
    login_adh = input("Login : ")
    sql = "select adherent from pret where adherent='%s' and date_retour is null;" % (login_adh)
    cur.execute(sql)
    raw = cur.fetchone()
    #test login
    while not raw :
        print("Login invalide, veuillez réessayer !")
        login_adh = input("Login : ")
        sql = "select adherent from pret where adherent='%s'and date_retour is null;" % (login_adh)
        cur.execute(sql)
        raw = cur.fetchone()
    #Date
    print("Entrée la date de prêt ")
    Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
    Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        print("La date saisie est impossible ! Veuillez ressaisir !")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
        Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    #Durée
    print(("Entrée la durée du pret en jours"))
    nb_jours = input("Nombre de jours : ")
    #Code ressource
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("Code ressource : "))
    #Exemplaire
    print("Entrée le numéro de l'exemplaire prêté")
    exemplaire = int(input("Numéro : "))
    sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % (exemplaire)
    cur.execute(sql)
    raw = cur.fetchone()
    #test exemplaire
    while not raw:
        print("Exemplaire non prêté, veuillez réessayer")
        exemplaire = int(input("Numéro : "))
        sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % (exemplaire)
        cur.execute(sql)
        raw = cur.fetchone()
    #Date retour
    Nyear_retour = int(input("Veuillez saisir l'année du retour\n"))
    Nmonth_retour = int(input("Veuillez saisir le mois du retour\n"))
    Nday_retour = int(input("Veuillez saisir le jour du retour\n"))
    while date(Nyear_retour, Nmonth_retour, Nday_retour) > date.today():
        print("La date saisie est impossible ! Veuillez ressaisir.\n")
        Nyear_retour = int(input("Veuillez saisir l'année du retour\n"))
        Nmonth_retour = int(input("Veuillez saisir le mois du retour\n"))
        Nday_retour = int(input("Veuillez saisir le jour du retour\n"))
    #Etat
    print("Entrée l'état de la ressource (neuf,bon,abîmé,perdu)")
    etat_retour = input("Veuillez saisir l'état : ")
    while (etat_retour != 'neuf') and (etat_retour != 'bon') and (etat_retour != 'abîmé') and (etat_retour != 'perdu'):
        print("La saisie est invalide, veuillez ressayer !")
        etat_retour = input("Veuillez saisir l'état : ")
    #SQL
    sql = "delete from pret where (pret.adherent='%s' and pret.exemplaire='%s')" %(login_adh, exemplaire)
    cur.execute(sql)
    sql = "insert into pret(adherent,exemplaire,code_ressource,date_pret,duree_pret, date_retour,etat_retour) values ('%s','%s','%s','%s','%s','%s','%s');" % (login_adh, exemplaire, code_ressource, date(Nyear_pret,Nmonth_pret,Nday_pret), nb_jours,date(Nyear_retour,Nmonth_retour,Nday_retour),etat_retour)
    cur.execute(sql)

def Reservation(login_adh, code_ressource, cur):
    #date réservation
    print("Entrée la date de réservation ")
    Nyear_reservation = int(input("Veuillez saisir l'année du réservation : "))
    Nmonth_reservation = int(input("Veuillez saisir le mois du réservation : "))
    Nday_reservation = int(input("Veuillez saisir le jour du réservation : "))
    while date(Nyear_reservation, Nmonth_reservation, Nday_reservation) > date.today():
        print("La date saisie est impossible ! Veuillez ressaisir !")
        Nyear_reservation = int(input("Veuillez saisir l'année du réservation : "))
        Nmonth_reservation = int(input("Veuillez saisir le mois du réservation : "))
        Nday_reservation = int(input("Veuillez saisir le jour du réservation : "))
    sql = "insert into reservation(adherent, ressource, date_reserve) values ('%s','%s','%s');" %(login_adh, code_ressource, date(Nyear_reservation,Nmonth_reservation,Nday_reservation))
    cur.execute(sql)

def Gerer_reservation(cur):
    user_choix = -1
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("1 Afficher les réservations en cours")
        print("2 Supprimer une réservation")
        print("0 Quitter")
        user_choix = input("Sélectioner un choix : ")
        if user_choix != "0":
            if user_choix == "1":
                Affichage_reservation(cur)
            elif user_choix == "2":
                Supprimer_reservation(cur)
            else:
                print("Veuillez effectuer une saisie valide !")

def Affichage_reservation(cur):
    user_choix = -1
    i_pret = 0
    sql="select * from reservation"
    cur.execute(sql)
    raw = cur.fetchall()
    #Aucune réservation en cours
    if raw == []:
        print("--------------------")
        print("Aucune réservation en cours")
        print("--------------------")
        user_choix = "0"
    #Affichage des réservations en cours
    nombre_pret = len(raw)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("Le document à était reservé par :",raw[i_pret][0])
        print("Le code du document est : ", raw[i_pret][1])
        print("Le début de la réservation est en date du : ",raw[i_pret][2])
        print("--------------------------------------------------------")
        print("1 Pour passer à la réservation suivante")
        print("0 Pour quitter")
        user_choix = input("Sélectionner un choix : ")
        if user_choix == "1":
            if i_pret+1 < nombre_pret:
                i_pret += 1
            elif i_pret+1 == nombre_pret:
                i_pret = 0

def Supprimer_reservation(cur):
    #login
    print("Entrée le login de l'adhérent")
    login_adh = input("Login : ")
    sql = "select login from compte_adherent where login='%s';" % (login_adh)
    cur.execute(sql)
    raw = cur.fetchone()
    #test login
    while not raw:
        print("Login invalide, veuillez réessayer !")
        login_adh = input("Login : ")
        sql = "select login from compte_adherent where login='%s';" % (login_adh)
        cur.execute(sql)
        raw = cur.fetchone()
    #code ressource
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("Code ressource : "))
    sql = "delete from reservation where adherent='%s' and ressource='%s';" %(login_adh, code_ressource)
    cur.execute(sql)

def analyser (cur):
    user_choix1 = -1
    while user_choix1!="0":
        print("--------------------------------------------------------")
        print("1 Documents les plus empruntés")
        print("2 Livres les plus empruntés")
        print("3 Musiques les plus empruntés")
        print("4 Films les plus empruntés")
        print("0 Quitter")
        user_choix1 = input("Selectionner un choix : ")
        if user_choix1!="0":
            if user_choix1=="1":
                document_favori(cur)

            else :
                print("Veuillez effectuer une saisie valide !")

def document_favori(cur):
    global nb_favori
    document_favori=[]
    sql="SELECT exemplaire, COUNT(exemplaire) AS nb FROM Pret GROUP BY exemplaire ORDER BY nb DESC;"
    cur.execute(sql)
    raw = cur.fetchall()
    if len(raw)>=3:
        nb_favori = 3
    elif len(raw) == 2:
        nb_favori = 2
    elif len(raw) == 1:
        nb_favori = 1
    for i in range (nb_favori):
        code_document = raw[i]
        sql="SELECT * FROM ressource JOIN exemplaire ON ressource.code = exemplaire.ressource WHERE exemplaire.id_exemplaire = '%s';" %(code_document[0])
        cur.execute(sql)
        document = cur.fetchall()
        document_favori.append(document)
    #Aucun favori
    if document_favori == []:
        print("--------------------")
        print("Document n'est favori")
        print("--------------------")
        user_choix = "0"
    #Affichage des prêts en cours
    print("--------------------------------------------------------")
    for i in range(nb_favori):
        print("Le code du document est :",document_favori[i][0][0])
        print("Le titre du document est : ",document_favori[i][0][1])
        print("La date du document est : ", document_favori[i][0][2])
        print("Le nom de l'éditeur est : ",document_favori[i][0][3])
        print("Le genre du document est :",document_favori[i][0][4])
        print("Le code de classification du document est ", document_favori[i][0][5])
        print("--------------------------------------------------------")

