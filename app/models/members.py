# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Region(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Region")
        verbose_name_plural = ("Regions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Region_detail", kwargs={"pk": self.pk})

class District(models.Model):

    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("District")
        verbose_name_plural = ("Districts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("District_detail", kwargs={"pk": self.pk})

class Constituency(models.Model):

    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("Constituency")
        verbose_name_plural = ("Constituencys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Constituency_detail", kwargs={"pk": self.pk})

class MemberOfParliament(models.Model):

    GENDER_OPTIONS =[
        ("Male", "Male"),
        ("Female", "Female")
    ]
    TYPE_OPTIONS =[
        ("MP", "MP"),
        ("Woman", "Woman")
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_OPTIONS)
    member_type = models.CharField(max_length=50, choices=TYPE_OPTIONS)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


    class Meta:
        verbose_name = ("MemberOfParl")
        verbose_name_plural = ("MemberOfParls")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MemberOfParl_detail", kwargs={"pk": self.pk})

