# Generated by Django 4.1.13 on 2025-03-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_question_studentanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='marks_obtained',
            field=models.FloatField(default=0),
        ),
    ]
