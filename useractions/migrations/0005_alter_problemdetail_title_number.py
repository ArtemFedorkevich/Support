# Generated by Django 3.2.7 on 2021-10-01 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useractions', '0004_alter_problemdetail_title_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemdetail',
            name='title_number',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='useractions.problem'),
        ),
    ]
