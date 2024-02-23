from django.urls import path
from .views import *

app_name = 'news'

urlpatterns = [
    path("homepageNews",home, name="homepageNews"),
    path("indexNews",indexNews, name="indexNews"),
    path("giornalisti/<int:pk>",giornalistaDetailView, name="giornalista_detail"),
    path("articoli/<int:pk>",articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>",lista_articoli_giornalista, name="lista_articoli"),
    path("lista_articoli",lista_articoli_giornalista, name="lista_articoli"),
    path("query_base",queryBase, name="query_base"), 
    path('api/giornalisti/', giornalisti_list_api, name='giornalisti_list_api'),
    path('api/giornalista/<int:pk>/', giornalista_api, name='giornalista_api'),
    path('api/articoli/', articoli_list_api, name='articoli_list_api'),
    path('api/articolo/<int:pk>/', articolo_api, name='articolo_api'),

    ]