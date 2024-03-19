import psycopg2
import psycopg2.extras

def connect_postgres(lista):
    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="teste",
            user="teste",
            password="teste",
            port=5432
        )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute('DROP TABLE IF EXISTS carros')

        create_script = '''CREATE TABLE IF NOT EXISTS carros (
                                id      SERIAL PRIMARY KEY, 
                                marca   VARCHAR(30) NOT NULL,
                                modelo  VARCHAR(30),
                                description VARCHAR(90))'''
        cur.execute(create_script)

        for carro in lista:
            cur.execute('INSERT INTO carros (marca, modelo, description) VALUES (%s, %s, %s)', (carro["Marca"], carro["Modelo"], carro["Versão"]))

        cur.execute('SELECT * FROM carros')
        for record in cur.fetchall():
            print(record['marca'], record['modelo'])

        conn.commit()

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None: 
            conn.close()

