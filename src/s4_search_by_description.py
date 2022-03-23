import sqlite3
from helpers import connect, print_column_titles, print_header


def search_by_description():
    con = connect()
    cur = con.cursor()
    print("Hvilket ord vil du søke på i en kaffebeskrivelse?")
    search_term = input(f"> ")
    print()
    print_column_titles("Brennerinavn", "Kaffenavn", width=20)
    for row in cur.execute(
        """
        SELECT DISTINCT Brenneri.Navn, Kaffe.Navn
        FROM Brenneri
        INNER JOIN Kaffe ON (Brenneri.ID = BrenneriID)
        LEFT JOIN Kaffesmaking ON (Kaffe.ID = KaffeID)
        WHERE Smaksnotater LIKE ? OR Beskrivelse LIKE ?
        """,
        (f"%{search_term}%", f"%{search_term}%"),
    ):
        print("\t".join(str(value).ljust(20) for value in row))
