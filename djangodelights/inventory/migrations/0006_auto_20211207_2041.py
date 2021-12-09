# Generated by Django 3.2.9 on 2021-12-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20211207_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('kilograms', 'kilogram'), ('counts', 'count'), ('grams', 'gram'), ('ounce', 'ounce'), ('pounds', 'pound')], default='grams', max_length=10),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]