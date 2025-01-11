from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    # Exibe todos os tópicos
    path('topics/', views.topics, name='topics'),
    
    # Exibe um tópico específico com o id
    path('topic/<int:topic_id>/', views.topic, name='topic'), 
    
    # Criação de um novo tópico
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Adicionar uma nova entrada para um tópico
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    # Editar uma entrada existente
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Deleta um tópico existente
    path('topics/delete/<int:topic_id>/', views.delete_topic, name='delete_topic'),

    # Deleta uma entrada existente
    path('topic/<int:topic_id>/delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
