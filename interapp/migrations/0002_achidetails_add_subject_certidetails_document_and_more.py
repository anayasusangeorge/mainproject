# Generated by Django 4.1.1 on 2023-04-30 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='achidetails',
            fields=[
                ('achi_id', models.AutoField(primary_key=True, serialize=False)),
                ('cann_id', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('achiname', models.CharField(max_length=100, null=True)),
                ('achiinfo', models.CharField(max_length=100, null=True)),
                ('achidate', models.DateField()),
            ],
        ),
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
        migrations.CreateModel(
            name='certidetails',
            fields=[
                ('cer_id', models.AutoField(primary_key=True, serialize=False)),
                ('cann_id', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('certiname', models.CharField(max_length=100, null=True)),
                ('cerinfo', models.CharField(max_length=100, null=True)),
                ('certidate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeks', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='interdetails',
            fields=[
                ('in_id', models.AutoField(primary_key=True, serialize=False)),
                ('cann_id', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('interns', models.CharField(max_length=100, null=True)),
                ('internname', models.CharField(max_length=100, null=True)),
                ('interndate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='projectdetails',
            fields=[
                ('pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('cann_id', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('proname', models.CharField(max_length=100, null=True)),
                ('prodetails', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField(blank=True)),
                ('price', models.IntegerField(default='')),
                ('outcomes', models.TextField()),
                ('assignment', models.TextField(default='')),
                ('Certificate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('promo', models.FileField(default='', upload_to='video')),
                ('course_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.duration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=500)),
                ('videos', models.FileField(upload_to='video')),
                ('time_duration', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('course_week', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='interapp.duration')),
            ],
        ),
        migrations.CreateModel(
            name='resumme',
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
                ('dob', models.DateField(default=0)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.document')),
            ],
        ),
        migrations.CreateModel(
            name='requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=0, max_length=70)),
                ('score', models.CharField(default=0, max_length=10)),
                ('time', models.CharField(default=0, max_length=10)),
                ('correct', models.CharField(default=0, max_length=10)),
                ('wrong', models.CharField(default=0, max_length=10)),
                ('percent', models.CharField(default=0, max_length=10)),
                ('total', models.CharField(default=0, max_length=10, verbose_name='total questions')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('course_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.duration')),
            ],
            options={
                'verbose_name_plural': 'Quiz - Result',
            },
        ),
        migrations.CreateModel(
            name='QuizProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('course_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.duration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quizdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_minutes', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('course_week', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='interapp.duration')),
            ],
        ),
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('course_week', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='interapp.duration')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('enrolled_at', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enrolled', models.BooleanField(default=False)),
                ('enroll_date', models.DateTimeField(auto_now_add=True)),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interapp.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackStudents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interapp.user_course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
