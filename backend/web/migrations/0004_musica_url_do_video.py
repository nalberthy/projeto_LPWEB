# Generated by Django 2.2.1 on 2019-06-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_genero_musica'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='url_do_video',
            field=models.URLField(null=True),
        ),
    ]
