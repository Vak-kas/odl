# Generated by Django 5.0.2 on 2024-02-22 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPage', '0003_alter_slider_assigntopage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='slideName',
            new_name='sliderName',
        ),
    ]
