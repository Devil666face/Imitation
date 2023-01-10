# Generated by Django 4.1.5 on 2023-01-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imitation', '0010_alter_incident_legal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='legal',
            field=models.CharField(choices=[('YES', 'Легетимно'), ('NONE', 'Не определено'), ('NO', 'Нарушение')], default='NO', max_length=5, verbose_name='Легетимность'),
        ),
    ]
