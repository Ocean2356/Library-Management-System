import psycopg2

def connexion():
    HOST = "tuxa.sme.utc"
    USER = "nf18a061"
    PASSWORD = "l0ixTFxR"
    DATABASE = "dbnf18a061"
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()
    return cur


def adherant(cur, login):
    #partie menu adherant
    user_choix1 = -1
    while user_choix1!="0": #partie adhérant pour l'instant
        print("1 Rechercher un document")
        print("2 Visualiser vos emprunts")
        print("0 Deconnexion")
        user_choix1 = input("Selectionner un choix")
        if user_choix1!="0":
            if user_choix1=="1":
                recherche()
            elif user_choix1=="2":
                visualiser(cur, login)
            else :
                print("Veuillez effectuer une saisie valide")


def admin(cur, login):
    #partie menu admin
    user_choix1 = -1
    while user_choix1!="0": #partie adhérant pour l'instant
        print("1 Gerer les ressources")
        print("2 Gestion des prêts")
        print("3 Gestion des utilisateurs")
        print("4 Analyser les données")
        print("0 Deconnexion")
        user_choix1 = input("Selectionner un choix")
        if user_choix1!="0":
            if user_choix1=="1":
                gerer_ressources(cur, login)
            elif user_choix1=="2":
                gerer_pret(cur, login)
            elif user_choix1=="3":
                gerer_user(cur, login)
            elif user_choix1=="4":
                analyser(cur, login)
            else :
                print("Veuillez effectuer une saisie valide")







user_choix = -1

while user_choix!="0": #partie adhérant pour l'instant
    #user_choix1 = -1
    cur = connexion()
    print("1 connexion")
    print("0 Quitter")
    user_choix = input("Saisir votre choix")
    #Partie log in
    if user_choix=="1":
        login = input("Saisir votre login")
        mot_de_passe = input("Saisir votre mot de passe")
        sql  = "select login, mot_de_passe from compte_adherent where login='%s' and mot_de_passe='%s';" % (login, mot_de_passe)
        cur.execute(sql)
        raw = cur.fetchone()
        #print(raw)
        if raw:
            adherant(cur, login)
        else :
            sql  = "select login, mot_de_passe from compte_personnel where login='%s' and mot_de_passe='%s';" % (login, mot_de_passe)
            cur.execute(sql)
            raw = cur.fetchone()
            if raw:
                admin(cur, login)
            else :
                print("Saisie non valide")
    elif user_choix=="0":
        exit()

conn.close()