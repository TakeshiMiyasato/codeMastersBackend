from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from codeMastersApi.models.puntosPorJugador import PuntosPorJugador


class PuntosPorJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntosPorJugador
        fields = ('id', 'idJugador', 'puntajeAnual', 'puntajeTotal', 'nivel', 'user_name')


class PuntosPorJugadorViewSet(viewsets.ModelViewSet):
    serializer_class = PuntosPorJugadorSerializer
    queryset = PuntosPorJugador.objects.all()

    @action(detail=False, methods=['POST'], url_path='leveling', name='leveling')
    def lvling(self, request):
        contar_puntos = lambda n: n + 10
        contar_lvl = lambda i: i + 1
        objeto_asqueroso = PuntosPorJugador.objects.get(idJugador=request.data['idJugador'])

        puntosAnuales = objeto_asqueroso.puntajeAnual + int(request.data['puntosAAsignar'])
        puntosTotales = objeto_asqueroso.puntajeTotal + int(request.data['puntosAAsignar'])
        print(puntosTotales)

        lvl = 0
        x = 0
        while x < puntosTotales:
            x = contar_puntos(x)
            lvl = contar_lvl(lvl)
            print(x)

        example = PuntosPorJugador.objects.get(idJugador=request.data['idJugador'])
        example.puntajeTotal = puntosTotales
        example.puntajeAnual = puntosAnuales
        example.nivel = lvl
        example.save()
        return Response({'puntajeAnual': puntosAnuales, 'puntajeTotal': puntosTotales, 'nivel': lvl})

    @action(detail=False, methods=['POST'], url_path='resetPuntosAnuales', name='resetPuntosAnuales')
    def reset_puntos_anuales(self, request):
        todos = PuntosPorJugador.objects.all()

        for punto in todos:
            punto.puntajeAnual = 0

        PuntosPorJugador.objects.bulk_update(todos, fields=['puntajeAnual'])
        return Response('Todos los puntajes anuales eliminados')

    @action(detail=False, methods=['POST'], url_path='getCompetitive', name='getCompetitive')
    def get_competitive(self, request):
        tabla = PuntosPorJugador.objects.all().order_by('-puntajeAnual')
        serializer = PuntosPorJugadorSerializer(tabla, many=True)
        return Response(serializer.data)