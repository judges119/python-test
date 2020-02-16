from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class PageView(models.Model):
    application = models.CharField(max_length=75)
    hits = models.IntegerField(default=0)
