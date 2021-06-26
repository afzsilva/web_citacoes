from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .models import ScrapData

# Create your views here.


def buscar_dados(request):
    dados_banco = ScrapData.objects.all()
    return render(request,"index.html",{'dados_banco':dados_banco})

def obter_dados_post(request):
    site_url = request.POST['urlscrap']
    print("URL >>> ",site_url)
    obter_dados_scrap(site_url)
    #return HttpResponse(site_url)
    return redirect('buscar_dados_url')


def obter_dados_scrap(url):

    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    autores = bsObj.select('small[itemprop="author"]')
    citacoes = bsObj.select('span[itemprop="text"]')

    citacoes_tratadas = []
    for tag in citacoes:
        citacoes_tratadas.append(tag.string)

    autores_tratados = []
    for tag in autores:
        autores_tratados.append(tag.string)

    salvar(autores_tratados, citacoes_tratadas)


"""
def mostrar_conteudo(lista):
    for item in lista:
        print(item.text)
"""

def salvar_um_scrapping(autor,citacao):

    dados = ScrapData(nome_autor=autor, citacao=citacao)
    dados.save()

def salvar(lista_autores, lista_citacao):
    limpar_dados()
    for a,c in zip(lista_autores, lista_citacao):
        salvar_um_scrapping(a,c)
    print("Salvo com sucesso")


def limpar_dados():
    dados_banco = ScrapData.objects.all()
    dados_banco.delete()



