from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']  # Defina os campos que serão usados no formulário

    topic_name = forms.CharField(max_length=200, label='Nome do Tópico', widget=forms.TextInput(attrs={
        'class': 'form-control',  # Aplica o estilo do Bootstrap
        'placeholder': 'Digite o nome do tópico aqui...'
    }))

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['texto']  # Certifique-se de que o campo é 'texto' no modelo Entry

    # Definindo o rótulo personalizado para o campo
    labels = {
        'texto': ''  # Rótulo vazio para o campo 'texto'
    }

    # Definindo o widget para o campo 'texto', para que ele seja exibido como uma área de texto maior
    widgets = {
        'texto': forms.Textarea(attrs={'cols': 80, 'rows': 10})  # Adiciona a área de texto com 80 colunas e 10 linhas
    }
