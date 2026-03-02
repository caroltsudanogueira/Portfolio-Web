
from django.shortcuts import render, redirect
from .models import Projeto, Contato

def index(request):
    if request.method == 'POST':
        # Pega os dados do formulário que você criou no HTML
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        # Salva no Neon
        Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
        
        # Redireciona para a mesma página para limpar o formulário
        return redirect('index')

    projetos = Projeto.objects.all()
    return render(request, 'portfolio/index.html', {'projetos': projetos})