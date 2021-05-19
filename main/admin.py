from django.contrib import admin
from .models import Tutorial

from django.db import models


# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_title",
              "tutorial_content"]

admin.site.register(Tutorial)