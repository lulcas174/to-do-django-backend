from django.db import models

# Create your models here.
class listaTarefas(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)