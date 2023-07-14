# Generated by Django 4.2 on 2023-07-14 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csgo', '0003_csgoplayer_steam_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CSMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('endstate', models.CharField(max_length=5)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csgo.csmap')),
            ],
        ),
        migrations.CreateModel(
            name='CSMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CSPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam_id', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=32)),
                ('elo', models.IntegerField(default=1500)),
            ],
        ),
        migrations.CreateModel(
            name='CSPlayerMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eloChange', models.FloatField(default=0)),
                ('win', models.BooleanField(default=False)),
                ('kills', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('headshotKills', models.IntegerField(default=0)),
                ('mvps', models.IntegerField(default=0)),
                ('enemiesFlashed', models.IntegerField(default=0)),
                ('utilityDamage', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csgo.csmatch')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csgo.csplayer')),
            ],
        ),
        migrations.CreateModel(
            name='CSRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('imageLink', models.CharField(max_length=128)),
                ('minElo', models.IntegerField(default=0)),
                ('maxElo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CSSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='CsgoPlayer',
        ),
        migrations.AddField(
            model_name='csmatch',
            name='mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csgo.csmode'),
        ),
        migrations.AddField(
            model_name='csmatch',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csgo.csseason'),
        ),
    ]
