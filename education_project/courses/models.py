import datetime
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.tag_name


class Course(models.Model):
    course_name = models.CharField(max_length=200, unique=False, blank=False, verbose_name="Kurs Adı")
    course_category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING, verbose_name="Kategori")
    course_tags = models.ManyToManyField(Tag, blank=True, null=True)
    course_description = models.TextField(blank=True, verbose_name="Kurs Açıklaması")
    course_date = models.DateTimeField(default=datetime.datetime.now, verbose_name="Yayımlanma Tarihi")
    course_image = models.ImageField(upload_to='images/%Y/%m/%d/', default='no_image.png', blank=True,
                                     verbose_name="Resim Dosyası", height_field=None)
    is_course_available = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name
