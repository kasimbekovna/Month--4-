from django.contrib import admin
from . import models

admin.site.register(models.Books)
admin.site.register(models.MyBook)
admin.site.register(models.Review)


