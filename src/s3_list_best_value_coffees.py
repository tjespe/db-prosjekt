from helpers import connect, print_column_titles


def list_best_value_coffees():
    con = connect()
    cur = con.cursor()
    print_column_titles(
        "Brennerinavn", "Kaffenavn", "Kilopris i NOK", "Gjennomsnittscore", width=20
    )
    for row in cur.execute(
        """
        SELECT Brenneri.Navn, Kaffe.Navn, KiloprisNOK, AVG(Score)
        FROM Kaffesmaking
        INNER JOIN Kaffe ON Kaffe.ID = KaffeID
        INNER JOIN Brenneri ON Brenneri.ID = BrenneriID
        GROUP BY KaffeID
        ORDER BY AVG(Score)/KiloprisNOK DESC; 
        """
    ):
        print("\t".join(str(value).ljust(20) for value in row))
    con.close()
