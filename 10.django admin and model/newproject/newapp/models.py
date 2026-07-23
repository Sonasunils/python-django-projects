from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    date_of_birth=models.DateField()
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    published_date=models.DateField((""), auto_now=False, auto_now_add=False)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    available=models.BooleanField(default=True)
    def __str__(self):
        return self.title

