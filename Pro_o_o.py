class Aluno(): 
    
    
    def __init__(self, nome, nota=0, media=6): 
        self.nome = nome
        self.notas = nota
        self.media = media


    def nota (self, notas):
        self.notas = notas

    def media_final(self, media=6):
        if self.notas > media :
            print (self.nome ,"Aprovado")

        else:
            print(self.nome, "Reprovado" )

aluno1 = Aluno ("Junior")
aluno1.nota(8)
aluno1.media_final(6)

aluno2 = Aluno ("Amarildo")
aluno2.nota(5)
aluno2.media_final(6)

    