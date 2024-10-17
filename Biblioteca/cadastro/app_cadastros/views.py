from django.shortcuts import render
from .models import Usuario


# Create your views here.

def home(request):
    return render(request,'cadastros/home.html')

#  Salvar os dados da tela para o banco de dados.

def usuarios(request):

   if request.method == 'POST': 
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Retonar os dados para a página de listagem de usuários.
    
    return render(request,'usuarios/usuarios.html', usuarios)



    # Exibir todos os usuários já cadastrados em uma nova página.

usuarios = {
    'usuarios': Usuario.objects.all()
}


