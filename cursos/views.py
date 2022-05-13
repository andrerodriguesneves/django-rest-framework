from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
        Api de cursos da Geek - Desenvolvido por André Rodrigues
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

class AvalicaoAPIView(APIView):
    """
        Api de availações da Geek - Desenvolvida por André Rodrigues
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serialiazer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serialiazer.data)


