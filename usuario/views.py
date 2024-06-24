from django.shortcuts import render, redirect
from .backends import UsuarioBackend
from .forms import UsuarioForm
from django.contrib.auth import login

from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Usuario

from django.shortcuts import get_object_or_404, redirect
from .models import Usuario

def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


class ProfileView(TemplateView):
    template_name = "perfil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


def login_usuario(request):
    error_message = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = UsuarioBackend().authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            error_message = "Credenciais inválidas. Por favor, digite novamente."
    return render(request, "usuario_login.html", {"error_message": error_message})


def registro_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("senha")
            user = UsuarioBackend().authenticate(
                request, email=email, password=password
            )
            if user is not None:
                login(request, user)
                return redirect("usuario_login")
    else:
        form = UsuarioForm()
    return render(request, "usuario_registro.html", {"form": form})
