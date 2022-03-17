import sqlite3
from helpers import connect, print_column_titles, print_header


def list_most_active_taste_users():
    con = connect()
    cur = con.cursor()
    print_column_titles("Fornavn", "Etternavn", "Antall unike kaffer smakt på i år")
    for row in cur.execute(
        """
        SELECT Fornavn, Etternavn, COUNT(DISTINCT KaffeID) as antall 
        FROM Bruker JOIN Kaffesmaking on BrukerEpost = Epost 
        WHERE Smaksdato > strftime('%Y', date('now'))
        GROUP BY Bruker.Epost 
        ORDER BY antall DESC; 
        """
    ):
        print("\t".join(str(value).ljust(15) for value in row))
    con.close()
