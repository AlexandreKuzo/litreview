# Generated by Django 3.1.3 on 2020-12-07 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvplit', '0005_auto_20201205_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('headline', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created'],
            },
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.CreateModel(
            name='CriticAutoReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('headline', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('auto_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='critic_auto_reviews', to='mvplit.autoreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='critic_auto_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created'],
            },
        ),
    ]
