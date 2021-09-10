from django.shortcuts import render
from core.models import listaTarefas
from rest_framework import viewsets
from core.serializers import tarefasSerializer
# Create your views here.

class tarefasViewSet(viewsets.ModelViewSet):
    queryset = listaTarefas.objects.all()
    serializer_class = tarefasSerializer
