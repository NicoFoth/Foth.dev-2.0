# Generated by Django 4.2 on 2023-07-14 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csgo', '0005_remove_csplayer_elo_csplayerseasonelo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='csplayerseasonelo',
            unique_together={('player', 'season')},
        ),
    ]
