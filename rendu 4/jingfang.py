from datetime import date
import psycopg2

def ajouter_document(cur, login):
    sql = "select code from ressource;"
    cur.execute(sql)
    raw = cur.fetchall()
    existants = []
    for ligne in raw:
        existants.append(ligne[0])
    print(existants)
    Ncode = int(input("Veuillez saisir le code du document\n"))
    while Ncode != "exit" and int(Ncode) in existants:
        Ncode = input("L'code saisi existe déjà! Veuillez ressaisir. Si vous voulez quitter, entrez exit\n")
    
    if Ncode != "exit":
        Ncode = int(Ncode)
        #Informations générales
        #Titre
        Ntitre = input("Veuillez saisir le titre de la ressource\n") 
        #Datetime
        tester = False
        while not tester: 
            try:
                Nyear = int(input("Veuillez saisir l'année d'apprarition de la ressource\n"))
                Nmonth = int(input("Veuillez saisir le mois d'apprarition de la ressource\n"))
                Nday = int(input("Veuillez saisir le jour d'apprarition de la ressource\n"))
            except Exception:
                print("Problème de saisie, rééssayer")
            else:
                try: 
                    if date(Nyear, Nmonth, Nday) > date.today():
                        print("La date saisie impossible! Veuillez ressaisir.\n")
                except Exception:
                    print("La date saisie impossible! Veuillez ressaisir.\n")
                else:
                    tester = True
        #Code de classification
        sql = "select code_classification from ressource;"
        cur.execute(sql)
        raw = cur.fetchall()
        existants = []
        for ligne in raw:
            existants.append(ligne[0])
        print(existants)
        Ncode_classification = int(input("Veuillez saisir le code de classification du document\n"))
        while Ncode_classification in existants:
            Ncode_classification = int(input("L'code saisi existe déjà! Veuillez ressaisir\n"))
        #autre
        Nediteur = input("Veuillez saisir l'éditeur de la ressource\n")
        Ngenre = input("Veuillez saisir le genre de la ressource\n")

        sql = "insert into ressource values ('%d', '%s', '%s', '%s', '%s', '%d');" % (Ncode, Ntitre, date(Nyear, Nmonth, Nday), Nediteur, Ngenre, Ncode_classification)
        cur.execute(sql)
        

        
        #Distinction type
        print("1 : Film\n2 : Enregistrement musical\n3 : Livre\n")
        NtypeRessource = int(input("Veuillez saisir l'indice du type de la ressource\n"))
        while NtypeRessource not in [1, 2, 3]:
            NtypeRessource = int(input("Erreur! Veuillez resaisir l'indice du type de la ressource\n"))
        if NtypeRessource==1:
            #Film
            print("Vous avez choisi Film\n")
            Nlongeur = input("Veuillez saisir la longeur du film, format HH:MM:SS\n")
            Nlangue = input("Veuillez saisir la langue du film\n")
            Nsynopsis = input("Veuillez saisir le synopsis du film\n")
            sql = "insert into film values ('%s', '%s', '%s', '%s');" % (Nlangue, Nlongeur, Nsynopsis, Ncode)
        elif NtypeRessource==2:
            #Music
            Nlongeur = input("Veuillez saisir la longeur de l'enregistrement, format HH:MM:SS\n")
            sql = "insert into oeuvre_musicale values ('%s', '%s');" % (Nlongeur,Ncode)

        elif NtypeRessource==3:
            #Livre
            sql = "select isbn from livre;"
            cur.execute(sql)
            raw = cur.fetchall()
            existants = []
            for ligne in raw:
                existants.append(ligne[0])
            print("Vous avez choisi Livre\n")
            Nisbn = int(input("Veuillez saisir le code ISBN du livre\n"))
            while Nisbn in existants:
                Nisbn = int(input("L'code saisi existe déjà! Veuillez ressaisir. Si vous voulez quitter, entrez exit\n"))
            Nlangue = input("Veuillez saisir la langue du livre\n")
            Nresume = input("Veuillez saisir le resumé du livre\n")
            sql = "insert into livre values ('%d', '%s', '%s', '%s');" % (Nisbn, Nlangue, Nresume, Ncode)
        
        cur.execute(sql)

        #Partie Contributeurs
        NbContrib = int(input("Il existe combien de comtributeurs ?\n"))
        for i in range(0, NbContrib):
            print("%d contributeur\n"%i)
            contributeur(Ncode, NtypeRessource, cur)


def contributeur(Ncode, NtypeRessource, cur):
    #Informations générales
    #Partir ID Contrib
    sql = "select id_contributeur, nom, prenom from contributeur;"
    cur.execute(sql)
    raw = cur.fetchall()
    existants = []
    print("Liste Contributeur dans le système\n")
    if not raw:
        print("Liste vide\n")
    else:
        for ligne in raw:
            print("\t%s \t%s \t%s\n"%(ligne[0], ligne[1], ligne[2]))
            existants.append(ligne[0])
    Nid_contributeur = int(input("Veuillez saisir le ID contributeur\n"))#A améliorer
    if Nid_contributeur not in existants:
        #Nouveau contributeur
        #Partie nom prénom
        Nnom = input("Veuillez saisir le nom du contributeur\n")
        Nprenom = input("Veuillez saisir le prénom du contributeur\n")
            
        #Partie date de naissance
        #Datetime
        tester = False
        while not tester: 
            try:
                Nyear = int(input("Veuillez saisir l'année de naissance\n"))
                Nmonth = int(input("Veuillez saisir le mois de naissance\n"))
                Nday = int(input("Veuillez saisir le jour de naissance\n"))
            except Exception:
                print("Problème de saisie, rééssayer")
            else:
                try: 
                    if date(Nyear, Nmonth, Nday) > date.today():
                        print("La date saisie impossible! Veuillez ressaisir.\n")
                except Exception:
                    print("La date saisie impossible! Veuillez ressaisir.\n")
                else:
                    tester = True
        #Partie nationalité
        Nnation = input("Veuillez saisir la nationalité du contributeur\n")

        sql = "insert into contributeur values ('%d', '%s', '%s', '%s', '%s');" % (Nid_contributeur, Nnom, Nprenom, date(Nyear, Nmonth, Nday), Nnation)
        cur.execute(sql)
    else:
        #Contributeur existant
        print("Vous avez sélectionné un contributeur existant\n")


    #Distinction Type
    if NtypeRessource==1:
        print("Selectionner parmi ces 2 types\n1 Réalisateur\n2 Acteur\n")
        tester = False
        while not tester: 
            try:
                NtypeContrib = int(input())
            except Exception:
                print("Problème de saisie, rééssayer\n")
            else:
                if NtypeContrib not in [1, 2]:
                    print("Choix impossible, rééssayer\n")
                else:
                    tester = True
        if NtypeContrib==1:
            sql = "insert into realisateur values ('%s', '%s');" % (Ncode, Nid_contributeur)
        else:
            sql = "insert into acteur values ('%s', '%s');" % (Ncode, Nid_contributeur)
    elif NtypeRessource==2:
        print("Selectionner parmi ces 2 types\n1 Compositeur\n2 Interprete\n")
        tester = False
        while not tester: 
            try:
                NtypeContrib = int(input())
            except Exception:
                print("Problème de saisie, rééssayer\n")
            else:
                if NtypeContrib not in [1, 2]:
                    print("Choix impossible, rééssayer\n")
                else:
                    tester = True
        if NtypeContrib==1:
            sql = "insert into compositeur values ('%s', '%s');" % (Ncode, Nid_contributeur)
        else:
            sql = "insert into interprete values ('%s', '%s');" % (Ncode, Nid_contributeur)

    elif NtypeRessource==3:
        sql = "insert into auteur values ('%s', '%s');" % (Ncode, Nid_contributeur)
    
    cur.execute(sql)



def modifier_document(cur, login):      #Fonction non testée, serveur PSQL est en panne 
    dict_livres = {1:"code",  2:"titre", 3:"date_apparition", 4:"editeur", 5:"genre", 6:"code_classification", 7:"ISBN", 8:"langue", 9:"résumé"}
    dict_musics = {1:"code",  2:"titre", 3:"date_apparition", 4:"editeur", 5:"genre", 6:"code_classification", 7:"longeur"}
    dict_films = {1:"code",  2:"titre", 3:"date_apparition", 4:"editeur", 5:"genre", 6:"code_classification", 7:"langue", 8:"longeur", 9:"synopsis"}
    sql = "select * from film_all;"
    cur.execute(sql)
    raw = cur.fetchall()
    films = []
    print("Les livres dans le système\n")
    if not raw:
        print("Liste vide\n")
    else:
        print("\tcode \ttitre \tdate_apparition \tediteur \tgenre \tcode_classification \tlangue \tlongeur \tsynopsis\n")
        for ligne in raw:
            print("\t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s\n"%(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6], ligne[7], ligne[8]))
            films.append(ligne[0])
    
    sql = "select * from livre_all;"
    cur.execute(sql)
    raw = cur.fetchall()
    livres = []
    print("Les films dans le système\n")
    if not raw:
        print("Liste vide\n")
    else:
        print("\tcode \ttitre \tdate_apparition \tediteur \tgenre \tcode_classification \tISBN \tlangue \trésumé\n")
        for ligne in raw:
            print("\t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s\n"%(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6], ligne[7], ligne[8]))
            livres.append(ligne[0])


    sql = "select * from music_all;"
    cur.execute(sql)
    raw = cur.fetchall()
    musics = []
    print("Les enregistrements musicaux dans le système\n")
    if not raw:
        print("Liste vide\n")
    else:
        print("\tcode \ttitre \tdate_apparition \tediteur \tgenre \tcode_classification \tlongeur\n")
        for ligne in raw:
            print("\t%s \t%s \t%s \t%s \t%s \t%s \t%s\n"%(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6]))
            musics.append(ligne[0])

    print("Veuillez saisir un code\n")
    tester = False
    while not tester: 
        try:
            Mcode = int(input())
        except Exception:
            print("Problème de saisie, rééssayer\n")
        else:
            if Mcode not in livres and Mcode not in music and Mcode not in films:
                print("Choix impossible, rééssayer\n")
            else:
                tester = True
    
    print("Vous voulez modifier quel attribut ?\n")
    if Mcode in livres:
        print("1 code \n2 titre \n3 date_apparition \n4 editeur \n5 genre \n6 code_classification \n7 isbn \n8 langue \n9 résumé\n")
        tester = False
        while not tester: 
            try:
                Mchoix = int(input())
            except Exception:
                print("Problème de saisie, rééssayer\n")
            else:
                if Mchoix not in dict_livres:
                    print("Choix impossible, rééssayer\n")
                else:
                    tester = True
        Mvaleur = input("Veuillez saisir la nouvelle valeur\n")
        if Mchoix==1:
            sql = "UPDATE ressource SET %s = '%s' WHERE code='%s';UPDATE livre SET %s = '%s' WHERE ressource='%s';"%(dict_livres[Mchoix], Mchoix, Mcode, dict_livres[Mchoix], Mchoix, Mcode)#Possiblement problématique

        elif Mchoix<=6:
            sql = "UPDATE ressource SET %s = '%s' WHERE code='%s';"%(dict_livres[Mchoix], Mchoix, Mcode)
        else:
            sql = "UPDATE livre SET %s = '%s' WHERE ressource='%s';"%(dict_livres[Mchoix], Mchoix, Mcode)
    elif Mcode in musics:
        print("1 code \n2 titre \n3 date_apparition \n4 editeur \n5 genre \n6 code_classification \n7 longeur\n")
        tester = False
        while not tester: 
            try:
                Mchoix = int(input())
            except Exception:
                print("Problème de saisie, rééssayer\n")
            else:
                if Mchoix not in dict_musics:
                    print("Choix impossible, rééssayer\n")
                else:
                    tester = True
        Mvaleur = input("Veuillez saisir la nouvelle valeur\n")
        if Mchoix==1:
            sql = "UPDATE ressource SET %s = '%s' WHERE code='%s';UPDATE oeuvre_musicale SET %s = '%s' WHERE ressource='%s';"%(dict_musics[Mchoix], Mchoix, Mcode, dict_musics[Mchoix], Mchoix, Mcode)#Possiblement problématique
        elif Mchoix<=6:
            sql = "UPDATE ressource SET %s = '%s' WHERE code='%s';"%(dict_musics[Mchoix], Mchoix, Mcode)
        else:
            sql = "UPDATE oeuvre_musicale SET %s = '%s' WHERE ressource='%s';"%(dict_musics[Mchoix], Mchoix, Mcode)

    else:
        print("1 code \n2 titre \n3 date_apparition \n4 editeur \n5 genre \n6 code_classification \n7 langue \n8 longeur \n9 synopsis\n")
        tester = False
        while not tester: 
            try:
                Mchoix = int(input())
            except Exception:
                print("Problème de saisie, rééssayer\n")
            else:
                if Mchoix not in dict_films:
                    print("Choix impossible, rééssayer\n")
                else:
                    tester = True
        Mvaleur = input("Veuillez saisir la nouvelle valeur\n")
        if Mchoix==1:
            sql = "UPDATE ressource SET %s = '%s' WHERE code='%s';UPDATE film SET %s = '%s' WHERE ressource='%s';"%(dict_films[Mchoix], Mchoix, Mcode, dict_films[Mchoix], Mchoix, Mcode)#Possiblement problématique
        elif Mchoix<=6:
            sql = "UPDATE ressource SET %s = '%s' WHERE code='%s';"%(dict_films[Mchoix], Mchoix, Mcode)
        else:
            sql = "UPDATE film SET %s = '%s' WHERE ressource='%s';"%(dict_films[Mchoix], Mchoix, Mcode)
    
    try:
        cur.execute(sql)
    except Exception:
        print("Problème lors de l'insertion, opération échouée\n")



def supprimer_document(cur, login): #Fonction non testée, serveur PSQL est en panne 
    sql = "select * from ressource;"
    cur.execute(sql)
    raw = cur.fetchall()
    existants = []
    if not raw:
        print("Liste vide\n")
    else:
        print("\tcode \ttitre \tdate_apparition \tediteur \tgenre \tcode_classification\n")
        for ligne in raw:
            print("\t%s \t%s \t%s \t%s \t%s \t%s \n"%(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5]))
            existants.append(ligne[0])
    tester = False
    while not tester: 
        try:
            Scode = int(input("Veuillez saisir le code du document à supprimer\n"))
        except Exception:
            print("Problème de saisie\n")
        else:
            if Scode != "exit" and Scode not in existants:
                print("L'code saisi n'est pas dans le système! Veuillez ressaisir. Si vous voulez quitter, entrez exit\n")
            else:
                tester = True
    sql = "delete from ressource where code='%s'"%Scode
    cur.execute(sql)
    

            

def gerer_ressources(cur, login):
    user_choix1 = -1
    while user_choix1!="0":
        print("1 Ajouter un nouveau document") 
        print("2 Modifier un un document") 
        print("3 Supprimer un un document")
        print("0 Revenir")
        user_choix1 = input("Selectionner un choix")
        if user_choix1!="0":
            if user_choix1=="1":
                ajouter_document(cur, login)
            elif user_choix1=="2":
                modifier_document(cur, login)
            elif user_choix1=="3":
                supprimer_document(cur, login)
            else :
                print("Veuillez effectuer une saisie valide")

""" HOST = "tuxa.sme.utc"
USER = "nf18a074"
PASSWORD = "ulk6EDbE"
DATABASE = "dbnf18a074"
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
cur = conn.cursor()


ajouter_document(cur, "tutu.yuan") 

conn.commit()

conn.close() """