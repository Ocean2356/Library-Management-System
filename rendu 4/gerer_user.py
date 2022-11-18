import psycopg2

def gerer_user(cur,login):
print("1 pour sanctionner un adhérant")
print("2 pour blacklister un adhérant")
print("3 pour mettre a jour la dette de l'adhérant")
user_choix1 = input("Selectionnez un choix")


if user_choix1==1:
    user_choix2=input("1 pour suspendre temporairement un adhérant")
    if user_choix2==1:
      dureesanction = input("Inserez la durée de la sanction ")
      sql = "insert into sanction values ('%s');" % (dureesanction)
      cur.execute(sql)    
    else:
        exit()


elif user_choix1==2:
    print("Etes vous sur de vouloir blacklister l'adherant ?")
    user_choix3=input("Selectionnez 1 pour Oui et 0 pour Non")
    if user_choix3==1:
        sql="insert into sanction values (1);"
        cur.execute(sql)
    else:
        exit()


elif user_choix1==3:
    sql="select sommeDue from sanction;"
    cur.execute(sql)
    montant = cur.fetchall()
    print("La somme due est de ", montant)
    user_choix4=input("Selectionnez 1 pour mettre à jour le montant de la somme de et 0 pour quitter") 
    if user_choix4==1:  
        montantDette = input("Inserez la durée de la sanction ")
        sql="insert into sanction values ('%s');" % (montantDette)
        cur.execute(sql)
    else:
        exit()
