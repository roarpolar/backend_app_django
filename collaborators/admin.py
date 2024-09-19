from django.contrib import admin
from .models import Colaborador

# Configuração do Django Admin para Colaborador
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'cpf', 'data_nasc', 'telefone_contato', 'email', 'funcao', 
        'add_matricula', 'senha', 'observacoes'
    )  # Inclui os novos campos na visualização da lista
    search_fields = ('nome', 'cpf', 'email', 'funcao')  # Adiciona novos campos ao campo de busca
    readonly_fields = ('senha',)  # Torna 'senha' somente leitura para segurança
    fieldsets = (
        (None, {
            'fields': (
                'nome', 'cpf', 'data_nasc', 'imagem', 'telefone_contato', 
                'email', 'funcao', 'add_matricula', 'senha', 'observacoes'
            )
        }),
    )

# Registro dos modelos no Django Admin
admin.site.register(Colaborador, ColaboradorAdmin)


