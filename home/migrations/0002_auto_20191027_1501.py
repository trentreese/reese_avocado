# Generated by Django 2.2.6 on 2019-10-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=150)),
                ('secret', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
