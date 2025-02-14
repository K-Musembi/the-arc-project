#!/usr/bin/python3
"""book class module"""

from django.db import models
from .base_model import BaseModel


class Book(BaseModel):
    """book class"""
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        """return book instance as string"""
        return f"Book {self.title} by {self.author} (ID: {self.id}, Created: {self.created_at})"
