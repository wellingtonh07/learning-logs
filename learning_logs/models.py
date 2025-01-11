from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_name  # Retorna o nome do tópico ao invés do objeto

class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    texto = models.TextField()
    data_adicionada = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto[:50]  # Mostra os primeiros 50 caracteres do texto da entrada
