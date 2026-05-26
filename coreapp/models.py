from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    address=models.CharField(max_length=200)
    contact=models.CharField(max_length=10)
    email=models.EmailField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name



