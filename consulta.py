import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import messagebox


def consultaid():
    consulta1 = tk.Tk()
    consulta1.geometry('300x200')
    Label_font = ('arial' , '30' , 'bold')
    Label_font2 = (' arialblack ', 10)
    consultaid.title(' consulta pelo id')

    label_id = tk.Label(consulta1 , text=' consulta pelo id:', font=Label_font2 )
    label_id.grid(row=0 , column=1 , padx=10 , pady=10)
    label_id = tk.Entry(consultaid)
    label_id.grid(row=1 , column=1 , padx=10 , pady=10)

    label_botaoid = tk.Button(consulta1 , text='pesquisar' , fg='white' , bg='red')
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

    label_botaonome = tk.Button(consulta2 , text='pesquisar' , fg='white' , bg='red')
    label_botaonome.grid(row=20 , columnspan=20 , pady=20)

    consulta2.mainloop()



def consulta():
    consulta_livros = tk.Tk()
    Label_font = ('arial' , '30' , 'bold')
    Label_font2 = (' arialblack ', 10)
    consulta_livros.title(' consulta de livros ')
    consulta_livros.geometry("500x300")

    Label_todos = Button(consulta_livros , text='consulta todos os livros' , font=Label_font2 , fg='white' , bg='red')
    Label_todos.pack(pady=20)

    label_id = Button(consulta_livros , text='consultar livro pelo id' , command=consultaid , font=Label_font2 , fg='white' , bg='red')
    label_id.pack(pady=20)

    label_consultanome = Button(consulta_livros , text='consultar livro pelo nome' , font=Label_font2 , fg='white' , bg='red')
    label_consultanome.pack(pady=20)

    label_retornar = Button(consulta_livros , text='retornar' , font=Label_font2 , fg='white' , bg='red')
    label_retornar.pack(pady=20)

    consulta_livros.mainloop()


consulta()