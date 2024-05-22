# Generated by Django 5.0.6 on 2024-05-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Напишите название книги')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Загрузите фото')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('audio', models.FileField(blank=True, upload_to='audio/', verbose_name='Загрузите аудио файл')),
                ('category_books', models.CharField(choices=[('новинки', 'новинки'), ('популярное', 'популярное'), ('подборки', 'подборки'), ('Другое', 'Другое')], max_length=100, verbose_name='Выберите категорию')),
                ('audio_time', models.PositiveIntegerField(verbose_name='Укажите длительность аудио книг')),
                ('author', models.CharField(max_length=100, null=True, verbose_name='Укажите автора')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'книги',
                'verbose_name_plural': 'список книг',
            },
        ),
    ]
