#!/usr/bin/python3
"""borrow class module"""

from django.db import models
from .base_model import BaseModel


class Borrow(BaseModel):
    """borrow class"""
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='borrower')
    book = models.ForeignKey(
        'Book', on_delete=models.CASCADE, related_name='borrowed')
    is_borrowed = models.BooleanField(default=False)
    return_date = models.DateTimeField(null=True)

    def __str__(self):
        """return borrow class as string"""
        return f"Borrowed by {self.user} (ID: {self.id}, Created: {self.created_at})"
