# Generated by Django 4.0.6 on 2024-04-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_contact_color_contact_initials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subtasks',
            field=models.JSONField(default=list),
        ),
    ]
