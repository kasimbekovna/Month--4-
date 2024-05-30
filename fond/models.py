from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class SocFondUser(User):
    GENDER = (("Male", "Male"), ("Female", "Female"))
    title = models.CharField(
        max_length=50,
        verbose_name="Заявление о назначении пенсии по возрасту",
        null=True,
    )
    text = models.TextField(
        verbose_name="Заполните для назначения пенсии основные документы", null=True
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Загрузите паспорт и трудовую книжку",
        blank=True,
        null=True,
    )
    pin_number = models.CharField(
        max_length=16,
        verbose_name="ИИН -Индивидуальный идентификационный номер",
        null=True,
    )
    phone_number = models.CharField(max_length=14, default="+996", null=True)
    age = models.PositiveIntegerField(
        default=58, validators=[MinValueValidator(5), MaxValueValidator(99)], null=True
    )
    gender = models.CharField(max_length=100, choices=GENDER, null=True)
    stag = models.PositiveIntegerField(default=0, null=True)
    fond = models.CharField(
        max_length=100,
        default="Ваш возраст слишком мал для назначении пенсии",
        null=True,
    )


@receiver(post_save, sender=SocFondUser)
def set_pension(sender, instance, created, **kwargs):
    if created:
        print("заявление о назначении пенсии")
        age = instance.age
        stag = instance.stag
        gender = instance.gender

        if age >= 60 and stag >= 40:
            instance.fond = "пенсия по стажу для мужчин"
        elif age >= 55 and stag >= 35:
            instance.fond = "пенсия по стажу для женщин"
        elif age >= 63 and stag >= 25:
            instance.fond = "пенсия по старости для мужчин"
        elif age >= 58 and stag >= 20:
            instance.fond = "пенсия по старости для женщин"
        else:
            instance.fond = "Вам пенсия не назначена, так как у вас не хватает стаж"
        instance.save()
