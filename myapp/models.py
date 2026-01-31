from django.db import models

class Item(models.Model):

    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Returned', 'Returned'),
    ]

    item_name = models.CharField(max_length=100)
    description = models.TextField()
    location_found = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.item_name

