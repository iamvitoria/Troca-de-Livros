from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Livro
from .forms import LivroForm

class IndexView(TemplateView):
    template_name = 'home.html'

class LivroListView(ListView):
    model = Livro
    template_name = 'listar_livro.html'
    context_object_name = 'livros'
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'adicionar_livro.html'
    success_url = reverse_lazy('listar_livro')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
