# Generated by Django 5.0.1 on 2025-06-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0002_rename_tanggal_artikel_created_at_artikel_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='artikel_images/'),
        ),
    ]
