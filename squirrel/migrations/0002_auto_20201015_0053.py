# Generated by Django 2.2.7 on 2020-10-15 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Approaches',
            new_name='approaches',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Chasing',
            new_name='chasing',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Climbing',
            new_name='climbing',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Eating',
            new_name='eating',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Foraging',
            new_name='foraging',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Indifferent',
            new_name='indifferent',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Kuks',
            new_name='kuks',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='X',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Y',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Moans',
            new_name='moans',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Other_activities',
            new_name='other_activities',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Primary_fur_color',
            new_name='primary_fur_color',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Quaas',
            new_name='quaas',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Running',
            new_name='running',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Runs_from',
            new_name='runs_from',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Specific_location',
            new_name='specific_location',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Tail_twitches',
            new_name='tail_twitches',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='Unique_squirrel_id',
            new_name='unique_squirrel_id',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='Shift',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='Tail_flags',
        ),
        migrations.AddField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Squirrel sighting session occured in morning or afternoon', max_length=100),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(default=False, help_text='Squirrel was seen flagging tail'),
        ),
    ]