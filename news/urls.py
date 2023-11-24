from django.urls import path
from .views import home,indexNews,queryBase, giornalistaDetailView,articoloDetailView, lista_articoli_giornalista

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    path("indexNews",indexNews, name="indexNews"),
    path("giornalisti/<int:pk>",giornalistaDetailView, name="giornalista_detail"),
    path("articoli/<int:pk>",articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>",lista_articoli_giornalista, name="lista_articoli"),
    path("lista_articoli",lista_articoli_giornalista, name="lista_articoli"),
    path("query_base",queryBase, name="query_base"),

    ]