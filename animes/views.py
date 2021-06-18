from django.shortcuts import redirect, render, get_object_or_404
from animes.models import Anime
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        animes = Anime.objects.filter(usuario=request.user.id)
        dados = {
            'animes': animes
        }
        return render(request, 'index.html', dados)
    else:
        return redirect('login')
        
def anime(request, anime_id):
    if request.user.is_authenticated:
        animes = get_object_or_404(Anime, pk=anime_id)
        dados = {
            'anime': animes
        }
        return render(request, 'animes/anime.html', dados)
    else:
        return redirect('login')

def adiciona_anime(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome_anime = request.POST['nome_anime']
            n_eps = request.POST['n_eps']
            eps_assistidos = request.POST['eps_assistidos']
            estado = request.POST['estado']
            nota = request.POST['nota']
            user = get_object_or_404(User, pk=request.user.id)
            if eps_assistidos > n_eps:
                messages.error(request, 'O número de episódios assistidos não pode ser maior que a quantidade de epsódios que contém o anime.')
                return redirect('adiciona_anime')
            if 'foto-anime' in request.FILES:
                foto = request.FILES['foto-anime']
                anime = Anime.objects.create(usuario=user, nome_anime=nome_anime, n_eps=n_eps, eps_assistidos=eps_assistidos, estado=estado, nota=nota, foto=foto)
            else:
                anime = Anime.objects.create(usuario=user, nome_anime=nome_anime, n_eps=n_eps, eps_assistidos=eps_assistidos, estado=estado, nota=nota)
            anime.save()
            return redirect('index')
        return render(request, 'animes/adiciona_anime.html')
    else:
        return redirect('login')

def edita_anime(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    dados = {
        'anime': anime
    }
    return render(request, 'animes/edita_anime.html', dados)

def atualiza_anime(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            anime_id = request.POST['anime_id']
            anime = Anime.objects.get(pk=anime_id)
            anime.nome_anime = request.POST['nome_anime']
            anime.n_eps = request.POST['n-eps']
            anime.eps_assistidos = request.POST['eps-assistidos']
            anime.estado = request.POST['estado']
            anime.nota = request.POST['nota']
            if 'foto_anime' in request.FILES:
                anime.foto = request.FILES['foto_anime']
            anime.save()
            return redirect('index')
    

def deleta_anime(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    anime.delete()
    return redirect('index')
