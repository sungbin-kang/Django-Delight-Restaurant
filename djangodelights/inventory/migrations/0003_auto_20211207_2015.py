# Generated by Django 3.2.9 on 2021-12-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20211207_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('kilograms', 'kilogram'), ('grams', 'gram'), ('ounce', 'ounce'), ('counts', 'count'), ('pounds', 'pound')], default='grams', max_length=10),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='photo',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='media/', width_field=200),
        ),
    ]
