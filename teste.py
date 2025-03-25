from tkinter import Tk, messagebox
import sqlite3
from tkinter import ttk
import tkinter as tk
from tkinter import *
import sys
from sqlite3 import dbapi2
import mysql.connector
import pandas as pd

def banco_dados():
    
    while True:
        try:
    
            conexao = mysql.connector.connect(
                host='********',
                user='********',
                password='*****',
                database='***********'
            )
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM livraria')
            cursor.fetchall()
            conexao.commit()
        except TypeError:
            messagebox.showerror('error' , 'algo deu errado!')
            continue
        finally:
            conexao.close
            cursor.close
def validar():
    database = tk.Tk()
    database.title('pesquisa')
    
    dados = banco_dados
    for i, linha in enumerate(dados):
        label = label(database, text=linha )
        label.grid(row=i , column=0 )
                


def verificar_login(event=None):
    # verificacao da tela de usuario e senha
    usuario = Entry_usuario.get()
    senha = Entry_senha.get()
    if usuario == 'vinicius' and senha == 'dev':
        messagebox.showinfo('login' , 'login bem sucedido')
        janela_login.destroy()
        abrir_janela_principal()
    else:
        messagebox.showerror('error' , ' login invalido')
# entrando na tela de cadastro

#def pergunta():
 #    pergunta1 = messagebox.askyesno('pergunta' , ' tem certeza que deseja sair?')
def consultaid():
    consulta1 = tk.Tk()
    consulta1.geometry('190x150')
    Label_font = ('arial' , '30' , 'bold')
    Label_font2 = (' arialblack ', 10)
    consulta1.title(' consulta pelo id')

    label_id = tk.Label(consulta1 , text=' consulta pelo id:', font=Label_font2 )
    label_id.grid(row=0 , column=1 , padx=10 , pady=10)
    label_id = tk.Entry(consulta1)
    label_id.grid(row=1 , column=1 , padx=10 , pady=10)

    label_botaoid = tk.Button(consulta1 , text='pesquisar'  , command=banco_dados , fg='white' , bg='red')
    label_botaoid.grid(row=20 , columnspan=20 , pady=20)

    consulta1.mainloop() 
def consultanome():
    consulta2 = tk.Tk()
    consulta2.geometry('190x150')
    Label_font = ('arial' , '30' , 'bold')
    Label_font2 = (' arialblack ', 10)
    consulta2.title(' consulta pelo nome')

    label_nome = tk.Label(consulta2 , text=' consulta palo nome:' , font=Label_font2)
    label_nome.grid(row=0 , column=1 , padx=10 , pady=10)
    label_nome = tk.Entry(consulta2)
    label_nome.grid(row=1 , column=1 , padx=10 , pady=10)

    label_botaonome = tk.Button(consulta2 , text='pesquisar' , command=banco_dados , fg='white' , bg='red')
    label_botaonome.grid(row=20 , columnspan=20 , pady=20)

    consulta2.mainloop()




def validacao_cadastro():
    try:
        nome = entry_nome.get()
        paginas = entry_paginas.get()
        compra = entry_compra.get()
        conn = dbapi2.connect('meus_livros.db')
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO livraria (nome , paginas , compra) VALUES (? , ? , ?)''', (nome , paginas , compra))
        conn.commit()
        messagebox.showinfo('cadastro' , ' livro  {} com {} paginas e comprado {} foi cadastrado com sucesso!'.format(nome, paginas,compra))
    except sqlite3.DatabaseError as erro:
        messagebox.showerror('erro' , ' produto nao cadastrado ')
        conn.rollback()
    finally:
        conn.close()
def cadastro():
        global entry_nome,entry_paginas,entry_compra

        janela_cadastro = tk.Tk()
        Label_font = ('arial' , '30' , 'bold')
        Label_font2 = (' arialblack ', 10)

        janela_cadastro.title(' tela de cadastro')

        Label_nome = tk.Label(janela_cadastro , text='nome do livro:', font=Label_font2)
        Label_nome.grid(row=0 , column=0 , padx=10 , pady=10)
        entry_nome = tk.Entry(janela_cadastro)
        entry_nome.grid(row=0 , column=1 , padx=10 , pady=10)

        Label_paginas = tk.Label(janela_cadastro, text='numero de paginas:' , font=Label_font2)
        Label_paginas.grid(row=1 , column=0 , padx=10 , pady=10)
        entry_paginas = tk.Entry(janela_cadastro)
        entry_paginas.grid(row=1, column=1, padx=10, pady=10)

        Label_compra = tk.Label(janela_cadastro , text='lugar de compra:' , font=Label_font2)
        Label_compra.grid(row=2 , column=0 , padx=10 , pady=10)
        entry_compra = tk.Entry(janela_cadastro)
        entry_compra.grid(row=2 , column=1 , padx=10 , pady=10)

        botao_cadastro = tk.Button(janela_cadastro , text=' cadastro' , command=validacao_cadastro , fg='white' , bg='red')
        botao_cadastro.grid(row=10, columnspan=20 , pady=20)

        botao_voltar = tk.Button(janela_cadastro , text=' retornar' , command=janela_cadastro.destroy , fg='white' , bg='red')
        botao_voltar.grid(row= 20, columns=60 , pady=20)
                                

        janela_cadastro.mainloop()

def consulta():
            consulta_livros = tk.Tk()
            consulta_livros.geometry('300x300')
            Label_font = ('arial' , '30' , 'bold')
            Label_font2 = (' arialblack ', 10)
            consulta_livros.title(' consulta de livros ')

            Label_todos = Button(consulta_livros , text='consulta todos os livros' , font=Label_font2 , command=banco_dados , fg='white' , bg='red')
            Label_todos.pack(pady=20)

            label_id = Button(consulta_livros , text='consultar livro pelo id' , command=consultaid ,  font=Label_font2 , fg='white' , bg='red')
            label_id.pack(pady=20)

            label_consultanome = Button(consulta_livros , text='consultar livro pelo nome' , command=consultanome , font=Label_font2 , fg='white' , bg='red')
            label_consultanome.pack(pady=20)

            label_retornar = Button(consulta_livros , text='retornar' ,command=consulta_livros.destroy, font=Label_font2 , fg='white' , bg='red')
            label_retornar.pack(pady=10)
            def validacao2():
                while True:
                    pergunta1 = messagebox.askyesno('pergunta' , ' tem certeza que deseja sair?')
                    if pergunta1 == True:
                        return abrir_janela_principal.destroy
                    else:
                        return consulta_livros
                
            consulta_livros.mainloop()

def remocao():
    remocao_id = tk.Tk()
    remocao_id.geometry('280x250')
    Label_font = ('arial' , '30' , 'bold')
    Label_font2 = (' arialblack ', 10)
    remocao_id.title(' remocao ')

    Label_remocaoid = tk.Label(remocao_id , text='qual id do livro:' , font=Label_font2)
    Label_remocaoid.grid(row=0 , column=0 , padx=5 , pady=5)
    entry_remocaoid = tk.Entry(remocao_id)
    entry_remocaoid.grid(row=0 , column=1 , padx=5 , pady=5)

    Label_remocaonome = tk.Label(remocao_id , text='qual o nome do livro:' , font=Label_font2)
    Label_remocaonome.grid(row=1 , column=0 , padx=5 , pady=5)
    entry_remocaonome = tk.Entry(remocao_id)
    entry_remocaonome.grid(row=1 , column=1 , padx=5 , pady=5)

    Label_botaoremocao = tk.Button(remocao_id , text='remocao' , command=validacao , font=Label_font2 , fg='white' , bg='red' )
    Label_botaoremocao.grid(row=10 , columnspan=10  , pady=10)
    
    label_botaovoltar = tk.Button(remocao_id, text="rotornar" , command=remocao_id.destroy , font=Label_font2 , fg='white' , bg='red' )
    label_botaovoltar.grid(row=20 , columnspan=20 , pady=20 )

    remocao_id.mainloop()


def validacao():
   
   resposta = messagebox.askyesno('confirmacao' , ' tem certeza que deseja excluir esse livro?')
   if resposta:
       messagebox.showinfo('livro removido com sucesso')
       outro = messagebox.askyesno(' deseja excluir outro item? ')
       if outro == True:
           messagebox.showinfo(' vamos remover mais livros')
           return remocao
       else:
           return abrir_janela_principal
    
   else:
       messagebox.showerror('error' , ' nao foi possivel excluir o livro')
       return abrir_janela_principal
       
    

def abrir_janela_principal():
    # entarndo na segunda tela 
    janela_principal = tk.Tk()
    janela_principal.geometry('300x300')
    Label_font = ('arial' , '15' , 'bold')
    Label_font2 = (' arialblack ', 10)
    janela_principal.title('janela principal')

    label_titulo2 = tk.Label(janela_principal , text=' qual a funcao desejada:' , font=Label_font2 , fg='blue')
    label_titulo2.pack()

    Label_cadastro = tk.Button(janela_principal , text='cadastro do livro' , font=Label_font2, command= cadastro ,fg='white' , bg='red')
    Label_cadastro.pack(pady=20)

    Label_consulta = tk.Button(janela_principal , text=' consulta de livros' , font= Label_font2, command=consulta, fg='white' , bg='red')
    Label_consulta.pack(pady=20)

    Label_remocao = tk.Button(janela_principal , text='remocao de livros', command=remocao, font= Label_font2, fg= 'white' , bg='red')
    Label_remocao.pack(pady=20)

    Label_sair = tk.Button(janela_principal , text='sair' , command=janela_principal.destroy , font= Label_font2, fg='white' , bg='red' )
    Label_sair.pack(pady=10)  
    
        

    janela_principal.mainloop()


# criando a tela de login

janela_login = tk.Tk()
Label_font = ('arial' , '20' , 'bold')
Label_font3 = ('calibre' , '10' , 'bold')
janela_login.title('login')
janela_login.geometry('300x200')


label_titulo = tk.Label(janela_login , text='DADOS DE USUARIO!' , font= Label_font , fg='blue')
label_titulo.grid(row=0 , columnspan=20 , padx=1)



label_usuario = tk.Label(janela_login, text="Usuário:" , font= Label_font3)
label_usuario.grid(row=1, column=0, padx=20, pady=20)
Entry_usuario = tk.Entry(janela_login)
Entry_usuario.grid(row=1, column=1, padx=20, pady=20)


label_senha = tk.Label(janela_login, text="Senha:" , font= Label_font3)
label_senha.grid(row=2, column=0, padx=20, pady=20)
Entry_senha = tk.Entry(janela_login , show='*')
Entry_senha.grid(row=2,column=1,padx=20,pady=20)


botao_login = tk.Button(janela_login , text='verificar' , command=verificar_login , fg='white' , bg='red')
botao_login.grid(row=15 , columnspan=15, pady=10)


janela_login.bind('<Return>', verificar_login)                  # comando para usuario entrar com a tecla enter


janela_login.mainloop()

# criando tela de cadastro

            
          



   
