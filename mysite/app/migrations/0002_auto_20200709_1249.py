# Generated by Django 3.0.6 on 2020-07-09 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='full_description',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProgramCats'),
        ),
    ]