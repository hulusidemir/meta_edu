# Generated by Django 4.0.2 on 2022-03-01 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_category_category_description_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category', verbose_name='Kategori'),
        ),
    ]