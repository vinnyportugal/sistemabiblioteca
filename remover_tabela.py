import sqlite3
import mysql.connector

conn = mysql.connector.connect(
    user = '******',
    password = '****',
    database = '******'
)

def remover_tabela():

    conn = mysql.connector.connect(
        user='******',
        password='******',
        database='*********'
    )
    cursor = conn.cursor()

    linha = cursor.execute(''' DELETE FROM livraria ''')


    delete = cursor.fetchall()
    conn.commit()

    for linha in delete:
        print(linha)

    while True:
        try:
            print(' tabela excluida com sucesso!!')
            break

        except mysql.connector.Error as err:
            print(' ERRO AO CONECTAR AO BANCO DE DADOS!!')
            return




    cursor.close()
    conn.close()


remover_tabela()