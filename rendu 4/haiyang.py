def recherche(cur):
    print("Entrer les mots clés à rechercher pour chaque champ")
    t = input("Titre : ")
    d = input("Date d'apparition : ")
    e = input("Éditeur : ")
    g = input("Genre : ")
    c = input("Contributeur : ")
    sql = """SELECT r.* 
            FROM ressource r
            WHERE titre LIKE '%"""+t+"""%'
                AND editeur LIKE '%"""+e+"""%'
                AND genre LIKE '%"""+g+"""%'
            ;"""
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)
#                AND date_apparition LIKE '%"""+d+"""%'

def visualiser(cur, login):
    sql = """SELECT *
            FROM pret
            WHERE adherent = '%s'
            ;""" % (login)
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)