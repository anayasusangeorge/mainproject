# Generated by Django 4.1.1 on 2023-05-05 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interapp', '0004_add_subject_delete_achidetails_delete_certidetails_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('carobj', models.TextField(blank=True)),
                ('college', models.CharField(blank=True, max_length=100)),
                ('colcourse', models.CharField(blank=True, max_length=100)),
                ('colpy', models.CharField(blank=True, max_length=100)),
                ('plus', models.CharField(blank=True, max_length=100)),
                ('plusmarks', models.CharField(blank=True, max_length=100)),
                ('pluspy', models.CharField(blank=True, max_length=100)),
                ('ten', models.CharField(blank=True, max_length=100)),
                ('schomarks', models.CharField(blank=True, max_length=100)),
                ('schopy', models.CharField(blank=True, max_length=100)),
                ('refe', models.TextField(blank=True, null=True)),
                ('phone', models.BigIntegerField(default=0)),
                ('address', models.TextField(blank=True)),
                ('strength', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('lang', models.TextField(blank=True, null=True)),
                ('hob', models.TextField(blank=True, null=True)),
                ('soci', models.CharField(blank=True, max_length=100)),
                ('coun', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=0, verbose_name='status')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
