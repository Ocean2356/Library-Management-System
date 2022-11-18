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




HOST = "tuxa.sme.utc"
USER = "nf18a061"
PASSWORD = "l0ixTFxR"
DATABASE = "dbnf18a061"
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))





cur = conn.cursor

# recherche(cur)

visualiser(cur, 'jingfang.yuan')

conn.close