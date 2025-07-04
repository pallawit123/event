# Generated by Django 5.1.4 on 2025-06-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_historical_significance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='image1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='historical_essence',
            new_name='instructions',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='date',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='tutorial_video_url',
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
