from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .members import MemberOfParliament

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class Ticket(models.Model):

    PRIORITY_OPTIONS = [
        ("1", "Low"),
        ("2", "Medium"),
        ("3", "High")
    ]
    STATUS_OPTIONS = [
        ("Pending", "Pending"),
        ("Open", "Open"),        
        ("Postponed", "Postponed"),
        ("Closed", "Closed")
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mp = models.ForeignKey(MemberOfParliament, on_delete=models.CASCADE)
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    parish = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    priority = models.CharField(max_length=50, choices=PRIORITY_OPTIONS)
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS)

    class Meta:
        verbose_name = ("Ticket")
        verbose_name_plural = ("Tickets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Ticket_detail", kwargs={"pk": self.pk})


