# Generated by Django 5.0.6 on 2024-06-13 16:42


import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_userprogress_options_and_more'),
        
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
    