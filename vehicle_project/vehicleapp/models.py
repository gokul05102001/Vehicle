from django.db import models

# Create your models here.
class vehicles(models.Model):
    image=models.ImageField(upload_to='images')
    company=models.CharField(max_length=250)
    price=models.IntegerField()
    features=models.TextField()

    def __str__(self):
        return self.company