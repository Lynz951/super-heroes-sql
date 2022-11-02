import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")

# ==============================================================


def select_all():
    query = """
        SELECT * FROM heroes
    """
    list_of_heros = execute_query(query).fetchall()
    # print(list_of_heros)
    for record in list_of_heros:
        print(record[1])
# select_all()

# def see_friends():
#     query = """
#         SELECT * FROM relationships r
#         JOIN relationship_types rt ON r.id = rt.id;
#         """
#     relationships_list = execute_query(query).fetchall()
#     print(relationships_list)
#     for record in relationships_list:
#         print(record[1])
# see_friends()

# def see_heroes():
#     query = """
#         SELECT name FROM heroes
#         """
#     list_of_heroes = execute_query(query).fetchall()
#     for record in list_of_heroes:
#         print(record[1])

name = input("What is your name? ")
print("Hello " + name + "! Welcome to The Super Secret Facebook for Superheroes!!")

option_1 = input("Would you like to see a list of our superheroes? yes or no?")
if (option_1 == "yes"):
    select_all()

if (option_1 == "no"):
    print("Ok whatever")