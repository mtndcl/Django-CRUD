# Generated by Django 2.2.3 on 2019-07-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
