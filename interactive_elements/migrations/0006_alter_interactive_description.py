# Generated by Django 5.0.6 on 2024-06-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive_elements', '0005_remove_multiplechoice_interactive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactive',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
