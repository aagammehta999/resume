# Generated by Django 4.0.3 on 2022-03-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='certificates/'),
        ),
    ]
