from django.contrib import admin
from animes.models import Anime

class Animes(admin.ModelAdmin):
    list_display = ('id', 'nome_anime', 'estado')
    list_display_links = ('id', 'nome_anime', 'estado')
    search_fields = ('nome_anime', )
    list_filter = ('estado', )

admin.site.register(Anime, Animes)