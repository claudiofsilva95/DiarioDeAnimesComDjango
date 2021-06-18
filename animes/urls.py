from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:anime_id>', views.anime, name='anime'),
    path('adiciona_anime', views.adiciona_anime, name='adiciona_anime'),
    path('edita/<int:anime_id>', views.edita_anime, name='edita_anime'),
    path('deleta/<int:anime_id>', views.deleta_anime, name='deleta_anime'),
    path('atualiza_anime', views.atualiza_anime, name='atualiza_anime')
]