from rest_framework import generics
from web_app.models import ScrapData
from .serializer.serializers import ScrapDataserializer


# novo
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Create your views here.
class ScrappsView(generics.ListAPIView):
    queryset = ScrapData.objects.all()
    serializer_class = ScrapDataserializer


@api_view()
def all_scrapps(request):
    dados = ScrapData.objects.all()
    dados_serializer =ScrapDataserializer(dados,many=True)
    return Response(dados_serializer.data)

