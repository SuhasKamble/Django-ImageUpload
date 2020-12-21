# Generated by Django 3.0.7 on 2020-12-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myImage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]