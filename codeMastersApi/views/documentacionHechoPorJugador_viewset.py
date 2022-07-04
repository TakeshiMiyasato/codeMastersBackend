from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from codeMastersApi.models import DocumentacionHechoPorJugador


class DocumentacionHechoPorJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentacionHechoPorJugador
        fields = '__all__'


class DocumentacionHechoPorJugadorViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentacionHechoPorJugadorSerializer
    queryset = DocumentacionHechoPorJugador.objects.all()

    @action(detail=False, methods=['POST'], url_path='getByUserId', name='getByUserId')
    def get_by_user_id(self, request):
        print(request.data['idUser'])
        hechosPorElJugador = DocumentacionHechoPorJugador.objects.all().\
            filter(usuarioId=request.data['idUser'],
                   documentacionId=request.data['idDocumentacion'])
        serializer = DocumentacionHechoPorJugadorSerializer(hechosPorElJugador, many=True)
        return Response(serializer.data)
