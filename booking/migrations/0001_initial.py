# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theatre', '0002_auto_20160515_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('payment_type', models.CharField(choices=[('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card'), ('Net Banking', 'Net Banking'), ('Wallet', 'Wallet')], max_length=11)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('paid_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('seat_type', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platinum')], max_length=8)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatre.Show')),
            ],
        ),
        migrations.AddField(
            model_name='bookedseat',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking'),
        ),
        migrations.AddField(
            model_name='bookedseat',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Seat'),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set([('no', 'show')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookedseat',
            unique_together=set([('seat', 'booking')]),
        ),
    ]
