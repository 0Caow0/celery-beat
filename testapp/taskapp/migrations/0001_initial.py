# Generated by Django 2.0.7 on 2018-11-16 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBTestDataBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.DecimalField(decimal_places=0, default=1, max_digits=10)),
                ('type', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DBTestTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=256)),
                ('value', models.DecimalField(decimal_places=0, default=1, max_digits=10)),
                ('data_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_info', to='taskapp.DBTestDataBase')),
            ],
        ),
    ]