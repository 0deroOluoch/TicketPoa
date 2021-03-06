# Generated by Django 2.2.6 on 2020-02-10 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('Event_description', models.TextField(max_length=1500)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=100)),
                ('Event_poster', models.ImageField(upload_to='posters')),
                ('location', models.CharField(max_length=100)),
                ('Mobile_Money_payment', models.BooleanField(default=False)),
                ('Visa_cared_payment', models.BooleanField(default=False)),
                ('Payment_in_installment', models.BooleanField(default=False)),
                ('Private_event', models.BooleanField(default=False)),
                ('Free_Event', models.BooleanField(default=False)),
                ('Featured_Event', models.BooleanField(default=False)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
                'db_table': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('mpesa_code', models.CharField(blank=True, max_length=100)),
                ('time', models.DateTimeField(auto_now=True)),
                ('complete', models.BooleanField(default=False)),
                ('amount', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Ticket')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_name', models.CharField(max_length=255)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_ordered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'verbose_name_plural': 'Event_oders',
                'verbose_name': 'Event_oder',
                'db_table': 'Event_oders',
            },
        ),
    ]
