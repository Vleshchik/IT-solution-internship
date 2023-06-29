#идея для добавления в базу данных:
import psycopg2

def save_query(text):
    conn = psycopg2.connect(
        host="your_host",
        port="your_port",
        database="your_database",
        user="your_username",
        password="your_password"
    )

    cursor = conn.cursor()
    query = "INSERT INTO queries (text) VALUES (%s)"
    cursor.execute(query, (text,))
    conn.commit()

    cursor.close()
    conn.close()


text = "текст"
save_query(text)