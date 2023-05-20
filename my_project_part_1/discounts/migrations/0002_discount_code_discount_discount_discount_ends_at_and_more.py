# Generated by Django 4.0.1 on 2023-05-17 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='code',
            field=models.CharField(default='skypro', max_length=20),
        ),
        migrations.AddField(
            model_name='discount',
            name='discount',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='ends_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='starts_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discounts.tour'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
