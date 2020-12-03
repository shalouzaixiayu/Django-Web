# Generated by Django 3.1.3 on 2020-12-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_property', models.CharField(max_length=64)),
                ('people_to_tag', models.ManyToManyField(related_name='ptt', to='cst.people')),
            ],
        ),
    ]
