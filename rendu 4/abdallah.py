import psycopg2


def gerer_user(cur, login):


    print("1 pour sanctionner un adhérent")
    print("2 pour blacklister un adhérent")
    print("3 pour mettre a jour la dette de l'adhérent")
    choix1 = input("Selectionnez un choix : ")
    if choix1 == "1":
        choix2 = input("Selectionnez 1 pour suspendre temporairement un adhérent")
        if choix2 == "1":
            dureesanction = input("Inserez la durée de la sanction ")
            sql = "insert into sanction values ('%s');" % (dureesanction)
            cur.execute(sql)
        else:
            exit()
    elif choix1 == "2":
        print("Etes vous sur de vouloir blacklister l'adherent ?")
        choix3 = input("Selectionnez 1 pour Oui et 0 pour Non")
        if choix3 == "1":
            sql = "insert into sanction values (1);"
            cur.execute(sql)
        else:
            exit()

    elif choix1 == "3":
        sql = "select sommeDu from compte_adherent;"
        cur.execute(sql)
        montant = cur.fetchall()
        print("La somme due est de ", montant)
        choix4 = input(
            "Selectionnez 1 pour mettre à jour le montant de la somme de et 0 pour quitter")
        if choix4 == "1":
            montantDette = input("Inserez la durée de la sanction ")
            sql = "insert into sanction values ('%s');" % (montantDette)
            cur.execute(sql)
        else:
            exit()
