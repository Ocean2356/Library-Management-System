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
                Retourner_pret(cur)
            else:
                print("Veuillez effectuer une saisie valide !")

def Affichage_pret_en_cour(cur):
    user_choix = -1
    i_pret = 0
    sql="select * from pret where etat_retour is null"
    cur.execute(sql)
    raw = cur.fetchall()
    if raw == []:
        print("--------------------")
        print("Aucun prêt en cours")
        print("--------------------")
        user_choix = "0"
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
    print("Entrée le login de l'adherent")
    login_adh = input("login : ")
    Nyear_pret = int(input("Veuillez saisir l'année du prêt\n"))
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt\n"))
    Nday_pret = int(input("Veuillez saisir le jour du prêt\n"))
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        print("La date saisie impossible! Veuillez ressaisir.\n")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt\n"))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt\n"))
        Nday_pret = int(input("Veuillez saisir le jour du prêt\n"))
    nb_jours = input("nombre de jours : ")
    print("Entrée le numéro de l'exemplaire prêté")
    exemplaire = int(input("numéro : "))
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("code ressource : "))
    sql = "insert into pret values ('%s','%s','%s','%s','%s');"%(login_adh, exemplaire, code_ressource, date(Nyear_pret,Nmonth_pret,Nday_pret), nb_jours)
    cur.execute(sql)
