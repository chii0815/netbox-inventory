# Generated by Django 4.0.8 on 2022-10-24 13:07

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
from utilities.json import CustomFieldJSONEncoder


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenancy', '0007_contact_link'),
        ('extras', '0077_customlink_extend_text_and_url'),
        ('dcim', '0161_cabling_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='netbox_inventory.supplier')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ['supplier', 'name'],
                'unique_together': {('supplier', 'name')},
            },
        ),
        migrations.CreateModel(
            name='InventoryItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('model', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('part_number', models.CharField(blank=True, max_length=50)),
                ('comments', models.TextField(blank=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inventoryitem_types', to='dcim.manufacturer')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ['manufacturer', 'model'],
                'unique_together': {('manufacturer', 'slug'), ('manufacturer', 'model')},
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('name', models.CharField(blank=True, default='', max_length=128)),
                ('asset_tag', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('serial', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=30)),
                ('warranty_start', models.DateField(blank=True, null=True)),
                ('warranty_end', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(blank=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='tenancy.contact')),
                ('device', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_asset', to='dcim.device')),
                ('device_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dcim.devicetype')),
                ('inventoryitem', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_asset', to='dcim.inventoryitem')),
                ('inventoryitem_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='netbox_inventory.inventoryitemtype')),
                ('module', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_asset', to='dcim.module')),
                ('module_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dcim.moduletype')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='tenancy.tenant')),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assets', to='netbox_inventory.purchase')),
                ('storage_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dcim.location')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='tenancy.tenant')),
            ],
            options={
                'ordering': ('device_type', 'module_type', 'inventoryitem_type', 'serial'),
                'unique_together': {('device_type', 'serial'), ('owner', 'asset_tag'), ('module_type', 'serial'), ('inventoryitem_type', 'serial')},
            },
        ),
    ]
