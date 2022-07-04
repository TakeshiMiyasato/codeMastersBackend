from rest_framework import serializers, viewsets

from codeMastersApi.models.documentacion import Documentacion


class DocumentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentacion
        fields = '__all__'


class DocumentacionViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentacionSerializer
    queryset = Documentacion.objects.all()
