# Generated by Django 5.0.6 on 2024-05-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_mybook_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideosContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("url_vidio", models.URLField()),
            ],
        ),
    ]
