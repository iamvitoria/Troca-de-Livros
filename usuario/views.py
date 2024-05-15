from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login

def login_usuario(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Credenciais inválidas. Por favor, digite novamente."
    return render(request, 'usuario_login.html', {'error_message': error_message})

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('senha')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('usuario_login')
    else:
        form = UsuarioForm()
    return render(request, 'usuario_registro.html', {'form': form})
