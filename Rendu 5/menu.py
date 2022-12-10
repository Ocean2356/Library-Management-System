import psycopg2
from datetime import date
from jingfang import gerer_ressources, ajouter_document, supprimer_document, modifier_document
from haiyang import recherche, visualiser
from lilian_valin import Gerer_pret, Affichage_pret_en_cour, Affichage_pret_fini, Nouveau_pret, Retour_pret, Analyser, Document_recommande
from abdallah import gerer_user

# Login PSQL
def connexion():
    conn = psycopg2.connect(
        user="postgres",
        password="2812",
        host="localhost",
        port="5432",
        database="postgres")
    return conn

"""# Login BDD UTC
def connexion():
    HOST = "tuxa.sme.utc"
    USER = "nf18a074"
    PASSWORD = "ulk6EDbE"
    DATABASE = "dbnf18a074"
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    return conn"""

def adherant(cur, login):
    #partie menu adherant
    user_choix1 = -1
    while user_choix1!="0": #partie adhérant pour l'instant
        print("--------------------------------------------------------")
        print("1 Rechercher un document") #haiyang
        print("2 Visualiser vos emprunts") #haiyang
        print("3 Recommandation")  # Lilian
        print("0 Déconnexion")
        user_choix1 = input("Sélectionner un choix : ")
        if user_choix1!="0":
            if user_choix1=="1":
                recherche(cur)
            elif user_choix1=="2":
                visualiser(cur, login)
            elif user_choix1=="3":
                Document_recommande(cur, login)
            else :
                print("Veuillez effectuer une saisie valide !")


def admin(cur, login):
    #partie menu admin
    user_choix1 = -1
    while user_choix1!="0": #partie adhérant pour l'instant
        print("--------------------------------------------------------")
        print("1 Gérer les ressources") #Jingfang
        print("2 Gestion des prêts") #Lilian
        print("3 Gestion des utilisateurs") #Abdallah
        print("4 Analyser les données") #Lilian
        print("0 Déconnexion")
        user_choix1 = input("Selectionner un choix : ")
        if user_choix1!="0":
            if user_choix1=="1":
                gerer_ressources(cur, login)
            elif user_choix1=="2":
                Gerer_pret(cur, login)
            elif user_choix1=="3":
                gerer_user(cur, login)
            elif user_choix1=="4":
                Analyser(cur)
            else :
                print("Veuillez effectuer une saisie valide !")


user_choix = -1
conn = connexion()
cur = conn.cursor()
while user_choix!="0": #partie adhérant pour l'instant
    print("--------------------------------------------------------")
    print("1 Connexion")
    print("0 Quitter")
    user_choix = input("Saisir votre choix : ")
    #Partie log in
    if user_choix=="1":
        login = input("Saisir votre login : ")
        mot_de_passe = input("Saisir votre mot de passe : ")
        #login = "tutu.yuan"
        #mot_de_passe = "iop"
        sql  = "select login, mot_de_passe from compte_adherent where login='%s' and mot_de_passe='%s';" % (login, mot_de_passe)
        cur.execute(sql)
        raw = cur.fetchone()
        if raw:
            adherant(cur, login)
        else :
            sql  = "select login, mot_de_passe from compte_personnel where login='%s' and mot_de_passe='%s';" % (login, mot_de_passe)
            cur.execute(sql)
            raw = cur.fetchone()
            if raw:
                admin(cur, login)
            else :
                print("Saisie non valide !")
        conn.commit()

conn.close()

