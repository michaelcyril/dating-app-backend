# Generated by Django 5.0 on 2024-03-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='lat',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='long',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='tags',
            field=models.ManyToManyField(blank=True, to='user_management.tag'),
        ),
    ]
