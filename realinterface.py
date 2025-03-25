from tkinter import Tk, messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import *






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




janela_login.mainloop()