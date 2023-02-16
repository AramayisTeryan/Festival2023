# Generated by Django 4.1.6 on 2023-02-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_ticketheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='TicketMenu name')),
                ('name1', models.CharField(max_length=50, verbose_name='TicketMenu name1')),
                ('name2', models.CharField(max_length=50, verbose_name='TicketMenu name2')),
                ('name3', models.CharField(max_length=50, verbose_name='TicketMenu name3')),
                ('name4', models.CharField(max_length=50, verbose_name='TicketMenu name4')),
                ('name5', models.CharField(max_length=50, verbose_name='TicketMenu name5')),
                ('name6', models.CharField(max_length=50, verbose_name='TicketMenu name6')),
                ('name7', models.CharField(max_length=50, verbose_name='TicketMenu name7')),
            ],
            options={
                'verbose_name': 'TicketMenu',
                'verbose_name_plural': 'TicketMenues',
            },
        ),
    ]