# Generated by Django 5.1.4 on 2025-01-10 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_rename_data_adicionada_topic_date_added_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='topic_name',
        ),
    ]