# Generated by Django 3.2.9 on 2021-11-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='img',
            field=models.ImageField(default='aabbccdd', upload_to='downloads'),
            preserve_default=False,
        ),
    ]
