# Generated by Django 4.2 on 2023-04-30 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_courseevaluation_total_average_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseevaluation',
            name='total_average',
        ),
        migrations.AlterField(
            model_name='courseevaluation',
            name='comments',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='courseevaluation',
            name='evaluator',
            field=models.CharField(max_length=100),
        ),
    ]
