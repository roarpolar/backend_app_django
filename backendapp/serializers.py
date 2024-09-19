from rest_framework import serializers
from collaborators.models import Colaborador

# Serializer para o modelo Colaborador
class ColaboradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['url', 'nome', 'cpf', 'data_nasc', 'imagem', 'senha', 'add_matricula']

