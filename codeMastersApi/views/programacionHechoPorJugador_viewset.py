from django.contrib.auth.models import User
from knox.models import User
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from codeMastersApi.models import ProgramacionHechoPorJugador


class ProgramacionHechoPorJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionHechoPorJugador
        fields = ('id', 'codigo', 'revisado', 'correcto', 'programacionId', 'usuarioId', 'user_name')


class ProgramacionHechoPorJugadorViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramacionHechoPorJugadorSerializer
    queryset = ProgramacionHechoPorJugador.objects.all()

    @action(detail=False, methods=['POST'], url_path='getVistoBueno', name='getVistoBueno')
    def get_visto_bueno(self, request):
        validacion = ProgramacionHechoPorJugador.objects.filter(usuarioId=request.data['idJugador'],
                                                                programacionId=request.data['idProgramacion']).last()
        serializer = ProgramacionHechoPorJugadorSerializer(validacion, many=False)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'], url_path='getSubidasByEjercicio', name='getSubidasByEjercicio')
    def get_subidas_by_ejercicio(self, request):
        ejerciciosSubidosByEjercicio = ProgramacionHechoPorJugador.objects.filter(
            programacionId=request.data['idProgramacion'], revisado=False)
        serializer =ProgramacionHechoPorJugadorSerializer(ejerciciosSubidosByEjercicio, many=True)
        return Response(serializer.data)
