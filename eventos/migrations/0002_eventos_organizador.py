# Generated by Django 2.2.6 on 2019-11-07 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0004_auto_20191107_1757'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='organizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colaborador.Colaborador'),
        ),
    ]