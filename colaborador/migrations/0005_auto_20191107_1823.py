# Generated by Django 2.2.6 on 2019-11-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0004_auto_20191107_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
