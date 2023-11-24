from django.urls import path
from prova_pratica_1.views import *
app_name="prova_pratica_1"
urlpatterns=[
        path('', index_pp1, name='index_pp1'),
        path('view_a/maxmin', maxmin, name='maxmin'),
        path('view_b/media', media, name='media'),
        path('view_b/voti', voti, name='voti'),
        
]