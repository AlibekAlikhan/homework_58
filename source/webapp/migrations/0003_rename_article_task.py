# Generated by Django 4.1.6 on 2023-03-03 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_article_create_at_alter_article_update_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Task',
        ),
    ]
