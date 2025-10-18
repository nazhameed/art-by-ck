from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsubmission',
            name='inquiry_type',
            field=models.CharField(
                choices=[
                    ('general', 'General Inquiry'),
                    ('purchase', 'Purchase Interest'),
                    ('exhibition', 'Exhibition Inquiry'),
                    ('other', 'Other'),
                ],
                default='general',
                help_text='Type of inquiry',
                max_length=20,
            ),
        ),
    ]
