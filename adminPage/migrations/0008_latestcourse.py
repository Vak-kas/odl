# Generated by Django 5.0.2 on 2024-02-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPage', '0007_alter_slide_description_alter_slide_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='latest/', verbose_name='이미지')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('price', models.FloatField(verbose_name='가격')),
            ],
        ),
    ]
