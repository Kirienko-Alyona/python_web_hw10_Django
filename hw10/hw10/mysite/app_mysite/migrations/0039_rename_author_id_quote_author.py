# Generated by Django 4.1.7 on 2023-03-27 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0038_rename_author_quote_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='author_id',
            new_name='author',
        ),
    ]