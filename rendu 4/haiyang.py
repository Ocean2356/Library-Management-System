def recherche():
    print("Entrer les mots clés à rechercher pour chaque champ")
    t = input("Titre")
    d = input("Date d'apparition")
    e = input("Éditeur")
    g = input("Genre")
    c = input("Contributeur")
    sql = """SELECT * from ressource
            WHERE titre LIKE '%%s%'
                AND date_apparition LIKE '%%s%'
                AND editeur LIKE '%%s%'
                AND genre LIKE '%%s%'
                """
