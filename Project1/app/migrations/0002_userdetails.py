# Generated by Django 2.2.6 on 2019-12-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('pw', models.CharField(max_length=20)),
            ],
        ),
    ]
