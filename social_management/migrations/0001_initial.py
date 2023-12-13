# Generated by Django 5.0 on 2023-12-13 08:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video', models.FileField(blank=True, null=True, upload_to='uploads/post_video/')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active like'), ('INACTIVE', 'Inactive like')], default='INACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_account', to='user_management.account')),
                ('likedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to='user_management.account')),
            ],
            options={
                'db_table': 'like',
            },
        ),
    ]
