# Generated by Django 3.0.7 on 2020-06-28 18:24

from decimal import Decimal
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_allfields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allfields',
            name='binary',
        ),
        migrations.AddField(
            model_name='allfields',
            name='file',
            field=models.FileField(blank=True, help_text='This is how FileFields look like...', null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='char',
            field=models.CharField(default='Some Chars...', help_text='This is how CharFields look like...', max_length=100),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='decimal',
            field=models.DecimalField(decimal_places=4, default=Decimal('10'), help_text='This is how DecimalFields look like...', max_digits=10),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='duration',
            field=models.DurationField(default=1, help_text='This is how DurationFields look like...'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='email',
            field=models.EmailField(default='mrcheese@example.com', help_text='This is how EmailFields look like...', max_length=100),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='file_path',
            field=models.FilePathField(help_text='This is how FilePathFields look like...', path='path/to/django-jazzmin/tests/test_app'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='float',
            field=models.FloatField(default=10.0, help_text='This is how FloatFields look like...'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='generic_ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1', help_text='This is how GenericIPAddressFields look like...'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='identifier',
            field=models.UUIDField(default=uuid.UUID('8dbe8058-b96c-11ea-8304-acde48001122'), help_text='This is how UUIDFields look like...'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='integer',
            field=models.IntegerField(default=10, help_text='This is how IntegerFields look like...'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='slug',
            field=models.SlugField(default='slug', help_text='This is how SlugFields look like...', max_length=100),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='small_integer',
            field=models.SmallIntegerField(default=1, help_text='This is how SmallIntegerFields look like...'),
        ),
        migrations.AlterField(
            model_name='allfields',
            name='text',
            field=models.TextField(default='Some valuable Text...', help_text='This is how TextFields look like...'),
        ),
    ]
