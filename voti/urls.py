from django.urls import path
from voti.views import *
app_name="voti"
urlpatterns=[
        path('', index_voti, name='index_voti'),
        path('view_a', view_a, name='view_a'),
        path('view_b', view_b, name='view_b'),
        path('view_c', view_c, name='view_c'),
        

]