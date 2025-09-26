from django.db import migrations, models

def seed_items(apps, schema_editor):
    Item = apps.get_model('pages', 'Item')
    Item.objects.bulk_create([
        Item(name='Notebook'),
        Item(name='Backpack'),
        Item(name='Water Bottle'),
    ])

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RunPython(seed_items, migrations.RunPython.noop),
    ]
