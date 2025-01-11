from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':  # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:  # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():  # Se o formulário for válido
            new_user = form.save()  # Cria o novo usuário
            # Autentica o usuário
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # Faz login do usuário e o redireciona para a página inicial
            if authenticated_user is not None:
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)