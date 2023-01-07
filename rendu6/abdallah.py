import psycopg2
from datetime import date

def gerer_user(cur, login):
    user_choix = -1
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("1 Afficher les adhérents sanctionés")
        print("2 Sanctionner un adhérent")
        print("3 Afficher les adhérents blacklistés")
        print("4 Gestions de la blacklistes")
        print("5 Ajouter adherant / personnel")
        print("0 Quitter")
        user_choix = input("Sélectioner un choix : ")
        if user_choix != "0":
            if user_choix == "1":
                Affichage_sanction(cur)
            elif user_choix == "2":
                Ajouter_sanction(cur)
            elif user_choix == "3":
                Affichage_blackliste(cur)
            elif user_choix == "4":
                Blacklister_adherent(cur)
            elif user_choix == "5":
                user_choix = input("1 pour ajouter un adherant, 2 pour ajouter un personnel : ")
                if user_choix == "1":  
                    ajouter_adherent(cur)
                elif user_choix == "2":
                    ajouter_personnel(cur)
                else:
                    print("Veuillez effectuer une saisie valide !")
            else:
                print("Veuillez effectuer une saisie valide !")

def Affichage_sanction(cur):
    user_choix = -1
    i_sanction = 0
    sql="select * from sanction "
    cur.execute(sql)
    raw = cur.fetchall()
    #Aucune sanction
    if raw == []:
        print("--------------------")
        print("Aucun adhérent sanctioné")
        print("--------------------")
        user_choix = "0"
    #Afficheage des prêts en cour
    nombre_sanction = len(raw)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("Le login de l'adhérent sanctionné est :",raw[i_sanction][0])
        print("C'est l'exemplaire numéro : ",raw[i_sanction][1])
        print("Le code du document est : ", raw[i_sanction][2])
        print("Le début du prêt est en date du : ",raw[i_sanction][3])
        print("La durée de la sanction est de ",raw[i_sanction][4],"jours")
        print("Le montant du remboursment est de : ",raw[i_sanction][5],"€")
        print("Le remboursement à t-il était effectué : ",raw[i_sanction][6])
        print("--------------------------------------------------------")
        print("1 Pour passer à la sanction suivante")
        print("0 Pour quitter")
        user_choix = input("Sélectionner un choix : ")
        if user_choix == "1":
            if i_sanction+1 < nombre_sanction:
                i_sanction += 1
            elif i_sanction+1 == nombre_sanction:
                i_sanction = 0

def Ajouter_sanction(cur):
    # login
    print("Entrer le login de l'adherent à sanctionner")
    login_adh = input("Login : ")
    sql = "select adherent from pret where adherent='%s';" % (login_adh)
    cur.execute(sql)
    raw = cur.fetchone()
    # test login
    while not raw:
        print("Login invalide, veuillez réessayer")
        login_adh = input("Login : ")
        sql = "select adherent from pret where adherent='%s;" % (login_adh)
        cur.execute(sql)
        raw = cur.fetchone()
    # exemplaire
    print("Entrer le numéro de l'exemplaire prêté")
    exemplaire = int(input("Numéro : "))
    sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % (exemplaire)
    cur.execute(sql)
    raw = cur.fetchone()
    # test exemplaire
    while raw:
        print("Exemplaire n'a pas encore était rendu, veuillez réessayer !")
        exemplaire = int(input("Numéro : "))
        sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % (exemplaire)
        cur.execute(sql)
        raw = cur.fetchone()
    # code ressource
    print("Entrer le code de la ressource : ")
    code_ressource = int(input("Code : "))
    # date prêt
    print("Entrée la date de prêt ")
    Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
    Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        print("La date saisie est impossible! Veuillez réessayer !")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
        Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    # Durée sanction
    print("Entrer la durée de la sanction")
    dureesanction = input("Durée : ")
    # Remboursement
    print("Entrer le montant du remboursement")
    remboursement = int(input("Montant : "))
    # Remboursement du
    print("Le remboursement à t-il était fait ? (1 ou 0)")
    remboursement_du = int(input("Saisir un choix : "))
    while (remboursement_du != 0) and (remboursement_du != 1):
        print("La saisie est invalide veuillez ressayer !")
        remboursement_du = int(input("Saisir un choix : "))
    # SQL
    sql = "insert into sanction(adherent,exemplaire,code_ressource,date_pret,duree_sanction,remboursement,remboursement_du ) values ('%s','%s','%s','%s','%s','%s','%s');" % (login_adh, exemplaire, code_ressource, date(Nyear_pret, Nmonth_pret, Nday_pret), dureesanction, remboursement,remboursement_du)
    cur.execute(sql)

def Affichage_blackliste(cur):
    user_choix = -1
    i_sanction = 0
    sql="select * from compte_adherent where blackliste='1' "
    cur.execute(sql)
    raw = cur.fetchall()
    #Aucune sanction
    if raw == []:
        print("--------------------")
        print("Aucun adhérent n'a été blacklisté")
        print("--------------------")
        user_choix = "0"
    #Afficheage des prêts en cour
    nombre_sanction = len(raw)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("Le login de l'adhérent blacklisté est :",raw[i_sanction][0])
        print("Numéro de carte de l'adhérent est : ",raw[i_sanction][3])
        print("--------------------------------------------------------")
        print("1 Pour passer à la sanction suivante")
        print("0 Pour quitter")
        user_choix = input("Sélectionner un choix : ")
        if user_choix == "1":
            if i_sanction+1 < nombre_sanction:
                i_sanction += 1
            elif i_sanction+1 == nombre_sanction:
                i_sanction = 0

def Blacklister_adherent(cur):
    
    
    user_choix = -1
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("1 Pour blacklister un adhérent")
        print("2 Pour déblacklister un adhérent")
        print("0 Quitter")
        user_choix = input("Selection un choix : ")
        if user_choix != "0":
            if user_choix == "1":
                #Blacklister un adhérent
                print("Entrer le login de l'adhérent à blacklister")
                login_adh = input("Login : ")
                sql = "update compte_adherent set blackliste =True where login='%s';" %(login_adh)
                cur.execute(sql)
            elif user_choix == "2":
                # déblacklister un adhérent
                print("Entrer le login de l'adhérent à déblacklister")
                login_adh = input("Login : ")
                sql = "update compte_adherent set blackliste =False where login='%s';" %(login_adh)
                cur.execute(sql)
            else:
                print("Veuillez effectuer une saisie valide !")
def ajouter_personnel (cur) :
    # Demande de saisie des informations du personnel à ajouter
    id_personnel = input("Veuillez saisir l'id du personnel : ")
    nom = input("Veuillez saisir le nom du personnel : ")
    prenom = input("Veuillez saisir le prénom du personnel : ")
    adresse = input("Veuillez saisir l'adresse du personnel : ")
    email = input("Veuillez saisir l'email du personnel : ")
    login = input("Veuillez saisir le login du personnel : ")
    mot_de_passe = input("Veuillez saisir le mot de passe du personnel : ")
    # Vérification de la saisie
    if id_personnel != "" and nom != "" and prenom != "" and adresse != "" and email != "" and login != "" and mot_de_passe != "":
        # Vérification de l'existence du personnel
        sql = "SELECT login FROM compte_personnel WHERE login = '%s';" % (login)
        cur.execute(sql)
        raw = cur.fetchone()
        if raw:
            print("Le personnel existe déjà")
        else:
            # Ajout du personnel
            sql = "INSERT INTO personnel (id_personnel, nom, prenom, adresse, email) VALUES ('%s', '%s', '%s', '%s', '%s');" % (id_personnel, nom, prenom, adresse, email)
            cur.execute(sql)
            sql = "INSERT INTO compte_personnel (login, mot_de_passe, personnel) VALUES ('%s', '%s', '%s');" % (login, mot_de_passe, id_personnel)
            cur.execute(sql)
            print("Le personnel a bien été ajouté")
    else:
        print("Veuillez saisir toutes les informations")

def ajouter_adherent (cur) :
    # Demande de saisie des informations de l'adhérent à ajouter
    id_adherent = int(input("Veuillez saisir l'id de l'adhérent : "))
    nom = input("Veuillez saisir le nom de l'adhérent : ")
    prenom = input("Veuillez saisir le prénom de l'adhérent : ")
    adresse = input("Veuillez saisir l'adresse de l'adhérent : ")
    email = input("Veuillez saisir l'email de l'adhérent : ")
    #Datetime
    Nyear = int(input("Veuillez saisir l'année de naissance de l'adherant : "))
    Nmonth = int(input("Veuillez saisir le mois de naissance de l'adherant : : "))
    Nday = int(input("Veuillez saisir le jour de naissance de l'adherant : : "))
    # Vérifier que la date de naissance saisie est antérieure à la date actuelle
    while date(Nyear, Nmonth, Nday) > date.today():
        print("La date saisie est impossible ! Veuillez ressaisir !")
        Nyear = int(input("Veuillez saisir l'année du réservation : "))
        Nmonth = int(input("Veuillez saisir le mois du réservation : "))
        Nday = int(input("Veuillez saisir le jour du réservation : "))
    tel = int(input("Veuillez saisir le numéro de téléphone de l'adhérent : "))
    login = input("Veuillez saisir le login de l'adhérent : ")
    mot_de_passe = input("Veuillez saisir le mot de passe de l'adhérent : ")
    # Vérification de la saisie
    if id_adherent != "" and nom != "" and prenom != "" and adresse != "" and email != "" and login != "" and mot_de_passe != "" and tel != "":
        # Vérification de l'existence de l'adhérent
        sql = "SELECT login FROM compte_adherent WHERE login = '%s';" % (login)
        cur.execute(sql)
        raw = cur.fetchone()
        if raw:
            print("L'adhérent existe déjà")
        else:
            # Ajout de l'adhérent
            sql = "INSERT INTO adherent (numero_carte, nom, prenom,date_de_naissance, adresse, email, tel, actuelle) VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%d', %s);" % (id_adherent, nom, prenom, date(Nyear, Nmonth, Nday), adresse, email, tel, False)
            cur.execute(sql)
            # Creation compte Nouvel Adhérent non blacklister par défaut
            sql = "INSERT INTO compte_adherent (login, mot_de_passe, blackliste, adherent) VALUES ('%s', '%s', %s '%d');" % (login, mot_de_passe, False, id_adherent)
            cur.execute(sql)
            print("L'adhérent a bien été ajouté")
