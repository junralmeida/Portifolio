
from tkinter import Tk,Label, Entry, Button, END

def cadastroAluno():
    nome = nome_entrada.get()
    idade = idade_entrada.get()
    nota = nota_entrada.get()

    print(f"Nome:{nome}")
    print(f"Idade:{idade}")
    print(f"Nota:{nota}")

    nome_entrada.delete(0,END)
    idade_entrada.delete(0,END)
    nota_entrada.delete(0,END)



widget= ("ariel, 15")

janela = Tk()
janela.title("Cadastro de aluno")

titulo = Label ( text="Cadastrado de aluno", font= widget)
titulo.pack()

nome_label = Label(janela, text="Nome")
nome_label.pack(padx=10, pady=5)
nome_entrada = Entry (janela, fg="black", bg="white")
nome_entrada.pack(padx=10, pady=5)


idade_label = Label(janela, text="Idade")
idade_label.pack(padx=10, pady=5)
idade_entrada = Entry (janela,fg="black", bg="white")
idade_entrada.pack()

nota_label = Label(janela,text="Nota")
nota_label.pack(padx=10, pady=5)
nota_entrada = Entry (janela,fg="black", bg="white")
nota_entrada.pack()


enviar = Button(text="Cadastrar" , command= cadastroAluno,fg="white", bg="black")
enviar.pack()


janela.mainloop()
