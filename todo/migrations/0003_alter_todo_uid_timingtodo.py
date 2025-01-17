# Generated by Django 5.1.4 on 2024-12-15 07:33

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_created_at_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9b177dc0-d4ea-4f2f-9791-bd033b2f52c2'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('9b177dc0-d4ea-4f2f-9791-bd033b2f52c2'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('timing', models.DateField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
