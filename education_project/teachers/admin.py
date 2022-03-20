from django.contrib import admin
from . import models


@admin.register(models.Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('teacher_name',)
