import psycopg2

HOST = "tuxa.sme.utc"
USER = "nf18a074"
PASSWORD = "ulk6EDbE"
DATABASE = "dbnf18a074"
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    
cur = conn.cursor()







""" sql  = "select * from sanction;" 
cur.execute(sql) 
raw = cur.fetchall()
#print(raw)
for line in raw:
    print("%s %s %s\n"%(line[0], line[1], line[2])) """

cur.execute(open("../rendu3/create.sql", "r").read())
cur.execute(open("../rendu3/insert.sql", "r").read())
conn.commit()

conn.close()
