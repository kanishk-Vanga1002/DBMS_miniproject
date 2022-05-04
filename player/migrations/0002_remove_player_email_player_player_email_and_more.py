# Generated by Django 4.0.1 on 2022-03-29 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='email',
        ),
        migrations.AddField(
            model_name='player',
            name='player_email',
            field=models.EmailField(default='email@email.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]