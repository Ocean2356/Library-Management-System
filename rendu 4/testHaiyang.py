import psycopg2
# from haiyang import recherche
# from menu import connexion

def visualiser(cur, login):
    sql = """SELECT *
            FROM pret
            WHERE adherent = '%s'
            ;""" % (login)
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)
        
def recherche(cur):
    print("Entrer les mots clés à rechercher pour chaque champ")
    t = input("Titre : ")
#    d = input("Date d'apparition : ")
    e = input("Éditeur : ")
    g = input("Genre : ")
    c = input("Contributeur : ")
    sql = """SELECT r.*
            FROM ressource r
            WHERE r.titre LIKE '%"""+t+"""%'
                AND r.editeur LIKE '%"""+e+"""%'
                AND r.genre LIKE '%"""+g+"""%'
                ;"""
    cur.execute(sql)
    raw = cur.fetchall()
    for ligne in raw:
        print(ligne)
        code = ligne[0]
        
        sql = """select * 
                from livre l 
                where l.ressource = '%d'
                ;""" % code
        cur.execute(sql)
        spe = cur.fetchone()
        if spe is not None:
            print(spe)
            code = spe[3]
            sql = """select c.*
                    from auteur p, contributeur c
                    where p.livre = %d
                        and p.id_contributeur = c.id_contributeur
                    ;""" % code
            cur.execute(sql)
            contributeur = cur.fetchall()
            for auteur in contributeur:
                print(auteur)
            
        else:
            sql = """select * 
                    from film l 
                    where l.ressource = '%d'
                    ;""" % code
            cur.execute(sql)
            spe = cur.fetchone()
            if spe is not None:
                print(spe)
                
            else:
                sql = """select * 
                        from oeuvre_musicale l 
                        where l.ressource = '%d'
                        ;""" % code
                cur.execute(sql)
                spe = cur.fetchone()
        
                print(spe)
        
        print()
#                AND date_apparition LIKE '%"""+d+"""%'



HOST = "tuxa.sme.utc"
USER = "nf18a074"
PASSWORD = "ulk6EDbE"
DATABASE = "dbnf18a074"
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))





cur = conn.cursor()

# recherche(cur)

# visualiser(cur, 'jingfang.yuan')
recherche(cur)

conn.close()