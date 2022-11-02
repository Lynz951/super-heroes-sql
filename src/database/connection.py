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

def add_super(name, about_me, biography):
    query = """
    INSERT INTO heroes (name, about_me, biography)
    VALUES (%s, %s, %s);
    """
    execute_query(query, (name, about_me, biography))

def delete_super(name):
    query = """
    DELETE FROM heroes (name, about_me, biography)
    WHERE (name = %s);
    """
    execute_query(query)

name = input("What is your name? ")
print("Hello " + name + "! Welcome to The Super Secret Facebook for Superheroes!!")

option_1 = input("Would you like to see a list of our superheroes? yes or no? ")
if (option_1 == "yes"):
    select_all()
if (option_1 == "no"):
    print("Ok whatever")

option_2 = input("Would you like to join The Super Secret Facebook for Superheroes? yes or no? ")
if (option_2 == "yes"):
     print("Awesome!")
     name = input("What is your super secret super name? ")
     about_me = input("Can you tell us one super thing about yourself? ")
     biography = input("Last thing, a short biography about you and your life as a super would really help other supers get to know you... ")
     add_super(name, about_me, biography)
    
if (option_2 == "no"):
    print("Well nevermind then...")

option_3 = input("Would you like to move on or delete your account? move on or delete? ")
if (option_3 == "move on"):
    print("okay!")

if (option_3 == "delete"):
    print("okok hold on")
    name = input("What is your super name? ")
    delete_super(name)
    print("Ok, all set!")