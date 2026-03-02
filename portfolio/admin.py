


from django.contrib import admin
from .models import Projeto, Categoria, Contato # Adicione Contato aqui
admin.site.register(Projeto)
admin.site.register(Categoria)
# Uma forma mais profissional de exibir os contatos
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio') # Colunas que aparecem na lista
    search_fields = ('nome', 'email') # Barra de busca por nome ou e-mail
    readonly_fields = ('data_envio',) # Impede que você altere a data manualmente