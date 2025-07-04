# Generated by Django 5.2.1 on 2025-06-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stockmarket_news", "0003_alter_stockmarketnews_authors_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockmarketnews",
            name="banner_image",
            field=models.URLField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="stockmarketnews",
            name="overall_sentiment_score",
            field=models.FloatField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="stockmarketnews",
            name="summary",
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="stockmarketnews",
            name="time_published",
            field=models.DateTimeField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="stockmarketnews",
            name="url",
            field=models.URLField(max_length=10000),
        ),
    ]
