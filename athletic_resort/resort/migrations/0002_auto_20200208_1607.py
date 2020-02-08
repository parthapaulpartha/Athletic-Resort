# Generated by Django 2.2.3 on 2020-02-08 10:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resort', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort_room',
            name='room_type',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Triple', 'Triple'), ('Quad', 'Quad'), (' Queen', ' Queen'), ('King', 'King'), ('Twin', 'Twin'), (' Hollywood twin room', ' Hollywood Twin Room'), ('Double-double', 'Double-double'), ('Studio', 'Studio'), ('Executive suite', 'Executive Suite'), ('Mini suite or Junior suite', 'Mini Suite or Junior Suite'), ('President suite ', 'President Suite'), ('Apartments ', 'Apartments '), ('Connecting rooms', 'Connecting rooms'), ('Murphy room', 'Murphy Room'), ('Accessible room ', 'Accessible Room '), ('Cabana', 'Cabana'), ('Adjoining rooms', 'Adjoining rooms'), ('Adjacent rooms', 'Adjacent rooms'), ('Villa', 'Villa'), ('Floored room', 'Floored Room'), ('Smoking ', 'Smoking ')], max_length=50),
        ),
        migrations.CreateModel(
            name='notepad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_pad', models.TextField(default='', max_length=900)),
                ('name', models.ForeignKey(default=None, on_delete='', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Note Pad',
            },
        ),
    ]
