import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)
user = (1, "johnny", "1234")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

connection.commit()

connection.close()

def test():
    pass


if __name__ == "__main__":
    test()