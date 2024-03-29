# Generated by Django 5.0.1 on 2024-02-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, null=True, verbose_name='File name')),
                ('file', models.FileField(unique=True, upload_to='files/', verbose_name='File')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Date/time loading')),
                ('processed', models.BooleanField(default=False, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'ordering': ('-uploaded_at',),
            },
        ),
    ]
