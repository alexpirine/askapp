# Generated by Django 2.2.5 on 2019-11-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0016_populate_domain'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='thread',
            name='link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='thread_type',
            field=models.CharField(choices=[('DD', 'Discussion'), ('LL', 'Link'), ('YT', 'Youtube video')], default='LL', max_length=2, null=True),
        ),
    ]