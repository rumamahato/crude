from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator


# IMAGE VALIDATION
def validate_image(file):
    valid_mime_types = ['image/jpeg', 'image/png', 'image/jpg']
    if file.content_type not in valid_mime_types:
        raise ValidationError("Only JPG, JPEG and PNG image allowed")


# VIDEO VALIDATION
def validate_video(file):
    valid_mime_types = ['video/mp4']
    if file.content_type not in valid_mime_types:
        raise ValidationError("Only MP4 video allowed")


# PDF VALIDATION
def validate_pdf(file):
    if file.content_type != 'application/pdf':
        raise ValidationError("Only PDF file allowed")


# MODEL
class student(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    address = models.CharField(max_length=200)
    contact = models.CharField(
    max_length=10,
    validators=[RegexValidator(r'^\d{10}$', "Enter valid 10-digit number")])
    DOB = models.DateField(null=True, blank=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/',null=True,blank=True,validators=[validate_image])
    video = models.FileField(upload_to='videos/',null=True,blank=True,validators=[validate_video])
    pdf = models.FileField(upload_to='pdfs/',null=True,blank=True,validators=[validate_pdf])

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name