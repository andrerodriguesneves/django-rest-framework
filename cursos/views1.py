from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"id": serializer.data['id'], "curso": serializer.data['titulo'] }, status=status.HTTP_201_CREATED)

class AvalicaoAPIView(APIView):
    """
        Api de availações da Geek - Desenvolvida por André Rodrigues
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serialiazer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serialiazer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


