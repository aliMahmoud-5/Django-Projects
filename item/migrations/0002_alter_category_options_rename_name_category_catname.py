# Generated by Django 4.2.1 on 2023-05-24 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('catName',), 'verbose_name_plural': 'Catergories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='catName',
        ),
    ]
