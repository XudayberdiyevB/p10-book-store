# Generated by Django 4.2 on 2023-04-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_tag_book_created_at_book_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='books', to='books.tag'),
        ),
    ]
