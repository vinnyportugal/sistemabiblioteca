import mysql.connector
import sqlite3
from sqlalchemy import create_engine, MetaData, Table



def contagem():
   conexao = mysql.connector.connect(
      user='*****',
      password='*****',
      database='*****'
   )
   cursor = conexao.cursor()
   cursor.execute(''' SELECT * FROM livraria''')
   conn = len(cursor.fetchall())

   print('numero de livros ->>> {}'.format(conn))


contagem()













