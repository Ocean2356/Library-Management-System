import psycopg2

HOST = "tuxa.sme.utc"
USER = "nf18a061"
PASSWORD = "l0ixTFxR"
DATABASE = "dbnf18a061"
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
cur = conn.cursor()







sql  = "select code, code_classification from ressource;" 
cur.execute(sql)
raw = cur.fetchall()
#print(raw)
for line in raw:
    print("%s %s\n"%(line[0], line[1]))


conn.close()
