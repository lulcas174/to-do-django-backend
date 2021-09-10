from core.models import listaTarefas
from rest_framework import serializers

class tarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = listaTarefas
        fields = ['id','title','description']