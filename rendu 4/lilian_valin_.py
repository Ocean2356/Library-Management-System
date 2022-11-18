def gerer_pret(cur, login):
    user_choix = -1
    while user_choix != "0":
        print("1 Afficher les prêt en cours")
        print("2 Afficher les prêt terminé")
        print("3 Crée un nouveau prêt")
        print("4 Retourner un prêt")
        print("0 Quitter")
        user_choix = input("Selection un choix : ")
        if user_choix != "0":
            if user_choix == "1":
                Affichage_pret_en_cour(cur)
            elif user_choix == "2":
                Affichage_pret_fini(cur)
            elif user_choix == "3":
                Nouveau_pret(cur)
            elif user_choix == "4":
                Retour_pret(cur)
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
    #Afficheage des prêts en cour
    nombre_pret = len(raw)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("Le document à était emprunter par :",raw[i_pret][0])
        print("C'est l'exemplaire numéro : ",raw[i_pret][1])
        print("Le code du document est : ", raw[i_pret][2])
        print("Le début du prêt est en date du : ",raw[i_pret][3])
        print("La durée du pret est de ",raw[i_pret][4],"jours")
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
        print("Le document à était emprunter par :", raw[i_pret][0])
        print("C'est l'exemplaire numéro : ", raw[i_pret][1])
        print("Le code du document est : ", raw[i_pret][2])
        print("Le début du prêt est en date du : ", raw[i_pret][3])
        print("La durée du pret est de ", raw[i_pret][4], "jours")
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
    print("Entrée le login de l'adherent")
    login_adh = input("login : ")
    #date prêt
    print("Entrée la date de prêt ")
    Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
    Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        print("La date saisie impossible! Veuillez ressaisir !")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
        Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    #durée
    print(("Entrée la durée du pret en jours"))
    nb_jours = input("nombre de jours : ")
    #exemplaire
    print("Entrée le numéro de l'exemplaire prêté")
    exemplaire = int(input("numéro : "))
    #code ressource
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("code ressource : "))
    #SQL
    sql = "insert into pret(adherent,exemplaire,code_ressource,date_pret,duree_pret) values ('%s','%s','%s','%s','%s');"%(login_adh, exemplaire, code_ressource, date(Nyear_pret,Nmonth_pret,Nday_pret), nb_jours)
    cur.execute(sql)

def Retour_pret(cur)
    #login
    print("Entrée le login de l'adherent")
    login_adh = input("login : ")
    #Date
    print("Entrée la date de prêt ")
    Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
    Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        print("La date saisie impossible! Veuillez ressaisir !")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
        Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    #Durée
    print(("Entrée la durée du pret en jours"))
    nb_jours = input("nombre de jours : ")
    #Exemplaire
    print("Entrée le numéro de l'exemplaire prêté")
    exemplaire = int(input("numéro : "))
    #Code ressource
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("code ressource : "))
    #Date retour
    Nyear_retour = int(input("Veuillez saisir l'année du retour\n"))
    Nmonth_retour = int(input("Veuillez saisir le mois du retour\n"))
    Nday_retour = int(input("Veuillez saisir le jour du retour\n"))
    while date(Nyear_retour, Nmonth_retour, Nday_retour) > date.today():
        print("La date saisie impossible! Veuillez ressaisir.\n")
        Nyear_retour = int(input("Veuillez saisir l'année du retour\n"))
        Nmonth_retour = int(input("Veuillez saisir le mois du retour\n"))
        Nday_retour = int(input("Veuillez saisir le jour du retour\n"))
    #Etat
    print("Entrée l'état de la ressource (neuf,bon,abîmé,perdu)")
    etat_retour = input("Veuillez saisir l'état : ")
    while etat_retour != 'neuf' and 'bon' and 'abîmé' and 'perdu':
        print("La saisie est invalide veuillez ressayer !")
        etat_retour = input("Veuillez saisir l'état : ")
    #SQL
    sql = "delete from pret where (pret.adherent='%s' and pret.exemplaire='%s')" %(login_adh, exemplaire)
    cur.execute(sql)
    sql = "insert into pret(adherent,exemplaire,code_ressource,date_pret,duree_pret, date_retour,etat_retour) values ('%s','%s','%s','%s','%s','%s','%s');" % (login_adh, exemplaire, code_ressource, date(Nyear_pret,Nmonth_pret,Nday_pret), nb_jours,date(Nyear_retour,Nmonth_retour,Nday_retour),etat_retour)
    cur.execute(sql)
