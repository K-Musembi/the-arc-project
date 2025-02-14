#!/usr/bin/python3
"""base model module"""

from django.db import models


class BaseModel(models.Model):
    """base model class"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # BaseModel should be an abstract class.
    
    def save(self, *args, **kwargs):
        """save instance to database"""
        super().save(*args, **kwargs)
    
    def find(self):
        """find all instances"""
        return self.objects.all()
    
    def find_one(self, **kwargs):
        """find one instance / object"""
        return self.objects.get(**kwargs)
    
    def delete(self, *args, **kwargs):
        """delete current instance from db"""
        super().delete(*args, **kwargs)
