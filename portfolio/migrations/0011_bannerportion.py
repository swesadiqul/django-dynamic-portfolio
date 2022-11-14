# Generated by Django 4.1.3 on 2022-11-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPortion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('banner_img', models.ImageField(null=True, upload_to='banner')),
            ],
            options={
                'verbose_name_plural': 'Banner Portion',
            },
        ),
    ]