# Generated by Django 4.1.7 on 2023-03-25 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_index_user_student_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='collage',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]