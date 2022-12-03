# Generated by Django 4.1.2 on 2022-10-22 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0003_favoriteitem_user_alter_favoriteitem_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteitem',
            name='user',
        ),
        migrations.AlterField(
            model_name='favoriteitem',
            name='favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorites.favorite'),
        ),
    ]
