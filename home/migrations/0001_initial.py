# Generated by Django 2.2.6 on 2019-10-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=191)),
            ],
            options={
                'db_table': 'socialaccount_socialapp',
                'managed': False,
            },
        ),
    ]
