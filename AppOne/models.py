"""
Author :    Marc Taron
Version :   1.0
Name :      AppOne/models.py
Date :      XX/XX/XX

Docstring : This file define the differents models of the AppOne
"""

from django.db import models
# Imported as foreignkey
from django.contrib.auth.models import User

# Create your models here.


# Example of a model : Many-to-one : one Book can only have one User and one User can have multiple Book
class Book(models.Model):
    # ForeignKey define a many-to-one relation : one User can have many Books
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    # Other typical fields for a model
    # Define a list that the user will have to chose in
    BOOK_GENRES = (
        (1, "Roman"), (2, "Science-fiction"), (3, "Fantasy"), (4, "Policier"), (5, "Théâtre"), (6, "Poésie"),
        (7, "Conte"),
        (8, "Biographie"), (9, "Philosophie"), (10, "Nouvelles"))
    # CharField : any character, has to have a max_length, blank and null = True mean that it can be empty, default
    # give a default value
    genre = models.CharField(max_length=256, blank=True, null=True, default=None)
    title = models.CharField(max_length=256, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True)
    picture = models.URLField()
    like = models.IntegerField(blank=True, null=True)
    shared = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(blank=True, null=True)


# Example of a model : Many-to-Many : one Character can be in many Chapter and one Chapter can have many Character
class Character(models.Model):
    chapter = models.ManyToManyField(Chapter, related_name='characters')  # manytomany


# Example of a model : One-to-One : one Profile can have one User and one User can have one Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
