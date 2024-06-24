from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import Livro
from .forms import LivroForm
from django.db.models import Q


class IndexView(ListView):
    model = Livro
    template_name = 'home.html'
    context_object_name = 'livros'

class LivroListView(ListView):
    model = Livro
    template_name = 'listar_livro.html'
    context_object_name = 'livros'
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'adicionar_livro.html'
    success_url = reverse_lazy('listar_livro')

class DetalhesLivroView(DetailView):
    model = Livro
    template_name = 'detalhes_livro.html'
    context_object_name = 'livro'

class BuscaLivroView(ListView):
    model = Livro
    template_name = 'busca_livro.html'
    context_object_name = 'livros'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Livro.objects.all()

        if query:
            object_list = Livro.objects.filter(
                Q(titulo__icontains=query) | Q(autor__icontains=query)
            )

        return object_list

