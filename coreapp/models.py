from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    address=models.CharField(max_length=200)
    contact=models.CharField(max_length=10)
    DOB = models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    video = models.FileField(upload_to='videos/',null=True,blank=True)
    pdf = models.FileField(upload_to='pdfs/',null=True,blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name



