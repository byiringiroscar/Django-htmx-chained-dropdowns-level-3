# Generated by Django 3.2.8 on 2024-04-08 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutors', to='core.module')),
            ],
        ),
    ]
