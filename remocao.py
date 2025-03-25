from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


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

  



remocao()
