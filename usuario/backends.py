from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class UsuarioBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            usuario = Usuario.objects.get(email=email)
            print("Usuario! ", usuario.email)

            print("Senha passada: ", password)
            print("Senha do usuário: ", usuario.password)
            if usuario.check_password(password):
                print("Senha valida do usuario")
                return usuario
        except Usuario.DoesNotExist:
            return None
