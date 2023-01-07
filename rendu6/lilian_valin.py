from datetime import date


def gerer_pret(cur):
    # Initialisation de la variable user_choix à -1
    user_choix = -1
    # Boucle tant qu'user_choix n'est pas égal à 0.
    while user_choix != "0":
        # Affichage du menu
        print("--------------------------------------------------------")
        print("1 Afficher les prêts en cours")
        print("2 Afficher les prêts terminé")
        print("3 Crée un nouveau prêt")
        print("4 Retourner un prêt")
        print("5 Gérer les réservations")
        print("0 Quitter")
        # Demande de sélection d'une option par l'utilisateur
        user_choix = input("Sélectionner un choix : ")
        # Si l'utilisateur ne sélectionne pas l'option 0
        if user_choix != "0":
            # Selon l'option sélectionnée, appel de la fonction associée
            if user_choix == "1":
                affichage_pret_en_cour(cur)
            elif user_choix == "2":
                affichage_pret_fini(cur)
            elif user_choix == "3":
                nouveau_pret(cur)
            elif user_choix == "4":
                retour_pret(cur)
            elif user_choix == "5":
                gerer_reservation(cur)
            # Si l'option sélectionnée n'est pas valide
            else:
                # Affichage d'un message d'erreur
                print("Veuillez effectuer une saisie valide !")


def affichage_pret_en_cour(cur):
    # Initialisation de la variable user_choix à -1
    user_choix = -1
    # Initialisation de la variable i_pret à 0.
    i_pret = 0
    # Création de la requête SQL pour récupérer les prêts en cours
    sql = "select * from pret where etat_retour is null"
    # Exécution de la requête SQL
    cur.execute(sql)
    # Récupération du résultat de la requête
    raw = cur.fetchall()
    # Si aucun prêt n'est en cours
    if not raw:
        # Affichage d'un message
        print("--------------------")
        print("Aucun prêt en cours")
        print("--------------------")
        # Affectation de 0 à user_choix pour sortir de la boucle
    # S'il y a des prêts en cours
    else:
        # Initialisation de la variable nombre_pret avec le nombre de prêts en cours
        nombre_pret = len(raw)
        # Boucle tant qu'user_choix n'est pas égal à 0.
        while user_choix != "0":
            # Affichage des informations du prêt en cours
            print("_" * 50)
            print("Le document à était emprunté par :", raw[i_pret][0])
            print("C'est l'exemplaire numéro : ", raw[i_pret][1])
            print("Le code du document est : ", raw[i_pret][2])
            print("Le début du prêt est en date du : ", raw[i_pret][3])
            print("La durée du prêt est de ", raw[i_pret][4], "jours")
            print("_" * 50)
            print("1 Pour passer au prêt suivant")
            print("0 Pour quitter")
            # Demande de sélection d'une option par l'utilisateur
            user_choix = input("Sélectionner un choix : ")
            # Si l'utilisateur sélectionne l'option 1
            if user_choix == "1":
                # Si le prêt courant n'est pas le dernier
                if i_pret + 1 < nombre_pret:
                    # Passage au prêt suivant
                    i_pret += 1
                # Si le prêt courant est le dernier
                elif i_pret + 1 == nombre_pret:
                    # Retour au premier prêt
                    i_pret = 0


def affichage_pret_fini(cur):
    # Initialisation de la variable user_choix à -1
    user_choix = -1
    # Initialisation de la variable i_pret à 0.
    i_pret = 0
    # Création de la requête SQL pour récupérer les prêts terminés
    sql = "select * from pret where etat_retour is not null"
    # Exécution de la requête SQL
    cur.execute(sql)
    # Récupération du résultat de la requête
    raw = cur.fetchall()
    # Si aucun prêt n'est terminé
    if not raw:
        # Affichage d'un message
        print("--------------------")
        print("Aucun prêt en fini")
        print("--------------------")
    # S'il y a des prêts terminés
    else:
        # Initialisation de la variable nombre_pret avec le nombre de prêts terminés
        nombre_pret = len(raw)
        # Boucle tant qu'user_choix n'est pas égal à 0.
        while user_choix != "0":
            # Affichage des informations du prêt terminé
            print("_" * 50)
            print("Le document à était emprunté par :", raw[i_pret][0])
            print("C'est l'exemplaire numéro : ", raw[i_pret][1])
            print("Le code du document est : ", raw[i_pret][2])
            print("Le début du prêt est en date du : ", raw[i_pret][3])
            print("La durée du prêt est de ", raw[i_pret][4], "jours")
            print('La date de retour est le : ', raw[i_pret][5])
            print("l'état au retour est ", raw[i_pret][6])
            print("_" * 50)
            print("1 Pour passer au prêt suivant")
            print("0 Pour quitter")
            # Demande de sélection d'une option par l'utilisateur
            user_choix = input("Sélectionner un choix : ")
            # Si l'utilisateur sélectionne l'option 1
            if user_choix == "1":
                # Si le prêt courant n'est pas le dernier
                if i_pret + 1 < nombre_pret:
                    i_pret += 1
                elif i_pret + 1 == nombre_pret:
                    i_pret = 0


def nouveau_pret(cur):
    # Initialisation d'exemplaire_prete à 1.
    exemplaire_prete = 1
    # Demande de saisie du login de l'adhérent
    print("Entrée le login de l'adhérent")
    login_adh = input("Login : ")
    # Création de la requête SQL pour vérifier l'existence de l'adhérent
    sql = "select login from compte_adherent where login='%s';" % login_adh
    # Exécution de la requête SQL
    cur.execute(sql)
    # Récupération du résultat de la requête
    raw = cur.fetchone()
    # Si l'adhérent n'existe pas
    while not raw:
        # Demande de saisie d'un login valide
        print("login invalide, veuillez réessayer")
        login_adh = input("Login : ")
        # Création de la requête SQL pour vérifier l'existence de l'adhérent
        sql = "select login from compte_adherent where login='%s';" % login_adh
        # Exécution de la requête SQL
        cur.execute(sql)
        # Récupération du résultat de la requête
        raw = cur.fetchone()
    # Demande de saisie de la date de prêt
    print("Entrée la date de prêt ")
    # Saisie de l'année de prêt
    # Saisie de l'année de prêt
    Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
    # Saisie du mois de prêt
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
    # Saisie du jour de prêt
    Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    # Vérification que la date de prêt saisie est bien antérieure à la date d'aujourd'hui.
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        # Si la date de prêt est postérieure à la date d'aujourd'hui, demande de saisie d'une date valide.
        print("La date saisie est impossible! Veuillez réessayer !")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
        Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    # Saisie de la durée du prêt en jours
    print("Entrée la durée du prêt en jours")
    nb_jours = input("Nombre de jours : ")
    # Demande de saisie du code de la ressource prêtée
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("Code ressource : "))
    # Demande de saisie du numéro de l'exemplaire prêté
    print("Entrée le numéro de l'exemplaire prêté")
    exemplaire = int(input("Numéro : "))
    # Création de la requête SQL pour vérifier que l'exemplaire n'est pas déjà en prêt
    sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % exemplaire
    # Exécution de la requête SQL
    cur.execute(sql)
    # Récupération du résultat de la requête
    raw = cur.fetchone()
    # Si l'exemplaire est déjà en prêt
    if raw:
        # Mise à jour de la valeur d'exemplaire_prete
        exemplaire_prete = 0
    # Tant que l'exemplaire est déjà en prêt
    while exemplaire_prete == 0:
        # Demande si l'utilisateur souhaite réserver l'exemplaire
        print("Exemplaire déjà en prêté, voulez vous le réserver ?")
        print("1 Oui")
        print("0 Non")
        # Saisie du choix de l'utilisateur
        user_choix = int(input("Saisir un choix : "))
        # Si l'utilisateur souhaite réserver l'exemplaire
        if user_choix == 1:
            # Appel de la fonction Reservation avec en paramètres le login de l'adhérent et le code de la ressource
            reservation(login_adh, code_ressource, cur)
            # Fin de la fonction
            exit()
        # Si l'utilisateur ne souhaite pas réserver l'exemplaire
        if user_choix == 0:
            # Demande de saisie du code de la ressource prêtée
            print("Entrée le code la ressource prêté")
            code_ressource = int(input("Code ressource : "))
            # exemplaire
            print("Entrée le numéro de l'exemplaire prêté")
            # Saisie du numéro de l'exemplaire prêté
            exemplaire = int(input("Numéro : "))
            # Création de la requête SQL pour vérifier que l'exemplaire n'est pas déjà en prêt
            sql = "select exemplaire from pret where exemplaire='%s' and date_retour is null;" % exemplaire
            # Exécution de la requête SQL
            cur.execute(sql)
            # Récupération du résultat de la requête
            raw = cur.fetchone()
            # Si l'exemplaire n'est pas déjà en prêt
            if not raw:
                # Mise à jour de la valeur d'exemplaire_prete
                exemplaire_prete = 1
        # Création de la requête SQL d'insertion des informations de prêt dans la table pret
        sql = "insert into pret(adherent,exemplaire,code_ressource,date_pret,duree_pret) values ('%s','%s','%s','%s','%s');" % (login_adh, exemplaire, code_ressource, date(Nyear_pret, Nmonth_pret, Nday_pret), nb_jours)
        # Exécution de la requête SQL
        cur.execute(sql)
        print("Prêt enregistré")


def retour_pret(cur):
    # Demander le login de l'adhérent
    print("Entrée le login de l'adhérent")
    login_adh = input("Login : ")
    # Vérifier si l'adhérent a un prêt en cours
    sql = "select adherent from pret where adherent='%s' and date_retour is null;" % login_adh
    cur.execute(sql)
    raw = cur.fetchone()
    # Si l'adhérent n'a pas de prêt en cours, demander de réessayer
    while not raw:
        print("Login invalide, veuillez réessayer !")
        login_adh = input("Login : ")
        sql = "select adherent from pret where adherent='%s'and date_retour is null;" % login_adh
        cur.execute(sql)
        raw = cur.fetchone()
    # Demander la date de prêt
    print("Entrée la date de prêt ")
    Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
    Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
    Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    # Vérifier que la date de prêt saisie est antérieure à la date actuelle
    while date(Nyear_pret, Nmonth_pret, Nday_pret) > date.today():
        print("La date saisie est impossible ! Veuillez ressaisir !")
        Nyear_pret = int(input("Veuillez saisir l'année du prêt : "))
        Nmonth_pret = int(input("Veuillez saisir le mois du prêt : "))
        Nday_pret = int(input("Veuillez saisir le jour du prêt : "))
    # Demander le code de la ressource prêtée
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("Code ressource : "))
    # Demander le numéro de l'exemplaire prêté
    print("Entrée le numéro de l'exemplaire prêté")
    exemplaire = int(input("Numéro : "))
    # Vérifier si l'exemplaire est actuellement prêté
    sql = "select exemplaire from pret where exemplaire ='%s' and date_retour is null;" % exemplaire
    cur.execute(sql)
    raw = cur.fetchone()
    # test exemplaire
    while not raw:
        print("Exemplaire non prêté, veuillez réessayer")
        exemplaire = int(input("Numéro : "))
        sql = "select exemplaire from pret where exemplaire ='%s' and date_retour is null;" % exemplaire
        cur.execute(sql)
        raw = cur.fetchone()
    # Demander la date de retour
    Nyear_retour = int(input("Veuillez saisir l'année du retour\n"))
    Nmonth_retour = int(input("Veuillez saisir le mois du retour\n"))
    Nday_retour = int(input("Veuillez saisir le jour du retour\n"))
    # Vérifier que la date de retour saisie est antérieure à la date actuelle
    while date(Nyear_retour, Nmonth_retour, Nday_retour) > date.today():
        print("La date saisie est impossible ! Veuillez ressaisir.\n")
        Nyear_retour = int(input("Veuillez saisir l'année du retour\n"))
        Nmonth_retour = int(input("Veuillez saisir le mois du retour\n"))
        Nday_retour = int(input("Veuillez saisir le jour du retour\n"))
    # Demander l'état de la ressource au moment du retour
    print("Entrée l'état de la ressource (neuf,bon,abîmé,perdu)")
    etat_retour = input("Veuillez saisir l'état : ")
    # Vérifier que l'état saisi est valide
    while (etat_retour != 'neuf') and (etat_retour != 'bon') and (etat_retour != 'abîmé') and (etat_retour != 'perdu'):
        print("Etat incorrect, veuillez réessayer")
        etat_retour = input("Veuillez saisir l'état : ")
    # Mettre à jour la base de données avec les informations de retour de prêt
    sql = "update pret set date_retour='%s', etat_retour='%s' where adherent='%s' and code_ressource='%s' and exemplaire='%s';" % (date(Nyear_retour, Nmonth_retour, Nday_retour), etat_retour, login_adh, code_ressource, exemplaire)
    cur.execute(sql)
    print("Retour enregistré")


def reservation(login_adh, code_ressource, cur):
    # Demander la date de réservation
    print("Entrée la date de réservation ")
    Nyear_reservation = int(input("Veuillez saisir l'année du réservation : "))
    Nmonth_reservation = int(input("Veuillez saisir le mois du réservation : "))
    Nday_reservation = int(input("Veuillez saisir le jour du réservation : "))
    # Vérifier que la date de réservation saisie est antérieure à la date actuelle
    while date(Nyear_reservation, Nmonth_reservation, Nday_reservation) > date.today():
        print("La date saisie est impossible ! Veuillez ressaisir !")
        Nyear_reservation = int(input("Veuillez saisir l'année du réservation : "))
        Nmonth_reservation = int(input("Veuillez saisir le mois du réservation : "))
        Nday_reservation = int(input("Veuillez saisir le jour du réservation : "))
    # Insérer les informations de réservation dans la base de données
    sql = "insert into reservation(adherent, ressource, date_reserve) values ('%s','%s','%s');" % (
        login_adh, code_ressource, date(Nyear_reservation, Nmonth_reservation, Nday_reservation))
    cur.execute(sql)
    print("Réservation enregistrée")


def gerer_reservation(cur):
    # Initialiser la variable de choix de l'utilisateur à une valeur non valide
    user_choix = -1
    # Boucle tant que l'utilisateur ne choisit pas de quitter (choix 0)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("1 Afficher les réservations en cours")
        print("2 Supprimer une réservation")
        print("0 Quitter")
        user_choix = input("Sélectionner un choix : ")
        # Si l'utilisateur ne choisit pas de quitter, exécuter l'option choisie
        if user_choix != "0":
            if user_choix == "1":
                # Afficher les réservations en cours
                affichage_reservation(cur)
            elif user_choix == "2":
                # Supprimer une réservation
                supprimer_reservation(cur)
            else:
                # Si l'utilisateur saisi une option non valide, afficher un message d'erreur
                print("Veuillez effectuer une saisie valide !")


def affichage_reservation(cur):
    # Initialiser la variable de choix de l'utilisateur à une valeur non valide
    user_choix = -1
    # Initialiser l'index de la réservation affichée à 0.
    i_pret = 0
    # Récupérer les informations de toutes les réservations de la base de données
    sql = "select * from reservation"
    cur.execute(sql)
    raw = cur.fetchall()
    # S'il n'y a aucune réservation en cours
    if not raw:
        print("--------------------")
        print("Aucune réservation en cours")
        print("--------------------")
    # Sinon, afficher les réservations en cours
    else:
        # Récupérer le nombre de réservations en cours
        nombre_pret = len(raw)
        # Boucle tant que l'utilisateur ne choisit pas de quitter (choix 0)
        while user_choix != "0":
            print("--------------------------------------------------------")
            print("Le document a été réservé par :", raw[i_pret][0])
            print("Le code du document est : ", raw[i_pret][1])
            print("Le début de la réservation est en date du : ", raw[i_pret][2])
            print("--------------------------------------------------------")
            print("1 Pour passer à la réservation suivante")
            print("0 Pour quitter")
            user_choix = input("Sélectionner un choix : ")
            # Si l'utilisateur choisit de passer à la réservation suivante
            if user_choix == "1":
                # Si l'index de la réservation affichée est inférieur au nombre de réservations en cours, l'incrémenter
                if i_pret + 1 < nombre_pret:
                    i_pret += 1
                # Sinon, remettre l'index à 0 pour recommencer à afficher les réservations à partir du début
                elif i_pret + 1 == nombre_pret:
                    i_pret = 0


def supprimer_reservation(cur):
    # Demander le login de l'adhérent
    print("Entrée le login de l'adhérent")
    login_adh = input("Login : ")
    # Vérifier que le login saisi correspond à un compte adhérent existant
    sql = "select login from compte_adherent where login='%s';" % login_adh
    cur.execute(sql)
    raw = cur.fetchone()
    # Si le login saisi ne correspond à aucun compte adhérent, demander à l'utilisateur de réessayer
    while not raw:
        print("Login invalide, veuillez réessayer !")
        login_adh = input("Login : ")
        sql = "select login from compte_adherent where login='%s';" % login_adh
        cur.execute(sql)
        raw = cur.fetchone()
    # Demander le code de la ressource réservée
    print("Entrée le code la ressource prêté")
    code_ressource = int(input("Code ressource : "))
    # Supprimer la réservation correspondante de la base de données
    sql = "delete from reservation where adherent='%s' and ressource='%s';" % (login_adh, code_ressource)
    cur.execute(sql)
    print("Réservation supprimée")


def analyser(cur):
    # Initialiser la variable de choix de l'utilisateur à une valeur non valide
    user_choix1 = -1

    # Boucle tant que l'utilisateur ne choisit pas de quitter (choix 0)
    while user_choix1 != "0":
        print("--------------------------------------------------------")
        print("1 Documents les plus empruntés")
        print("0 Quitter")
        user_choix1 = input("Sélectionner un choix : ")

        # Si l'utilisateur ne choisit pas de quitter, exécuter l'option choisie
        if user_choix1 != "0":
            if user_choix1 == "1":
                # Afficher les documents les plus empruntés
                document_favori(cur)
            else:
                # Si l'utilisateur saisi une option non valide, afficher un message d'erreur
                print("Veuillez effectuer une saisie valide !")


def document_favori(cur):
    # Déclarer la variable "document_favori" en tant que liste vide
    doc_favori = []
    nb_favori = 0
    # Récupérer les identifiants d'exemplaire les plus empruntés, ainsi que le nombre d'emprunts correspondant
    sql = "SELECT exemplaire, COUNT(exemplaire) AS nb FROM Pret GROUP BY exemplaire ORDER BY nb DESC;"
    cur.execute(sql)
    raw = cur.fetchall()
    # Si au moins 3 documents ont été empruntés, prendre les 3 documents les plus empruntés
    # Sinon, prendre le nombre de documents empruntés le plus proche de 3.
    if len(raw) >= 3:
        nb_favori = 3
    elif len(raw) == 2:
        nb_favori = 2
    elif len(raw) == 1:
        nb_favori = 1
    # Pour chaque document emprunté, récupérer ses informations et l'ajouter à la liste "document_favori"
    for i in range(nb_favori):
        code_document = raw[i]
        sql = "SELECT * FROM ressource JOIN exemplaire ON ressource.code = exemplaire.ressource WHERE exemplaire.id_exemplaire = '%s';" % (
            code_document[0])
        cur.execute(sql)
        document = cur.fetchall()
        doc_favori.append(document)
    # Si aucun document n'a été emprunté, afficher un message
    if not doc_favori:
        print("--------------------")
        print("Aucun document n'est favori")
        print("--------------------")
    # Affichage des favoris
    print("_" * 100)
    for i in range(nb_favori):
        print("Le code du document est :", doc_favori[i][0][0])
        print("Le titre du document est : ", doc_favori[i][0][1])
        print("La date du document est : ", doc_favori[i][0][2])
        print("Le nom de l'éditeur est : ", doc_favori[i][0][3])
        print("Le genre du document est :", doc_favori[i][0][4])
        print("Le code de classification du document est ", doc_favori[i][0][5])
        print("_" * 100)


def document_recommande(cur, login):
    # Initialisation des listes
    doc_recommande = []
    document_emprunte = []
    affichage = False
    # Récupération des informations des documents empruntés par l'utilisateur
    sql = "SELECT ressource.code, ressource.date_apparition, ressource.editeur, ressource.genre FROM ressource JOIN pret ON pret.code_ressource = ressource.code WHERE adherent='%s';" % login
    cur.execute(sql)
    raw = cur.fetchall()
    # Ajout des codes des documents empruntés à la liste document_emprunte
    for i in range(len(raw)):
        code = raw[i][0]
        document_emprunte.append(code)
        # Récupération des informations sur les documents recommandés
        editeur = raw[i][2]
        genre = raw[i][3]
        sql = "SELECT code FROM ressource  WHERE NOT (code='%s') AND (editeur = '%s' OR genre = '%s');" % (code, editeur, genre)
        cur.execute(sql)
        recommandation = cur.fetchall()
        # Ajout des codes de documents recommandés à la liste document_recommande
        if recommandation:
            for j in range(len(recommandation)):
                doc_recommande.append(recommandation[j][0])
        # Suppression des doublons dans la liste document_recommande
        doc_recommande = list(set(doc_recommande))
    # Affichage des recommandations
    print("_" * 100)
    for i in doc_recommande:
        # Récupération des informations sur les documents recommandés
        sql = "SELECT * FROM ressource JOIN exemplaire ON ressource.code = exemplaire.ressource WHERE ressource.code = '%s';" % i
        cur.execute(sql)
        document = cur.fetchone()
        # Si le document n'a pas déjà été emprunté, on l'affiche
        if document[0] not in document_emprunte:
            affichage = True
            # Affichage des recommandations
            print("Le code du document est : ", document[0])
            print("Le titre du document est : ", document[1])
            print("La date du document est : ", document[2])
            print("Le nom de l'éditeur est : ", document[3])
            print("Le genre du document est : ", document[4])
            print("Le code de classification du document est : ", document[5])
            print("_" * 100)
    # Si aucun document n'a été affiché, on affiche un message indiquant qu'il n'y a pas de recommandation
    if not affichage:
        print("Aucune recommandation pour vous")
