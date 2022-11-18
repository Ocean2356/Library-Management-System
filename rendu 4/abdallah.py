import psycopg2


def gerer_user(cur, login):


    print("1 pour sanctionner un adhérent\n")
    print("2 pour blacklister un adhérent\n")
    print("3 pour mettre a jour la dette de l'adhérent\n")
    choix1 = input("Selectionnez un choix : \n")
    if choix1 == "1":
        choix2 = input("Selectionnez 1 pour suspendre temporairement un adhérent\n")
        if choix2 == "1":
            dureesanction = input("Inserez la durée de la sanction \n")
            sql = "insert into sanction values ('%s');" % (dureesanction)
            cur.execute(sql)
        else:
            exit()
    elif choix1 == "2":
        print("Etes vous sur de vouloir blacklister l'adherent ? \n")
        choix3 = input("Selectionnez 1 pour Oui et 0 pour Non\n")
        if choix3 == "1":
            numeroadherent=input("Inserez le numero de l'adherent que vous souhaitez blackliste : \n")
            sql = "update compte_adherent set blackliste='1' where numeroCarte='%s';" % (numeroadherent)
            cur.execute(sql)
        else:
            exit()

    elif choix1 == "3":
        sql = "select sommeDu from compte_adherent;"
        cur.execute(sql)
        montant = cur.fetchall()
        print("La somme due est de ", montant)
        choix4 = input("Selectionnez 1 pour mettre à jour le montant de la somme de et 0 pour quitter\n")
        if choix4 == "1":
            montantDette = input("Inserez la durée de la sanction \n")
            sql = "insert into sanction values ('%s');" % (montantDette)
            cur.execute(sql)
        else:
            exit()
