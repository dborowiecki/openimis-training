# Generated by Django 3.2.18 on 2023-03-21 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0013_auto_20211103_1023'),
        ('insuree_deceased', '0003_insureedeceasedmutation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinsureedeceased',
            name='insuree',
            field=models.ForeignKey(blank=True, db_column='InsureeID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='insuree.insuree'),
        ),
        migrations.AlterField(
            model_name='insureedeceased',
            name='insuree',
            field=models.ForeignKey(blank=True, db_column='InsureeID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='insuree.insuree'),
        ),
    ]
