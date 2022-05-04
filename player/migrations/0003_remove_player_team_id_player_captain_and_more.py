# Generated by Django 4.0.1 on 2022-03-29 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_remove_matchs_team1_id_remove_matchs_team2_id'),
        ('player', '0002_remove_player_email_player_player_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team_id',
        ),
        migrations.AddField(
            model_name='player',
            name='captain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='tournament_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='tournament.tournament'),
            preserve_default=False,
        ),
    ]