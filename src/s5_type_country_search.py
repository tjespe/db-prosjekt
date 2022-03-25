from helpers import connect, safe_get_placeholders, print_column_titles


def search_by_type_or_country():
    con = connect()
    cur = con.cursor()
    print("Er det noen foredlingsmetoder du ikke liker?")
    print(
        "Ulike metoder i databasen: "
        + ",".join(row[0] for row in cur.execute("SELECT Navn FROM Foredlingsmetode"))
    )
    search_term_processing_methods = input(
        f"Skriv navn på metoder, adskilt med komma > "
    ).split(",")
    print("Hvilke land ønsker du hvilke sted er ønsker du kaffer fra?")
    print(
        "Land i databasen: "
        + ",".join(row[0] for row in cur.execute("SELECT DISTINCT Land FROM Gård"))
    )
    search_term_coutries = input(f"Skriv navn på land, adskilt med komma > ").split(",")

    print()
    print_column_titles("Brennerinavn", "Kaffenavn", width=20)

    for row in cur.execute(
        f"""
        SELECT
            Brenneri.Navn,
            Kaffe.Navn
        FROM
            Kaffe
            INNER JOIN Brenneri ON (BrenneriID = Brenneri.ID)
            INNER JOIN Kaffeparti ON Kaffeparti.ID = PartiID
            INNER JOIN Gård ON GårdID = Gård.ID
        WHERE
            ForedlingsmetodeNavn NOT IN ({safe_get_placeholders(search_term_processing_methods)})
            AND Land IN ({safe_get_placeholders(search_term_coutries)})
        """,
        (*search_term_processing_methods, *search_term_coutries),
    ):
        print("\t".join(str(value).ljust(20) for value in row))
