from datetime import date

def ajouter_document(cur, login):
    sql = "select code from ressource;"
    cur.execute(sql)
    raw = cur.fetchall()
    existants = []
    for ligne in raw:
        existants.append(ligne[0])
    print(existants)
    Ncode = int(input("Veuillez saisir le code du document\n"))
    while Ncode in existants and Ncode != "exit":
        Ncode = int(input("L'code saisi existe déjà! Veuillez ressaisir. Si vous voulez quitter, entrez exit\n"))
    
    if Ncode != "exit":
        #Informations générales
        #Titre
        Ntitre = input("Veuillez saisir le titre de la ressource\n") 
        #Datetime
        Nyear = int(input("Veuillez saisir l'année d'apprarition de la ressource\n"))
        Nmonth = int(input("Veuillez saisir le mois d'apprarition de la ressource\n"))
        Nday = int(input("Veuillez saisir l'année d'apprarition de la ressource\n"))
        while date(Nyear, Nmonth, Nday) > date.today():
            print("La date saisie impossible! Veuillez ressaisir.\n")
            Nyear = int(input("Veuillez saisir l'année d'apprarition de la ressource\n"))
            Nmonth = int(input("Veuillez saisir le mois d'apprarition de la ressource\n"))
            Nday = int(input("Veuillez saisir la date d'apprarition de la ressource\n"))
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

        sql = "insert into ressource values ('%s', '%s', '%s', '%s', '%s', '%s');" % (Ncode, Ntitre, date(Nyear, Nmonth, Nday), Nediteur, Ngenre, Ncode_classification)
        cur.execute(sql)
        

        '''
        #Distinction type
        NtypeRessource = int(input("Veuillez saisir l'indice du type de la ressource\n"))
        print("1 :Film\n2 : Enregistrement musical\n3 : Livre\n")
        while NtypeRessource not in [1, 2, 3]:
            NtypeRessource = int(input("Erreur! Veuillez resaisir l'indice du type de la ressource\n"))
        if NtypeRessource==1:
            NtypeRessource = "Film"
        elif NtypeRessource==2:
            NtypeRessource = "Film"
        elif NtypeRessource==3:
            NtypeRessource = "Livre"
        '''



        

                    






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
                gerer_pret(cur, login)
            elif user_choix1=="3":
                gerer_user(cur, login)
            elif user_choix1=="4":
                analyser(cur, login)
            else :
                print("Veuillez effectuer une saisie valide")