# Generated by Django 4.1.7 on 2023-05-10 11:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'db_table': 'raca',
            },
        ),
    ]
