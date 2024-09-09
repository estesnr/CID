from django.db import models
from django import forms


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AuthenticationForm(models.Model):
    username = models.CharField(max_length=63)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class SearchForm(models.Model):
    search = models.CharField(max_length=100)

    def __str__(self):
        return self.search