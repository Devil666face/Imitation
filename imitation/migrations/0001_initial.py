# Generated by Django 4.1.5 on 2023-01-03 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='Неизвестный тип', max_length=255, verbose_name='Тип инцидента')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='icons/category/%Y/%m/%d/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='Неизвестный инцидент', max_length=255, verbose_name='Название инцидента')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('legal', models.BooleanField(default=True, verbose_name='Легетимность')),
                ('image', models.ImageField(blank=True, null=True, upload_to='icons/example/%Y/%m/%d/', verbose_name='Изображение')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imitation.category', verbose_name='Тип инцидента')),
            ],
            options={
                'verbose_name': 'Инцидент',
                'verbose_name_plural': 'Инциденты',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ExpamleIncident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='Неизвестный инцидент', max_length=255, verbose_name='Название известного инцидента')),
                ('legal', models.BooleanField(default=True, verbose_name='Легетимность')),
                ('image', models.ImageField(blank=True, null=True, upload_to='icons/example/%Y/%m/%d/', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imitation.category', verbose_name='Тип инцидента')),
            ],
            options={
                'verbose_name': 'Известный инцидент',
                'verbose_name_plural': 'Известные инциденты',
                'ordering': ['category'],
            },
        ),
    ]
