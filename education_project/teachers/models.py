from django.db import models


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_title = models.CharField(max_length=200)
    teacher_description = models.TextField(blank=True)
    teacher_image = models.ImageField(upload_to="teachers/")
    teacher_facebook = models.URLField(max_length=100, blank=True)
    teacher_twitter = models.URLField(max_length=100, blank=True)
    teacher_linkedin = models.URLField(max_length=100, blank=True)
    teacher_github = models.URLField(max_length=100, blank=True)
    