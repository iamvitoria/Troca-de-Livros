from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import EmailValidator
import requests


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, idade, cpf, senha, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, idade=idade, cpf=cpf, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, idade, cpf, senha, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, nome, idade, cpf, senha, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(
        "Membro da equipe",
        default=False,
        help_text="Designa se este usuário pode acessar a área de administração.",
    )

    nome = models.CharField("Nome", max_length=250)
    idade = models.PositiveIntegerField("Idade")
    email = models.EmailField("E-mail", unique=True, validators=[EmailValidator()])
    cpf = models.CharField("CPF", max_length=14, unique=True)
    cep = models.CharField("CEP", max_length=9)
    endereco = models.CharField("Endereço", max_length=255, blank=True)
    numero = models.CharField("Número", max_length=10, blank=True)
    complemento = models.CharField("Complemento", max_length=255, blank=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    estado = models.CharField("Estado", max_length=100, blank=True)
    foto_perfil = models.ImageField(
        upload_to="perfil_fotos/",
        blank=True,
        null=True,
        default="media/profile-pic.jpg",
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome", "idade", "cpf"]

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.cep and not self.endereco:
            self._preencher_endereco()
        super().save(*args, **kwargs)

    def _preencher_endereco(self):
        cep_url = f"http://viacep.com.br/ws/{self.cep}/json/"
        response = requests.get(cep_url)
        if response.status_code == 200:
            data = response.json()
            self.endereco = data.get("logradouro", "")
            self.bairro = data.get("bairro", "")
            self.cidade = data.get("localidade", "")
            self.estado = data.get("uf", "")

    groups = models.ManyToManyField(
        "auth.Group", verbose_name="groups", blank=True, related_name="auth_user_groups"
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="auth_user_permissions",
    )
