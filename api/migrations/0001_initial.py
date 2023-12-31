# Generated by Django 4.2.7 on 2023-11-02 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name="To'liq ism")),
                ('organization_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tashkilot nomi')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Telefon raqami')),
                ('amount', models.PositiveIntegerField(verbose_name='Homiylik summasi ')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Ariza sanasi')),
                ('status', models.CharField(choices=[(' Moderation ', 'Moderatsiya'), ('New', 'Yangi'), ('Appoved', 'Tasdiqlangan'), ('Cancelled', 'Bekor qilingan')], default='New', max_length=50, verbose_name='Homiyning holati')),
                ('type', models.CharField(choices=[('legel', 'yuridik'), ('pyhsical', 'jismoniy')], max_length=50, verbose_name='Shahs turi')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name="To'liq ism")),
                ('contract', models.PositiveIntegerField(verbose_name='Kontrakt summasi')),
                ('degree', models.CharField(choices=[('bachelor', 'bakalavor'), ('master', 'magistr')], default='bachelor', max_length=50, verbose_name='Darajasi')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nomi')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Ajratilgan summ')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.sponsor', verbose_name='Sponsr')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.student', verbose_name='Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.university'),
        ),
    ]
