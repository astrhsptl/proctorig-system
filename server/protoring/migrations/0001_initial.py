# Generated by Django 4.1.3 on 2022-11-24 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField(max_length=4096)),
                ('photo', models.ImageField(null=True, upload_to='exam_tasks/%Y/%m/%d')),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExamRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to='records/%Y/%m/%d')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protoring.exam')),
            ],
        ),
    ]
