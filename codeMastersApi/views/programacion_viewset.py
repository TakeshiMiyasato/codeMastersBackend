from rest_framework import serializers, viewsets

from codeMastersApi.models import Programacion


class ProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programacion
        fields = '__all__'


class ProgramacionViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramacionSerializer
    queryset = Programacion.objects.all()
