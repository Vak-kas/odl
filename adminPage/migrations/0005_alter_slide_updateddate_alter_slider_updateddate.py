# Generated by Django 5.0.2 on 2024-02-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPage', '0004_rename_slidename_slider_slidername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='updatedDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='업데이트 날짜'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='updatedDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='업데이트 날짜'),
        ),
    ]
