from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class MyBook(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=2222)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_book = models.ForeignKey(MyBook, on_delete=models.CASCADE,
                                     related_name='review_book')
    stars = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review_book}-{self.stars}'





class Books(models.Model):
    CATEGORY_BOOKS = (
        ('новинки', 'новинки'),
        ('популярное','популярное'),
        ('подборки','подборки'),
        ('Другое', 'Другое'),
    )

    title = models.CharField(max_length=50, verbose_name='Напишите название книги', null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото', blank=True, null=True)
    description = models.TextField(verbose_name='Краткое описание')
    audio = models.FileField(upload_to='audio/', verbose_name='Загрузите аудио файл', blank=True,null=True)
    category_books = models.CharField(max_length=50, choices=CATEGORY_BOOKS, verbose_name='Выберите категорию', null=True)

    audio_time = models.PositiveIntegerField(verbose_name='Укажите длительность аудио книг', null=True)
    author = models.CharField(max_length=100, verbose_name='Укажите автора', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.created_at}'


    class Meta:
        verbose_name = 'книги'
        verbose_name_plural = 'список книг'
