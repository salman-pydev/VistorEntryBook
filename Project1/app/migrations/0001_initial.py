# Generated by Django 2.2.6 on 2019-12-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorDeatils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('ContactNo', models.IntegerField()),
                ('Date', models.DateField()),
                ('Address', models.CharField(max_length=500)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=30)),
            ],
        ),
    ]
