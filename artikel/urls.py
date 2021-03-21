from django.urls import path
from .views import ArtikelKategoriListView, ArtikelListView, ArtikelDetailView, ArtikelCreateView, ArtikelManageView, ArtikelDeleteView, ArtikelUpdateView

urlpatterns = [
    path('manage/update/<pk>', ArtikelUpdateView.as_view(), name='update'),
    path('manage/delete/<pk>', ArtikelDeleteView.as_view(), name='delete'),
    path('manage/', ArtikelManageView.as_view(), name='manage'),
    path('tambah/', ArtikelCreateView.as_view(), name='create'),
    path('<page>', ArtikelListView.as_view(), name='list'),
    path('detail/<slug>', ArtikelDetailView.as_view(), name='detail'),
    path('kategori/<kategori>/<page>', ArtikelKategoriListView.as_view(), name = 'category'),
]