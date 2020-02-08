from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class resort_room(models.Model):
    TYPE_CHOICES = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
        ('Quad', 'Quad'),
        (' Queen', ' Queen'),
        ('King', 'King'),
        ('Twin', 'Twin'),
        (' Hollywood twin room', ' Hollywood Twin Room'),
        ('Double-double', 'Double-double'),
        ('Studio', 'Studio'),
        ('Executive suite', 'Executive Suite'),
        ('Mini suite or Junior suite', 'Mini Suite or Junior Suite'),
        ('President suite ', 'President Suite'),
        ('Apartments ', 'Apartments '),
        ('Connecting rooms', 'Connecting rooms'),
        ('Murphy room', 'Murphy Room'),
        ('Accessible room ', 'Accessible Room '),
        ('Cabana', 'Cabana'),
        ('Adjoining rooms', 'Adjoining rooms'),
        ('Adjacent rooms', 'Adjacent rooms'),
        ('Villa', 'Villa'),
        ('Floored room', 'Floored Room'),
        ('Smoking ', 'Smoking '),
    )
    room_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    room_image = models.ImageField(upload_to='room_image', default='')
    room_details = models.TextField(max_length=9000, default='')
    resort_name = models.CharField(max_length=20, default='Athletic_Resort')
    price = models.CharField(max_length=100, default='')
    capacity = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.room_type

    class Meta:
        verbose_name_plural = 'Resort Room'

#----- Note Pad ----------
class notepad(models.Model):
    name = models.ForeignKey(User, default=None, on_delete='')
    note_pad = models.TextField(max_length=900, default='')
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Note Pad'