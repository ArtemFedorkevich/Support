# Generated by Django 3.2.7 on 2021-10-04 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useractions', '0007_problemdetail_title_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(default='In progress', max_length=100),
        ),
        migrations.AlterField(
            model_name='problemdetail',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_status', to='useractions.problem'),
        ),
    ]
