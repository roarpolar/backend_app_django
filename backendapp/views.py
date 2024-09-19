from rest_framework import viewsets
from rest_framework import permissions
from collaborators.models import Colaborador
from .serializers import ColaboradorSerializer

# ViewSet para o modelo Colaborador
class ColaboradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar colaboradores.
    """
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    permission_classes = [permissions.IsAuthenticated]


