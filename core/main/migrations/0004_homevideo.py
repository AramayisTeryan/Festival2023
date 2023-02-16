# Generated by Django 4.1.4 on 2023-02-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='media', verbose_name='HomeVideo video')),
            ],
            options={
                'verbose_name': 'HomeVideo',
                'verbose_name_plural': 'HomeVideos',
            },
        ),
    ]
