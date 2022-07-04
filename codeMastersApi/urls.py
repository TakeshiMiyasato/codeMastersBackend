from django.urls import include, path
from rest_framework import routers

from codeMastersApi.views import DocumentacionHechoPorJugadorViewSet, ProgramacionViewSet, \
    ProgramacionHechoPorJugadorViewSet
from codeMastersApi.views.documentacion_viewset import DocumentacionViewSet
from codeMastersApi.views.puntosPorJugador_viewset import PuntosPorJugadorViewSet
from codeMastersApi.views.register_viewset import RegisterAPI

router = routers.DefaultRouter()
router.register(r'documentaciones', DocumentacionViewSet)
router.register(r'puntosPorJugadores', PuntosPorJugadorViewSet)
router.register(r'documentacionHechaPorJugador', DocumentacionHechoPorJugadorViewSet)
router.register(r'programaciones', ProgramacionViewSet)
router.register(r'programacionHechaPorJugador', ProgramacionHechoPorJugadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
]