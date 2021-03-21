from django.views.generic.edit import DeleteView, UpdateView
from artikel.forms import ArtikelForm
from django.db.models.expressions import OrderBy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Artikel
from .forms import ArtikelForm
from django.urls import reverse_lazy
# Create your views here.
#membuatc class kalau bisa satu class utk satu fungsi

class ArtikelUpdateView(UpdateView):
    form_class = ArtikelForm
    model = Artikel
    template_name = 'artikel/artikel_update.html'

class ArtikelDeleteView(DeleteView):
    model = Artikel
    template_name = 'artikel/artikel_delete_confirmation.html'
    success_url = reverse_lazy('artikel:manage')

class ArtikelManageView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_manage.html'
    context_object_name = 'artikel_manage'

class ArtikelCreateView(CreateView):
    form_class = ArtikelForm
    template_name = 'artikel/artikel_create.html'

class ArtikelPerKategori():
    model = Artikel
    def get_latest_artikel_each_kategori(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset = []
        for kategori in kategori_list:
            artikel = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(artikel)
        # print(queryset)
        return queryset

class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_kategori_list.html"
    ordering = ['-published']
    context_object_name = 'artikel_list'
    paginate_by = 3
    def get_queryset(self):
        # print(self.kwargs)
        self.queryset = self.model.objects.filter(kategori__iexact = self.kwargs['kategori'])
        # print(artikel_per_kategori)
        return super().get_queryset()
    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori__iexact = self.kwargs['kategori'])
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list' #mengubah nama variabel object_list menjadi artikel_list
    ordering = ['-published'] #dari yang paling terakhir dibuat
    paginate_by = 3
    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel/artikel_detail.html'
    context_object_name = 'artikel'
    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        artikel_serupa = self.model.objects.filter(kategori = self.object.kategori).exclude(id = self.object.id)
        self.kwargs.update({'artikel_serupa':artikel_serupa})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)
