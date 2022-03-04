# Generated by Django 4.0.2 on 2022-03-03 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.category', verbose_name='Kategori'),
        ),
    ]
