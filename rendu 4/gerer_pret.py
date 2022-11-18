def gerer_pret(cur):
    user_choix =-1
    i_pret = 1
    sql="select * from pret"
    cur.execute(sql)
    raw = cur.fetchall()
    nombre_pret = len(raw)
    while user_choix != "0":
        print("--------------------------------------------------------")
        print("Le document à était emprunter par :",raw[i_pret][0])
        print("C'est l'exemplaire numéro : ",raw[i_pret][1])
        print("Le début du prêt est en date du : ",raw[i_pret][2])
        print("La durée du pret est de ",raw[i_pret][3],"jours")
        print('La date de retour est le : ',raw[i_pret][4])
        print("l'état au retour est ",raw[i_pret][5])
        print("--------------------------------------------------------")
        print("1 Pour passer au prêt suivant")
        print("0 Pour quitter")
        user_choix = input("Sélectionner un choix : ")
        if user_choix == "1":
            if i_pret+1 < nombre_pret:
                i_pret += 1
            elif i_pret+1 == nombre_pret:
                i_pret = 0