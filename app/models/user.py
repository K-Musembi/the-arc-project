#!/usr/bin/python3
"""user class module"""

from django.db import models
from .base_model import BaseModel


class User(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=512)

    def __str__(self):
        return f"User {self.first_name} {self.last_name} (ID: {self.id}, Created {self.created_at})"
    