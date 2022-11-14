# Generated by Django 4.1.3 on 2022-11-06 19:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_contactinformation_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='BD')),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'ContactUs',
            },
        ),
    ]
