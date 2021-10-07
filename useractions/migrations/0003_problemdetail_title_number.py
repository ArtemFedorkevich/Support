# Generated by Django 3.2.7 on 2021-10-01 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useractions', '0002_remove_problemdetail_title_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemdetail',
            name='title_number',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='question', to='useractions.problem'),
            preserve_default=False,
        ),
    ]