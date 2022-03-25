from helpers import print_error
from s1_add_tastetest import add_tastetest
from s2_list_most_active_test_users import list_most_active_taste_users
from s3_list_best_value_coffees import list_best_value_coffees
from s4_search_by_description import search_by_description
from s5_type_country_search import search_by_type_or_country


actions = [
    ("Registrere en smakstest", add_tastetest),
    (
        "Skriv ut liste over brukere som har utført flest smakstester",
        list_most_active_taste_users,
    ),
    (
        "Skriv ut liste over kaffene som gir mest for pengene",
        list_best_value_coffees,
    ),
    ("Søk etter kaffer basert på beskrivelse", search_by_description),
    ("Finn kaffer basert på typer og land", search_by_type_or_country),
    ("Avslutt programmet", exit),
]

if __name__ == "__main__":
    print(
        """
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________              ██╗░░██╗░█████╗░███████╗███████╗███████╗██████╗░██████╗░   
    <_____________> ___         ██║░██╔╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗ 
    |             |/ _ \        █████═╝░███████║█████╗░░█████╗░░█████╗░░██║░░██║██████╦╝
    |               | | |       ██╔═██╗░██╔══██║██╔══╝░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗
    |               |_| |       ██║░╚██╗██║░░██║██║░░░░░██║░░░░░███████╗██████╔╝██████╦╝
 ___|             |\___/        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═════╝░╚═════╝░
/    \___________/    \    
\_____________________/    
    """
    )
    while True:
        print("Hva vil du gjøre?")
        for i, option in enumerate(actions):
            action_name, action_fn = option
            print(f"{i+1}) {action_name}")
        try:
            i = int(input("> ")) - 1
            print("\n")
            actions[i][1]()
            print("\n")
        except (ValueError, IndexError):
            print_error(
                f"Vennligst velg en handling ved å skrive inn et tall fra 1 til {len(actions)}."
            )
        except EOFError:
            exit()
