from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    learnings = models.CharField(max_length=2000)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class WishlistBook(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class CurrentBook(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name