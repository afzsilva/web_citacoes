from django.urls import path
from .views import buscar_dados, obter_dados_post

urlpatterns = [
    path('',buscar_dados,name='buscar_dados_url'),
    path('obter_dados_post/',obter_dados_post,name='obter_dados_post'),

]