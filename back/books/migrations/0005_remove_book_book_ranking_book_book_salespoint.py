# Generated by Django 4.2.21 on 2025-05-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_book_embedding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_ranking',
        ),
        migrations.AddField(
            model_name='book',
            name='book_salesPoint',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
