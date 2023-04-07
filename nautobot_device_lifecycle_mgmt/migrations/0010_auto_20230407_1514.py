# Generated by Django 3.2.15 on 2023-04-07 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_device_lifecycle_mgmt', '0009_software_remove_image_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicesoftwarevalidationresult',
            name='valid_software',
            field=models.ManyToManyField(related_name='_nautobot_device_lifecycle_mgmt_devicesoftwarevalidationresult_valid_software_+', to='nautobot_device_lifecycle_mgmt.ValidatedSoftwareLCM'),
        ),
        migrations.AddField(
            model_name='inventoryitemsoftwarevalidationresult',
            name='valid_software',
            field=models.ManyToManyField(related_name='_nautobot_device_lifecycle_mgmt_inventoryitemsoftwarevalidationresult_valid_software_+', to='nautobot_device_lifecycle_mgmt.ValidatedSoftwareLCM'),
        ),
        migrations.AlterField(
            model_name='devicesoftwarevalidationresult',
            name='software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nautobot_device_lifecycle_mgmt.softwarelcm'),
        ),
    ]
