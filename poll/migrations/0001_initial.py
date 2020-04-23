# Generated by Django 3.0.5 on 2020-04-23 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, null=True)),
                ('choice_1', models.CharField(max_length=500, null=True)),
                ('choice_2', models.CharField(max_length=500, null=True)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('description', models.TextField(null=True)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('audio_url', models.URLField(max_length=2000, null=True)),
            ],
            options={
                'db_table': 'results',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=500, null=True)),
                ('case', models.CharField(max_length=20, null=True)),
                ('browser', models.CharField(max_length=100, null=True)),
                ('ip_address', models.CharField(max_length=100, null=True)),
                ('result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Result')),
            ],
            options={
                'db_table': 'responses',
            },
        ),
    ]