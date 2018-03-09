# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-02 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.CharField(default='-1', max_length=50, primary_key=True, serialize=False)),
                ('match', models.CharField(default='-1', max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('correct', models.BooleanField(default=False)),
                ('feedback_content', models.CharField(default='-1', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('hint_id', models.CharField(default='-1', max_length=50, primary_key=True, serialize=False)),
                ('hint_level', models.IntegerField(default=0)),
                ('hint_content', models.CharField(default='-1', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.CharField(default='-1', max_length=30, primary_key=True, serialize=False)),
                ('module_name', models.CharField(default='-1', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problem_id', models.CharField(default='-1', max_length=30, primary_key=True, serialize=False)),
                ('problem_name', models.CharField(default='-1', max_length=50)),
                ('description', models.CharField(default='-1', max_length=50)),
                ('learning_objectives', models.CharField(default='-1', max_length=5000)),
                ('purpose', models.CharField(default='-1', max_length=50)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSM.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.CharField(default='-1', max_length=30, primary_key=True, serialize=False)),
                ('section_name', models.CharField(default='-1', max_length=100)),
                ('parent_type', models.CharField(default='-1', max_length=10)),
                ('parent_id', models.CharField(default='-1', max_length=30)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSM.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('sequence_id', models.CharField(default='-1', max_length=30, primary_key=True, serialize=False)),
                ('sequence_name', models.CharField(default='-1', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('step_id', models.CharField(default='-1', max_length=50, primary_key=True, serialize=False)),
                ('step_name', models.CharField(default='-1', max_length=100)),
                ('step_content', models.CharField(default='-1', max_length=5000)),
                ('step_type', models.CharField(default='-1', max_length=5)),
                ('value', models.CharField(default='-1', max_length=5000)),
                ('kc1', models.CharField(default='-1', max_length=1000)),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DSM.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(default='-1', max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_id', models.CharField(default='-1', max_length=30, primary_key=True, serialize=False)),
                ('unit_name', models.CharField(default='-1', max_length=50)),
                ('sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSM.Sequence')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSM.Unit'),
        ),
        migrations.AddField(
            model_name='hint',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSM.Step'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSM.Step'),
        ),
    ]
