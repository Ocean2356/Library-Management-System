def recherche(cur):
    print("Entrer les mots clés à rechercher pour chaque champ")
    t = input("Titre : ")
    d = input("Date d'apparition : ")
    e = input("Éditeur : ")
    g = input("Genre : ")
    c = input("Contributeur : ")
    sql = """SELECT * 
            FROM ressource
            WHERE titre LIKE '\%%s\%'
                AND date_apparition LIKE '\%%s\%'
                AND editeur LIKE '\%%s\%'
                AND genre LIKE '\%%s\%'
            ;""" % (t, d, e, g)
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)

def visualiser(cur, login):
    sql = """SELECT *
            FROM pret
            WHERE adherent = '%s'
            ;""" % (login)
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)