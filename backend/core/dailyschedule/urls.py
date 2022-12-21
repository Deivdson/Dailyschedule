from django.urls import include, re_path, path
from .views import *
from rest_framework import routers
from . import views

app_name = 'cronogramas'

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'cronogramas', views.CronogramaViewSet, basename='Cronograma')
router.register(r'tarefas', views.TarefaViewSet)
router.register(r'alunos', views.AlunoViewSet, basename='Aluno')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]