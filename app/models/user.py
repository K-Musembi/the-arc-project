#!/usr/bin/env python3
"""user class module"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from .base_model import BaseModel


class User(AbstractUser, BaseModel):
    """
    Django auth: AbstractUser class already defines the following fields:
    - username
    - first_name
    - last_name
    - email
    - password
    - last_login
    - is_superuser
    - is_staff
    - is_active
    - date_joined
    """

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='app_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='app_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        """return user instance as string"""
        return f"User {self.first_name} {self.last_name} (ID: {self.id}, Created {self.created_at})"
