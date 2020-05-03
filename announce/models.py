from django.db import models
from django.urls import reverse

from yunanion import settings


class Announce(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    GOOD_TYPE_CHOICES = [
        ('ST', 'Studio'),
        ('T1', 'Appart T1'),
        ('T2', 'Appart T2'),
        ('T3', 'Appart T3'),
        ('T4', 'Appart T4'),
    ]
    appart_type = models.CharField(max_length=2, choices=GOOD_TYPE_CHOICES)
    space = models.DecimalField(max_digits=3, decimal_places=0)
    image = models.ImageField(upload_to="images/")

    def get_absolute_url(self):
        return reverse("announce:announce-detail", kwargs={"id": self.id})
