# Generated by Django 4.1.1 on 2023-04-30 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interapp', '0003_delete_add_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_subject',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='img/')),
                ('description', models.TextField(default='')),
                ('desc', models.TextField(blank=True)),
                ('course_week', models.CharField(default='', max_length=20)),
                ('price', models.IntegerField(default='')),
                ('outcomes', models.TextField()),
                ('assignment', models.TextField(default='')),
                ('Certificate', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='achidetails',
        ),
        migrations.DeleteModel(
            name='certidetails',
        ),
        migrations.DeleteModel(
            name='interdetails',
        ),
        migrations.DeleteModel(
            name='projectdetails',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='colcourse',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='colpy',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='plusmarks',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='pluspy',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='schomarks',
        ),
        migrations.RemoveField(
            model_name='resumme',
            name='schopy',
        ),
        migrations.AddField(
            model_name='resumme',
            name='achi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='resumme',
            name='certi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='resumme',
            name='interns',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='resumme',
            name='projects',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resumme',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='resumme',
            name='refe',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]