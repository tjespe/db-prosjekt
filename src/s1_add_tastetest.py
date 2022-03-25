from datetime import date
from helpers import connect, print_error


def add_tastetest():
    con = connect()
    cur = con.cursor()
    print("Hva er e-posten din?")
    email = input("> ")
    active_users = set([row[0] for row in cur.execute("SELECT Epost FROM BRUKER")])
    if email not in active_users:
        print(
            "Denne brukeren finnes ikke i databasen. Vil du, A, registrere bruker, eller B, prøve på nytt?"
        )
        answer = input("Skriv A/B > ")
        if answer.upper() == "A":
            first_name = input("Hva er fornavnet ditt?\n> ")
            last_name = input("Hva er etternavnet ditt?\n> ")
            cur.execute(
                "INSERT INTO Bruker (Epost, Fornavn, Etternavn) VALUES (?, ?, ?)",
                (email, first_name, last_name),
            )
        else:
            return add_tastetest()
    print("Hvilken kaffe har du smakt på?")
    valid_pks = set()
    for pk, coffe_name, roastery_name in cur.execute(
        f"""
        SELECT Kaffe.ID, Kaffe.Navn, Brenneri.Navn
        FROM Kaffe
        INNER JOIN Brenneri ON Brenneri.ID = Kaffe.BrenneriID
        """
    ):
        print(f"{pk}) '{coffe_name}' fra '{roastery_name}'")
        valid_pks.add(pk)
    pk = None
    while pk is None:
        try:
            pk = int(input(f"> "))
        except ValueError:
            print_error("Vennligst skriv inn tallet til kaffen du har smakt på.")
        except EOFError:
            return
        if pk is not None and pk not in valid_pks:
            print_error(
                f"Ugyldig valg. Velg en av tallene til kaffene ovenfor {valid_pks}."
            )
            pk = None
    print("Hvilken score vil du gi kaffen på en skala fra 1 til 10?")
    score = None
    while score is None:
        try:
            score = int(input("> "))
        except (ValueError, EOFError):
            print_error("Vennligst skriv et gyldig tall")
        if score < 1 or score > 10:
            print_error("Vennligst skriv et gyldig tall mellom 1 og 10")
            score = None
    print("Hvordan vil du beskrive kaffen?")
    description = input("> ")
    cur.execute(
        """
        INSERT INTO
        Kaffesmaking (
            BrukerEpost,
            KaffeID,
            Smaksdato,
            Score,
            Smaksnotater
        )
        VALUES (?, ?, ?, ?, ? );
        """,
        (email, pk, date.today().isoformat(), score, description),
    )
    con.commit()
    con.close()
    print("✅ Takk for din rating.")
