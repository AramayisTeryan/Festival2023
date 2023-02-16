# Generated by Django 4.1.4 on 2023-02-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_homevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='About name')),
                ('name1', models.CharField(max_length=50, verbose_name='About name1')),
                ('name2', models.CharField(max_length=50, verbose_name='About name2')),
                ('name3', models.CharField(max_length=50, verbose_name='About name3')),
                ('about', models.TextField(verbose_name='About about')),
                ('about1', models.TextField(verbose_name='About about1')),
                ('about2', models.TextField(verbose_name='About about2')),
                ('about3', models.TextField(verbose_name='About about3')),
                ('img', models.ImageField(upload_to='media', verbose_name='About image')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
    ]
