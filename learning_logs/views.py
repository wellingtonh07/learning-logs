from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

# Página inicial
def index(request):
    return render(request, 'learning_logs/index.html')

# Exibe todos os tópicos
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# Exibe um tópico específico e suas entradas
@login_required
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)  # Recupera o tópico com o id passado na URL
    entries = topic.entry_set.all()  # Ou qualquer lógica para pegar as entradas relacionadas ao tópico
    return render(request, 'learning_logs/topic.html', {'topic': topic, 'entries': entries})

# Criação de um novo tópico
@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user  # Associa o tópico ao usuário logado
            new_topic.save()
            return redirect('learning_logs:topics')
    else:
        form = TopicForm()

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# Adiciona uma nova entrada a um tópico
@login_required
def new_entry(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            # Criação de uma nova entrada associando o usuário logado
            entry = form.save(commit=False)
            entry.topic = topic
            entry.owner = request.user  # Associa a entrada ao usuário logado
            entry.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        form = EntryForm()

    return render(request, 'learning_logs/new_entry.html', {'form': form, 'topic': topic})

# Edita uma entrada existente
@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic  # A entrada tem uma relação com o tópico

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        form = EntryForm(instance=entry)

    return render(request, 'learning_logs/edit_entry.html', {'form': form, 'topic': topic, 'entry': entry})

@login_required
def delete_topic(request, topic_id):
    # Pega o tópico com o ID fornecido ou retorna 404 se não encontrado
    topic = get_object_or_404(Topic, id=topic_id)

    # Verifica se o usuário logado é o dono do tópico (caso seja necessário)
    if topic.owner != request.user:
        return redirect('learning_logs:topics')  # Redireciona se não for o dono

    # Exclui o tópico
    topic.delete()

    # Redireciona para a página de tópicos após excluir
    return redirect('learning_logs:topics')


@login_required
def delete_entry(request, topic_id, entry_id):
    topic = get_object_or_404(Topic, id=topic_id)
    entry = get_object_or_404(Entry, id=entry_id)

    # Verifica se o usuário logado é o dono da entrada
    if entry.owner != request.user:
        return redirect('learning_logs:topic', topic_id=topic.id)  # Redireciona se não for o dono

    # Exclui a entrada
    entry.delete()

    # Redireciona para a página do tópico após excluir
    return redirect('learning_logs:topic', topic_id=topic.id)