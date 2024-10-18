# Generated by Django 5.1.2 on 2024-10-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_posts_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='link_image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
