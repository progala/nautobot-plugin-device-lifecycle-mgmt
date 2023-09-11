from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nautobot_device_lifecycle_mgmt", "0016b_post_nautobot_v2_migrations"),
    ]

    operations = [
        migrations.AddField(
            model_name="cvelcm",
            name="affected_softwares",
            field=models.ManyToManyField(
                blank=True, related_name="corresponding_cves", to="nautobot_device_lifecycle_mgmt.SoftwareLCM"
            ),
        ),
        migrations.AddField(
            model_name="contractlcm",
            name="devices",
            field=models.ManyToManyField(blank=True, related_name="device_contracts", to="dcim.Device"),
        ),
    ]
