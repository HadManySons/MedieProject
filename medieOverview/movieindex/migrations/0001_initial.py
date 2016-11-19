# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subpath', models.CharField(db_index=True, max_length=200)),
                ('added', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(default=0)),
                ('metadata', models.TextField(blank=True)),
                ('title', models.CharField(max_length=200)),
                ('length', models.IntegerField(default=0)),
                ('size', models.IntegerField()),
                ('bitrate', models.IntegerField()),
                ('codec', models.CharField(max_length=20)),
                ('fps', models.FloatField()),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MovieFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('folder', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('count', models.IntegerField(default=0)),
                ('movies', models.ManyToManyField(related_name='tags', to='movieindex.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Thumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0)),
                ('image', models.BinaryField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbs', to='movieindex.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieindex.MovieCategory'),
        ),
        migrations.AddField(
            model_name='movie',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieindex.MovieFolder'),
        ),
        migrations.AddField(
            model_name='movie',
            name='main_thumb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie2', to='movieindex.Thumb'),
        ),
    ]
