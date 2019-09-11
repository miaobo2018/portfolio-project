# Generated by Django 2.2.5 on 2019-09-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_data', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
