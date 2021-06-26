from django.urls import path
from .views import ScrappsView, all_scrapps

urlpatterns = [
    # path('citacoes/',ScrappsView,name='citacoes'),
    path('all_citacoes/',all_scrapps,name='all_citacoes'),

]