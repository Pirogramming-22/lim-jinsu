from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100)  
    year = models.IntegerField()  
    genre = models.CharField(max_length=50)  
    director = models.CharField(max_length=100)  
    cast = models.TextField()  
    rating = models.FloatField()  
    runtime = models.IntegerField()  
    review = models.TextField()  

    def __str__(self):
        return self.title 
