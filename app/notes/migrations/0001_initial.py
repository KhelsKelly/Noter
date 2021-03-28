# Generated by Django 3.1.6 on 2021-03-28 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Write everything down here so as not to forget it later!', verbose_name='content')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date of creation')),
                ('image', models.ImageField(blank=True, help_text='Attach here any image you want if need be', null=True, upload_to='notes/', verbose_name='image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]